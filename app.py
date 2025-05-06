# Temporary hacks for Python 3.13 compatibility
import sys, types, traceback
# Stub for cgi module removed in Python 3.13
fake_cgi = types.ModuleType('cgi')
def parse_header(value): return value, {}
fake_cgi.parse_header = parse_header
fake_cgi.parse_multipart = lambda *args, **kwargs: ({}, None)
sys.modules['cgi'] = fake_cgi
# Stub missing httpx exceptions
import httpx
httpx.ConnectError = Exception
httpx.ReadTimeout = Exception

import arxiv
import gradio as gr
from transformers import pipeline
from googletrans import Translator as GoogleTranslator  # working translation tool 

# Global storage
latest = []
# Models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn") 
gt = GoogleTranslator()

# Simplify text
def simplify_text(text):
    prompt = f"explain in simple terms: {text}"
    try:
        return summarizer(prompt, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]
    except Exception as e:
        print(traceback.format_exc())
        return f"Error: {e}"

# Translate to Spanish (other languages can be added)
def translate_to_es(text):
    try:
        return gt.translate(text, dest='es').text
    except Exception as e:
        print(traceback.format_exc())
        return f"Error: {e}"

# Fetch papers
client = arxiv.Client()
def fetch_papers(keyword):
    global latest
    try:
        search = arxiv.Search(query=f"ti:{keyword}", max_results=10, sort_by=arxiv.SortCriterion.SubmittedDate) #searching the last added 10 papers, when available
        latest = []
        titles = []
        for paper in client.results(search=search):
            latest.append({"title": paper.title, "abstract": paper.summary})
            titles.append(paper.title)
        # Enable Show button after fetch
        return gr.update(choices=titles, value=titles[0]), gr.update(interactive=True)
    except Exception:
        print(traceback.format_exc())
        return gr.update(choices=[], value=None), gr.update(interactive=False)

# Show abstract
def show_details(title):
    try:
        for p in latest:
            if p["title"] == title:
                summary = summarizer(p["abstract"], max_length=200, min_length=50, do_sample=False)[0]["summary_text"]
                return p["abstract"], summary
        return "Not found.", ""
    except Exception:
        print(traceback.format_exc())
        return "Error loading abstract.", "Error loading summary."

demo = gr.Blocks(css="""
  :root {
    --body-background-fill: #edfaff !important;
  }
  gradio-app {
    background: var(--body-background-fill) !important;
  }
  
  button#fetch-btn,
  button#show-btn,
  button#simplify-btn,
  button#translate-btn {
    background-image: none        !important;
  }

  /* Fetch Papers */
  button#fetch-btn {
    background-color: #4CAF50     !important;
    color: white                  !important;
    border: none                  !important;
  }
  button#fetch-btn:hover {
    background-color: #45A049     !important;
  }

  /* Show Details */
  button#show-btn {
    background-color: #2196F3     !important;
    color: white                  !important;
    border: none                  !important;
  }
  button#show-btn:hover {
    background-color: #1E88E5     !important;
  }

  /* Make Simpler */
  button#simplify-btn {
    background-color: #FFA000     !important;
    color: white                  !important;
    border: none                  !important;
  }
  button#simplify-btn:hover {
    background-color: #FF8F00     !important;
  }

  /* Translate to Spanish */
  button#translate-btn {
    background-color: #9C27B0     !important;
    color: white                  !important;
    border: none                  !important;
  }
  button#translate-btn:hover {
    background-color: #7B1FA2     !important;
  }
""").queue()



with demo:
    gr.Markdown("## Computer Science Paper Explorer & Explainer")
    input_kw = gr.Textbox(label="Enter keyword to search arXiv")
    fetch_btn = gr.Button("Fetch Papers", elem_id="fetch-btn")
    dropdown = gr.Dropdown(label="Select a paper title", choices=[], elem_id="paper-dropdown")
    show_btn = gr.Button("Show Abstract", elem_id="show-btn", interactive=False)

    with gr.Row():
        with gr.Column(): abstract_box = gr.Textbox(label="Abstract", lines=10)
        with gr.Column(): summary_box = gr.Textbox(label="Initial Explanation", lines=10)
    simplify_btn = gr.Button("Make Simpler", elem_id="simplify-btn")
    translate_btn = gr.Button("Translate to Spanish", elem_id="translate-btn")
    translation_box = gr.Textbox(label="Explicación en Español", lines=10)

    fetch_btn.click(fetch_papers, inputs=[input_kw], outputs=[dropdown, show_btn], queue=True)
    show_btn.click(show_details, inputs=[dropdown], outputs=[abstract_box, summary_box], queue=True)
    simplify_btn.click(simplify_text, inputs=[summary_box], outputs=[summary_box], queue=True)
    translate_btn.click(translate_to_es, inputs=[summary_box], outputs=[translation_box], queue=True)

    
    
if __name__ == "__main__":
    demo.launch(share=True)
