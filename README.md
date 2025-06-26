# Trend AI Agent

This project fetches news via NewsAPI, analyzes trending topics, detects breakpoints, recommends investments, and visualizes everything via Streamlit.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. (Optional) Set your own NewsAPI key:
   ```bash
   export NEWS_API_KEY=your_api_key
   ```
   The scripts default to an example key if not provided.

## Usage

Run the pipeline in order:

```bash
python trend_fetch_newsapi.py
python trend_analyzer.py
python trend_breakpoint_detector.py
python trend_investment_recommender.py
```

Then launch the dashboard:

```bash
streamlit run dashboard.py
```

## GitHub Actions

The workflow in `.github/workflows/update.yml` executes the above steps daily and commits updated JSON results back to the repository.
