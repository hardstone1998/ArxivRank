CREATE TABLE arxiv_papers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paper_id VARCHAR(255) NOT NULL UNIQUE,
    title TEXT,
    authors TEXT,
    summary TEXT,
    link TEXT,
    published DATETIME,
    updated_date DATETIME,
    categories TEXT
);
