# 模拟推荐逻辑
import json

with open("trend_keywords_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for trend in data:
    trend['recommendation'] = []
    for kw in trend['keywords']:
        if 'AI' in kw or 'ChatGPT' in kw:
            trend['recommendation'].append('NVIDIA')
        if 'EV' in kw:
            trend['recommendation'].append('TSLA')
        if 'Green Energy' in kw:
            trend['recommendation'].append('ICLN')

with open("trend_keywords_output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
