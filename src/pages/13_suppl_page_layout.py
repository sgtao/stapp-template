# 13_suppl_page_layout.py
import sys
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# サイドバー
with st.sidebar:
    url_input = "https://docs.streamlit.io/develop/api-reference/layout"
    st.markdown(f"[st Layouts and Containers]({url_input})")


# # メインページに移動
# st.page_link("main.py", label="Go to Main", icon="🏠")

st.title("Streamlit Layouts and Containers")
st.caption("これはサプーの動画用テストアプリです")

"""
動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8&t=1345s

- Streamlitのディフォルトレイアウトは上から下に部品が並べられます
- 左右方向のレイアウトしたいときは、`st.columns`を利用します
- `col1, col2 = st.column(2)`とすると２列のレイアウトを指定できます
"""

df = pd.read_csv("assets/data/temperature.csv", index_col="月")

col1, col2 = st.columns(2)

with col1:
    # データフレーム読み出し
    st.subheader("st.dataframe(df)")
    st.dataframe(df)
    st.subheader("st.table(df)")
    st.table(df)

with col2:
    # # 折れ線グラフ
    # st.subheader("st.line_chart(df)")
    # st.line_chart(df)

    # 棒グラフ
    st.subheader("st.bar_chart(df['2022年'])")
    st.bar_chart(df["2022年"])

    # matplotlib
    st.subheader("using matplotlib")
    fig, ax = plt.subplots()
    ax.plot(df.index, df["2022年"])
    ax.set_title("matplotlib graph")
    st.pyplot(fig)

"""
ページング：複数ページのコンテンツ作成
- 動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8&t=1461s
- １アプリで複数ページを作成するときは、`pages`フォルダ配下に各ページコンテンツを作成する
- `streamlit run`で起動するメインアプリのファイルからの相対パスで`pages`フォルダを作る(下例)
```sh
src
├── main.py
├── pages  # 各ページのコンテンツ
│   ├── 01_example_app.py
│   ├── 11_python_suppl_app.py
│   ├── 12_suppl_datavisual_app.py
│   └── 13_suppl_page_layout.py
├── components
└── functions
```
"""
