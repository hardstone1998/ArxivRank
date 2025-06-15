import os
import sys

import feedparser
from datetime import datetime
import time
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mapper.arxiv_paper import insert_paper, select_paper_by_paper_id

# 日志设置
logging.basicConfig(filename="arxiv_error.log", level=logging.ERROR)


def fetch_all_arxiv_papers(category="cs.AI", start_date_str="2023-01-01", skip_count=0):
    base_url = "http://export.arxiv.org/api/query?"
    start_index = skip_count
    max_results = 200
    delay_seconds = 3

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    total_inserted = skip_count

    try:
        while True:
            search_query = f"cat:{category}"
            sort_by = "submittedDate"
            url = (f"{base_url}search_query={search_query}"
                   f"&sortBy={sort_by}&sortOrder=descending"
                   f"&start={start_index}&max_results={max_results}")

            feed = feedparser.parse(url)
            entries = feed.entries

            if not entries:
                time.sleep(delay_seconds * 10)
                continue

            for i, entry in enumerate(entries):
                if total_inserted < skip_count:
                    total_inserted += 1
                    continue

                published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
                updated_date = datetime.strptime(entry.updated, "%Y-%m-%dT%H:%M:%SZ")
                if published_date < start_date:
                    return

                # 判断数据库中是否存在这个论文如果存在，直接跳过
                rs = select_paper_by_paper_id(entry.id)
                if len(rs) >= 1:
                    print("文章已经存在："+entry.id)
                    continue

                paper = {
                    "title": entry.title,
                    "authors": [author.name for author in entry.authors],
                    "summary": entry.summary,
                    "link": entry.link,
                    "published": published_date.strftime("%Y-%m-%d %H:%M:%S"),
                    "categories": [tag.term for tag in entry.tags],
                    "paper_id": entry.id,
                    "updated_date": updated_date,
                }

                try:
                    insert_paper(paper)
                    print(f"Inserted: {paper['title']}")
                    total_inserted += 1
                except Exception:
                    print(f"Failed at #{total_inserted}, logged to error log")
                    continue

            start_index += max_results
            time.sleep(delay_seconds)
    except Exception as e:
        print("total_inserted:", total_inserted)
        print(e)


# 使用时可指定 skip_count 跳过前几条数据
if __name__ == "__main__":
    fetch_all_arxiv_papers("cs.AI", start_date_str="2023-01-01", skip_count=0)
