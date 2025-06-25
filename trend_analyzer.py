import json
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

# 加载新闻数据
with open("trend_news_window.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 准备文本
texts = [item['translated_text'] for item in data]
vectorizer = TfidfVectorizer(max_features=100)
X = vectorizer.fit_transform(texts)

# 聚类
kmeans = KMeans(n_clusters=5, random_state=42).fit(X)
labels = kmeans.labels_

# 关键词聚合与统计
trend_clusters = defaultdict(list)
for i, item in enumerate(data):
    trend_clusters[labels[i]].append(item)

result = []
for cluster_id, items in trend_clusters.items():
    dates = [i['date'] for i in items]
    topics = list(set(i['topic'] for i in items))
    score = len(items)
    result.append({
        "cluster": cluster_id,
        "keywords": topics,
        "trend_score": score,
        "start_date": min(dates),
        "end_date": max(dates),
        "samples": items[:5]  # 截取样例展示
    })

with open("trend_keywords_output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
