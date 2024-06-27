# 01_example_app.py
import sys
import os
import streamlit as st
from PIL import Image

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

# サイドバー
with st.sidebar:
    url_input = "https://docs.streamlit.io/develop/api-reference/widgets"
    st.markdown(f"[st input widet api]({url_input})")


# # メインページに移動
# st.page_link("main.py", label="Go to Main", icon="🏠")

st.title("Python Suppl App")
st.caption("これはサプーの動画用テストアプリです")

"""
このアプリはサプー動画で紹介していたコードを実装してみたページです
動画URL: https://www.youtube.com/watch?v=4nsTce1Oce8
"""

st.subheader("他者紹介")
st.text(
    "Python VTuber サプーさんは、Python関連情報をYouTubeで発信してます\n"
    "よければチャンネル登録よろしくお願いします！"
)

code = """
import streamlit as st
st.title("Python Suppl App")
st.caption("これはサプーの動画用テストアプリです")
"""
st.code(code, language="python")


# 画像
st.subheader("画像")
image = Image.open("assets/images/sample_image.png")
st.image(image, width=200)

# 動画はスキップ
# st.video(video_file)


# 入力ウィジット
with st.form(key="profile_form"):
    st.subheader("入力ウィジット")

    # テキストボックス
    name = st.text_input("名前")
    address = st.text_input("住所")
    # print(name)

    # セレクトボックス
    age_category = st.radio(
        "年齢層", ("18才未満", "18才以上65才未満", "65才以上")
    )

    # 複数選択
    hobby = st.multiselect(
        "趣味", ("スポーツ", "読書", "アニメ", "釣り", "料理")
    )

    # チェックボックス
    mail_subscribe = st.checkbox("メールマガジンを購読する")

    # スライダー
    height = st.slider("身長", min_value=110, max_value=210)

    # カラーピッカー
    color = st.color_picker("テーマカラー", "#4600F9")

    # ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")

    # print(f"submit_btn: {submit_btn}")
    # print(f"cancel_btn: {cancel_btn}")
    if submit_btn:
        st.text(f"ようこそ!{name}さん！{address}に書籍を送りました！")
        st.text(f"年齢層：{age_category}")
        st.text(f"趣味：{', '.join(hobby)}")
        st.text(f"身長：{height} cm")
        st.text(f"メールマガジン購読：{mail_subscribe}")
        st.text(f"テーマカラー(コード)：{color}")
