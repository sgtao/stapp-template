# tests/test_main.py
from streamlit.testing.v1 import AppTest

def test_show_title():
    """show title"""
    at = AppTest.from_file("src/pages/01_example_app.py")
    at.run(timeout=30)  # タイムアウトを10秒に設定
    # assert at.title[0].value == "Hello World"
    assert "Welcome to " in at.markdown[0].value
