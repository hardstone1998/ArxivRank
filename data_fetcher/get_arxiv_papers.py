import feedparser
from datetime import datetime, timedelta


def get_arxiv_papers(category="cs.AI", reference_date=None, days_back=7, max_results=200):
    base_url = "http://export.arxiv.org/api/query?"
    # 如果没有传入 reference_date，使用当前日期
    if reference_date:
        ref_date = datetime.strptime(reference_date, "%Y-%m-%d")
    else:
        ref_date = datetime.now()

    start_date = ref_date - timedelta(days=days_back)

    search_query = f"cat:{category}"
    sort_by = "submittedDate"

    url = f"{base_url}search_query={search_query}&sortBy={sort_by}&sortOrder=descending&max_results={max_results}"

    feed = feedparser.parse(url)

    papers = []
    for entry in feed.entries:
        published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%SZ")
        if start_date <= published_date <= ref_date:
            paper = {
                "title": entry.title,
                "authors": [author.name for author in entry.authors],
                "summary": entry.summary,
                "link": entry.link,
                "published": entry.published,
                "categories": [tag.term for tag in entry.tags],
                "id": entry.id,
            }
            papers.append(paper)

    return papers


# 示例用法
papers = get_arxiv_papers("cs.AI", reference_date="2025-06-12", days_back=7)
for p in papers:
    print("-------------------")
    print(p["title"])
