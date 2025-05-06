
# 🧠 Scientific Paper Explorer & Explainer

🙏Thank you to arXiv for use of its open access interoperability. This is an independent and non-commercial project.

A Gradio-based web application to search scientific papers on arXiv, generate simplified summaries, and provide translations (so far into Spanish). Developed as part of an NLP and data science learning journey, the project emphasizes real-world applications of transformers, multilingual processing, and UI integration.

---

## 💬 Imagine you hear a team member mention a new ML model, a framework, an algorithm ...

- and you want to quickly grasp the essence to discuss its integration into your ML operations.
- or you want to get a scientifically proven reason to better communicate with non-technical stakeholders.
- or your English is... well...you can read papers. But you feel more confident when reading in your native language (e.g. Spanish)
- or your Dad asked you what is it that you actually do at your tech job, but you lack simple terms to explain?




---

## 🚀 Use Case

My idea was that, as modern science moves so quickly, sometimes we do not even have enough time to process the findings before they are beaten by an improved solution.  And there is no better feeling than understanding something new on your own.
With a help of an Explorer and Explainer, for example.

I hope that it lays a foundation for a multilingual, representative and accessible research papers system that I had in mind as a personal project since I started learning Data Science.

So far, with the first version, you can:

- 📚 **Search** for the latest academic papers (max 10) on a given topic (via arXiv API)
- ✏️ **Summarize** fetched abstracts using transformer-based summarization (BART)
- 💬 **Simplify** complex content for easier understanding
- 🌍 **Translate** summaries into Spanish (via Google Translate)

As a researcher, I would love to have something like that at the beginning of my journey.

---
![Alt text](https://github.com/NataliiaPopkova/Scientific-Paper-Explorer-and-Explainer/blob/main/1.png)

The first explanation of the abstract might even be enough. But if you coould use a clearer version to better understand the idea...

![Alt text](https://github.com/NataliiaPopkova/Scientific-Paper-Explorer-and-Explainer/blob/main/2.png)

... a "Make Simpler" button could be used. The translation function can be applied both to the initial and the simplified version.

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

- [ ] Resolve **version issue** and improve styles code, getting rid of the temporal solutions 
- [ ] Allow **language selection** for translation (another model will be selected) 
- [ ] Add support for **PDF direct download**  
- [ ] Keywords: **extract them**? Recommend other titles based on this? 
- [ ] Consider hosting at a cloud-based platform like **AWS** 

---



## ▶️ Live Demo

[Launch the demo here](https://4ffb7d8df33b778f2f.gradio.live)  
_(Hosted via Gradio share link - please ask me for an updated one)_
