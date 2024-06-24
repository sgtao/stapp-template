# 01_example_app.py
import streamlit as st

# # メインページに移動
# st.page_link("main.py", label="Go to Main", icon="🏠")

st.title("Python Suppl App")
st.caption("これはサプーの動画用テストアプリです")

"""
このアプリはサプー動画で紹介していたコードを実装してみるページです
動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8
"""

st.subheader("自己紹介")
st.text(
    "Python関連情報をYouTubeで発信しているPython VTuber サプーです\n"
    "よければチャンネル登録よろしくお願いします！"
)
