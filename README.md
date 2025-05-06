
# 🧠 ArXiv Paper Explorer & Explainer

A Gradio-based web application to search scientific papers on arXiv, generate simplified summaries, and provide translations in Spanish. Developed as part of an NLP and data science learning journey, the project emphasizes real-world applications of transformers, multilingual processing, and UI integration.

---

## 🚀 Use Case

This tool is designed for students, junior data scientists, researchers, and non-native English speakers who want to:

- 📚 **Search** for the latest academic papers on a given topic (via arXiv API)
- ✏️ **Summarize** abstracts using transformer-based summarization (BART)
- 💬 **Simplify** complex content for easier understanding
- 🌍 **Translate** summaries into Spanish (via Google Translate)

It's particularly useful in multilingual research teams or educational settings where access to simplified and translated content is valuable.

---

## ⚙️ Features

- **Gradio UI** built with custom CSS styling  
- **Transformers pipeline** for summarization using `facebook/bart-large-cnn`  
- **Google Translate API** (`googletrans`) for Spanish translation  
- **arXiv API** integration for real-time paper search  
- **Live demo deployment** via Gradio share link  

---

## 📊 Stack

| Technology      | Purpose                                 |
|----------------|------------------------------------------|
| `Python 3.13`  | Main language                            |
| `Gradio`       | Web interface                            |
| `transformers` | NLP (summarization)                      |
| `googletrans`  | Translation to Spanish                   |
| `arxiv`        | Paper search API                         |

---

## 🛠️ Challenges Faced

- **Python 3.13 compatibility**  
  The `cgi` module was removed in Python 3.13, breaking `arxiv` package compatibility. A temporary shim was added to patch it at runtime:
  ```python
  import sys, types
  fake_cgi = types.ModuleType('cgi')
  ...
  sys.modules['cgi'] = fake_cgi
  ```

- **Gradio styling issues**  
  Gradio ignores some native CSS selectors. To apply custom button styling, we had to use `elem_id` with proper specificity and `!important` declarations.

- **Live debugging via browser DevTools**  
  Used Chrome DevTools to inspect shadow DOM and figure out why styles weren’t applying. Ensured that styles were injected correctly and not overridden.

---

## 📈 What’s Next

- [ ] Add **metadata filtering** (e.g., by subject area or date)  
- [ ] Implement **Spanish summarization** directly (using multilingual models like mBART or mT5)  
- [ ] Add support for **PDF upload and summarization**  
- [ ] Store and **rank saved papers** with a personal note system  
- [ ] Deploy via **Hugging Face Spaces** with authentication  

---

## 💼 Relevance to Junior DS/NLP Roles

This project demonstrates:

- Ability to build complete data + NLP pipelines  
- UI + UX thinking with Gradio and CSS  
- Troubleshooting in modern Python environments (Python 3.13)  
- Use of Hugging Face transformers in production-level workflows  
- Awareness of multilingual NLP and accessibility  

---

## ▶️ Live Demo

[Launch the demo here](https://e1fe8ba7bbfa1ca98c.gradio.live)  
_(Hosted via Gradio share link — may take a moment to load if asleep)_
