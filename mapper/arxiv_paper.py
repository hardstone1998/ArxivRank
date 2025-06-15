from tools.ConnectMysqlPool import ConnectMysqlPool
from tools.load_config import load_config
import logging

cmp = ConnectMysqlPool()

def select_paper_by_paper_id(paper_id:str):
    try:
        sql = "select * from arxiv_papers where paper_id = %s"
        params = (paper_id,)
        rs = cmp.execute(sql, params)
        logging.info(f"查询数据库成功,result:{rs}")
    except Exception as e:
        logging.error("查询数据库异常")
        raise Exception(e)
    return rs

# 逐条插入论文
def insert_paper(paper):
    try:
        sql = """
        INSERT INTO arxiv_papers (paper_id, title, authors, summary, link, published, updated_date, categories)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        rs = cmp.execute(sql, (
                paper["paper_id"],
                paper["title"],
                ", ".join(paper["authors"]),
                paper["summary"],
                paper["link"],
                paper["published"],
                paper["updated_date"].strftime("%Y-%m-%d %H:%M:%S"),
                ", ".join(paper["categories"])))
        logging.info(f"插入数据库成功,result:{rs}")
    except Exception as e:
        logging.error(f"Error at paper ID {paper['paper_id']}: {str(e)}")
        print(e)
        raise  # 可选择是否终止或跳过继续
