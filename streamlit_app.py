
import streamlit as st
import json

st.set_page_config(page_title="趋势关键词分析", layout="wide")
st.title("📈 AI趋势关键词分析仪表盘")

# 读取JSON数据
try:
    with open("trend_keywords_output.json", "r", encoding="utf-8") as f:
        trends = json.load(f)
except FileNotFoundError:
    st.error("找不到关键词数据文件，请先运行数据采集器。")
    st.stop()

# 展示每个趋势
for trend in trends:
    st.subheader(f"📰 {trend['source_text']}")
    st.write(f"📅 日期: {trend['date']}")
    st.write(f"🔥 趋势评分: {trend['trend_score']}")
    if trend["keywords"]:
        st.markdown("**关键词链条：**")
        for kw in trend["keywords"]:
            st.write(f"- **{kw['core_keyword']}** → {', '.join(kw['related'])}")
    st.markdown("---")
