# 12_suppl_datavisual_app.py
import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# サイドバー
with st.sidebar:
    url_input = "https://docs.streamlit.io/develop/api-reference/charts"
    st.markdown(f"[st Chart elements]({url_input})")


# # メインページに移動
# st.page_link("main.py", label="Go to Main", icon="🏠")

st.title("Python DataVisualization App")
st.caption("これはサプーの動画用テストアプリです")

"""
このアプリはサプー動画で紹介していたコードを実装してみたページです
動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8&t=1108s
"""


# データフレーム読み出し
df = pd.read_csv("assets/data/temperature.csv", index_col="月")

st.subheader("st.dataframe(df)")
st.dataframe(df)
st.subheader("st.table(df)")
st.table(df)

# 折れ線グラフ
st.subheader("st.line_chart(df)")
st.line_chart(df)

# 棒グラフ
st.subheader("st.bar_chart(df['2022年'])")
st.bar_chart(df["2022年"])


# matplotlib
st.subheader("using matplotlib")
fig, ax = plt.subplots()
ax.plot(df.index, df["2022年"])
ax.set_title("matplotlib graph")
st.pyplot(fig)
