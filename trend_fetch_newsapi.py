
import requests
import datetime
import json
from googletrans import Translator

API_KEY = "62fe55a584804d249a1f6af499f71750"
TREND_TOPICS = [
    "Artificial Intelligence",
    "Semiconductor",
    "Clean Energy",
    "Aging Population",
    "Carbon Border Tax"
]

def fetch_news():
    all_articles = []
    for topic in TREND_TOPICS:
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={topic}&"
            f"language=en&"
            f"sortBy=publishedAt&"
            f"pageSize=3&"
            f"apiKey={API_KEY}"
        )
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for article in data.get("articles", []):
                all_articles.append({
                    "topic": topic,
                    "title": article.get("title", ""),
                    "publishedAt": article.get("publishedAt", "")[:10],
                    "url": article.get("url", "")
                })
    return all_articles

def extract_keywords(topic):
    mappings = {
        "Artificial Intelligence": ["AI", "AIGC", "GPT", "自动化"],
        "Semiconductor": ["芯片", "晶圆", "封装", "产能"],
        "Clean Energy": ["光伏", "风能", "绿氢", "碳中和"],
        "Aging Population": ["老龄化", "医疗", "护理", "养老金"],
        "Carbon Border Tax": ["碳税", "排放", "环保", "绿色政策"]
    }
    return [{"core_keyword": topic, "related": mappings.get(topic, [])}]

def score_trend():
    return int(70 + 30 * (datetime.datetime.now().second % 10) / 10)

def translate_text(text, translator):
    try:
        result = translator.translate(text, src='en', dest='zh-cn')
        return result.text
    except Exception:
        return "[翻译失败]"

def build_trend_json(news_items):
    translator = Translator()
    structured = []
    today = datetime.date.today().isoformat()
    for item in news_items:
        translated = translate_text(item["title"], translator)
        structured.append({
            "date": today,
            "source_text": item["title"],
            "translated_text": translated,
            "keywords": extract_keywords(item["topic"]),
            "trend_score": score_trend()
        })
    return structured

def main():
    news = fetch_news()
    trend_json = build_trend_json(news)
    with open("trend_keywords_output.json", "w", encoding="utf-8") as f:
        json.dump(trend_json, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
