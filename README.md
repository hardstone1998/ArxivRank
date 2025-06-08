# ArxivRank
ArxivRank is an open-source project that automatically identifies and ranks the top 10 high-quality AI papers from arXiv each week.



# 🔍 ArxivRank – Weekly AI Paper Selection from arXiv

**ArxivRank** is an open-source project designed to automatically identify and rank the **top 10 high-quality AI papers from arXiv every week**. It aims to support initiatives like [dair-ai/ML-Papers-of-the-Week](https://github.com/dair-ai/ML-Papers-of-the-Week) and help researchers stay on top of cutting-edge work without information overload.

---

## 🎯 Project Goal

To develop an intelligent, scalable pipeline that:

- Retrieves the latest arXiv AI papers (weekly),
- Evaluates their quality using LLM + RAG techniques,
- Outputs the **Top 10 most impactful, novel, and well-written papers**,
- And optionally integrates with newsletters or community curation efforts.

---

## ⚙️ Key Technologies

- **RAG (Retrieval-Augmented Generation)** for context-aware analysis.
- **Large Language Models (LLMs)** for summarization, evaluation, and ranking.
- **Custom Prompting & Fine-tuning** for domain-specific understanding.
- **Multi-criteria Scoring System**, including:
  - Novelty
  - Technical soundness
  - Writing clarity
  - Potential impact
  - Community relevance

---

## 📦 Project Components (Planned)

- `data_fetcher/` – Collects weekly arXiv AI papers
- `embedder/` – Embeds abstracts and key sections for semantic analysis
- `evaluator/` – Applies prompts and scoring logic to rank papers
- `ranker/` – Combines scores across dimensions to select top 10
- `output/` – Generates markdown / JSON / newsletter-ready outputs

---

## 💡 Contributions Welcome

This project is in early development. **Ideas, feature suggestions, scoring criteria, and technical contributions are warmly welcome!**

Feel free to:
- Submit an issue with suggestions
- Create a pull request with improvements
- Join discussions on how to improve the scoring framework or prompt design

---

## 📄 License

[MIT License](LICENSE)

---

## 🌐 Related Projects

- [dair-ai/ML-Papers-of-the-Week](https://github.com/dair-ai/ML-Papers-of-the-Week)
- [arxiv-sanity-preserver](https://github.com/karpathy/arxiv-sanity-preserver)
- [paperswithcode.com](https://paperswithcode.com)

---