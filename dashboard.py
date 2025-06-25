import streamlit as st
import json

st.set_page_config(page_title="趋势关键词分析", layout="wide")
st.title("📈 AI趋势关键词分析仪表盘")

try:
    with open("trend_keywords_output.json", "r", encoding="utf-8") as f:
        trends = json.load(f)
except FileNotFoundError:
    st.error("找不到分析结果文件，请先运行分析模块。")
    st.stop()

for trend in trends:
    st.subheader(f"趋势群组 #{trend['cluster']}")
    st.write(f"📅 时间段: {trend['start_date']} ~ {trend['end_date']}")
    st.write(f"🔥 趋势评分: {trend['trend_score']}")
    st.write(f"📌 包含关键词: {', '.join(trend['keywords'])}")
    if trend.get('breakpoint_detected'):
        st.warning("⚠️ 拐点信号检测")
    if trend.get('recommendation'):
        st.success(f"💰 推荐标的: {', '.join(trend['recommendation'])}")
    st.markdown("---")
