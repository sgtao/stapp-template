# 12_suppl_datavisual_app.py
import sys
import os
import streamlit as st
import pandas as pd

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# サイドバー
with st.sidebar:
    url_input = "https://docs.streamlit.io/develop/api-reference/charts"
    st.markdown(f"[st chart widet api]({url_input})")


# # メインページに移動
# st.page_link("main.py", label="Go to Main", icon="🏠")

st.title("Python DataVisualization App")
st.caption("これはサプーの動画用テストアプリです")

"""
このアプリはサプー動画で紹介していたコードを実装してみたページです
動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8
"""


# データフレーム読み出し
df = pd.read_csv("assets/data/temperature.csv", index_col="月")
st.dataframe(df)
