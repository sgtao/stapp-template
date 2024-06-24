import streamlit as st

"""
# Welcome to Streamlit!

Edit `/src` and `/tests` to customize this app to your heart's desire :heart:.
"""

# サイドバーのページに移動
# st.page_link("pages/example_app.py", label="Go to Example App")
st.page_link("pages/01_example_app.py", label="Go to Example App", icon="🚀")
st.page_link(
    "pages/02_python_suppl_app.py", label="VTuberサプーの紹介コード", icon="👩"
)
