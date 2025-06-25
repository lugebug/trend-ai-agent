import os
import json
from datetime import datetime, timedelta
from newsapi.newsapi_client import NewsApiClient
from googletrans import Translator

# 设置 API 密钥和翻译器
newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY", "62fe55a584804d249a1f6af499f71750"))
translator = Translator()

# 设置关键词列表（可根据趋势扩展）
keywords = [
    "Artificial Intelligence", "Semiconductor", "EV", "Green Energy",
    "NVIDIA", "TSMC", "ChatGPT", "OpenAI"
]

# 设置时间范围（过去30天）
today = datetime.today()
from_date = (today - timedelta(days=30)).strftime('%Y-%m-%d')
to_date = today.strftime('%Y-%m-%d')

# 存储结果
trend_data = []

# 拉取每个关键词过去30天的新闻
for kw in keywords:
    try:
        articles = newsapi.get_everything(q=kw,
                                          from_param=from_date,
                                          to=to_date,
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=50)
        for article in articles['articles']:
            title = article['title']
            try:
                translated = translator.translate(title, src='en', dest='zh-cn').text
            except Exception:
                translated = "[翻译失败] " + title
            trend_data.append({
                "date": article["publishedAt"][:10],
                "source_text": title,
                "translated_text": translated,
                "source": article["source"]["name"],
                "topic": kw
            })
    except Exception as e:
        print(f"[警告] 抓取关键词 {kw} 出错: {e}")

# 保存文件
with open("trend_news_window.json", "w", encoding="utf-8") as f:
    json.dump(trend_data, f, ensure_ascii=False, indent=2)
