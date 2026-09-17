# Language Planning in Sociolinguistics — Sindhi & Regional Dialects

This started as a coursework analysis on language planning and policy for regional dialects, with Sindhi as the central case study. Instead of leaving it as a static write-up, I turned it into an interactive Streamlit app so the ideas — status/corpus/acquisition planning, globalization pressures, the tension between recognition and real vitality — are something you can click through, chart, and ask questions about, rather than just read.

## What's in here

- **Overview** — the core argument, plus a chart comparing Sindhi vs. Urdu/English usage across different domains (home, school, government, media), and a clickable map of where Sindhi is spoken in Sindh
- **Policy Development** — the three-level framework (status / corpus / acquisition planning) that the rest of the app builds on
- **Globalization & Standardization Pressures** — the two forces squeezing regional dialects, side by side in tabs
- **Challenges** and **Strategies** — what's working against Sindhi's preservation, and what the literature suggests could help
- **Case Study: Sindhi** — the strengths and ongoing pressures specific to Sindhi
- **Language Comparison Tool** — pick any combination of Pakistan's major regional languages and compare them using real 2023 census figures, plus their actual official/provincial status (Sindhi vs. Punjabi is a genuinely interesting contrast here)
- **Quick Quiz** and **Glossary** — a self-check and a searchable reference for the key terminology
- **Ask AI Assistant** — a live chat (powered by Groq) if you want to ask something the app doesn't directly cover
- **References** — the actual scholarly sources behind this (Rahman, Haugen, Fishman, UNESCO), because this app is a summary, not a citation

## Running it locally

```bash
git clone <your-repo-url>
cd <your-repo-folder>
pip install -r requirements.txt
streamlit run app.py
```

It'll open at `http://localhost:8501`.

### The AI Assistant needs an API key

The "Ask AI Assistant" page uses [Groq](https://console.groq.com) for fast LLM responses. To enable it locally, create `.streamlit/secrets.toml` in the project root:

```toml
GROQ_API_KEY = "your-key-here"
```

Don't commit this file — it's already covered by `.gitignore`. Without a key, every other page still works fine; that one page just shows a warning instead of a chat box.

## Deploying

This is built to run on [Streamlit Community Cloud](https://share.streamlit.io) for free:

1. Push this repo to GitHub (public, for the free tier)
2. On Streamlit Cloud, create a new app pointing at this repo, branch `main`, file `app.py`
3. Add your `GROQ_API_KEY` under the app's **Settings → Secrets** (not in the repo)
4. Deploy — you'll get a `yourapp.streamlit.app` link

## Tech stack

- **Streamlit** — the app framework
- **Plotly** — the charts and the interactive map
- **Pandas** — wrangling the small datasets behind the charts
- **Groq** (`openai/gpt-oss-120b`) — powers the AI assistant

## Design notes

The color palette and dividers are drawn from **Ajrak**, the traditional Sindhi block-print textile — indigo, madder red, and mustard ochre — rather than a generic dashboard theme. Felt more honest to the subject matter than defaulting to Streamlit's blue.

## A note on the content

The domain-usage percentages on the Overview page are illustrative, not measured survey data — they're there to make the *pattern* of language shift visible, not to claim precision. The language comparison figures, on the other hand, are real: they come from Pakistan's 2023 census. If you're citing anything from this project academically, go to the primary sources listed on the References page rather than this app.

## License

Educational project — feel free to fork, adapt, or build on it for your own coursework.
