# 01_example_app.py
import sys
import os
import streamlit as st
from PIL import Image

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# # メインページに移動
# st.page_link("main.py", label="Go to Main", icon="🏠")

st.title("Python Suppl App")
st.caption("これはサプーの動画用テストアプリです")

"""
このアプリはサプー動画で紹介していたコードを実装してみたページです
動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8
"""

st.subheader("自己紹介")
st.text(
    "Python関連情報をYouTubeで発信しているPython VTuber サプーです\n"
    "よければチャンネル登録よろしくお願いします！"
)

code = """
import streamlit as st
st.title("Python Suppl App")
st.caption("これはサプーの動画用テストアプリです")
"""
st.code(code, language="python")


# 画像
st.subheader("画像（sgtao画像です）")
image = Image.open("assets/images/sample_image.png")
st.image(image, width=200)
