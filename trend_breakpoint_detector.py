# 模拟拐点检测逻辑
import json
import datetime

with open("trend_keywords_output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for trend in data:
    # 模拟设定某一类趋势突然新闻量提升为拐点
    trend['breakpoint_detected'] = trend['trend_score'] > 20

with open("trend_keywords_output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
