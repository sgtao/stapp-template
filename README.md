# stpyapp-template
[streamlit](https://streamlit.io/)のアプリ開発するためのテンプレートを作ってみる

## コンテンツ
- サンプルコード（[streamlit-example](https://github.com/streamlit/streamlit-example)）を追加
- [PythonVtuber動画](https://www.youtube.com/watch?v=4nsTce1Oce8)のアプリを作ってみる

## Usage
- [poetry cli](https://cocoatomo.github.io/poetry-ja/cli/)を利用する

### Setup
```sh
poetry install
poetry shell
```

### コマンド一覧
```sh
$ task --list
start        streamlit run src/main.py
test         pytest tests
test-cov     pytest tests --cov --cov-branch -svx
test-repo    pytest tests --cov --cov-report=html
format       black --line-length 79 src
lint         flake8 src
check-format black整形とflake8チェックを実行
```

### Start as local service
```sh
# on poetry shell
# streamlit hello
# streamlit run src/main.py
task start
# Local URL: http://localhost:8501
```


### format and lint check
```sh
# task format
# task lint
task check-format
```


### Test with `pytest`
- [streamlitのテスト手法](https://docs.streamlit.io/develop/concepts/app-testing/get-started)を参考にテストを実施
```sh
# on poetry shell
# pytest tests/test_main.py
task test
```

### Test coverage

#### show c1 coverage
```sh
# on poetry shell
task test-cov
```

#### output HTML coverage report
```sh
# on poetry shell
task test-repo
```


## 他プロジェクトでの利用手順例
### 01. リポジトリURLの変更
- `git-clone`したあと、`git-remote`でoriginを変更する
```sh
PROJECT_NAME="stapp-excel2csv"
GITHUB_URL="https://github.com/sgtao/${PROJECT_NAME}.git"
git clone https://github.com/sgtao/stpyapp-template.git $PROJECT_NAME
cd  $PROJECT_NAME
# git remote add origin $GITHUB_URL
git remote set-url origin $GITHUB_URL
git branch -M main
# GitHub二リポジトリを作成したあとに`git-push`実施
git push -u origin main
```

### 02．`pyproject.toml`の変更
- `pyproject.toml`ファイルの`[tool.poetry]`グループを変更する
```toml
[tool.poetry]
- name = "stpyapp-template"
+ name = "csv_viewer"
version = "0.1.0"
- description = "streamlit project template for quick start"
- authors = ["Shogo Ogami <sg.tao.so@gmail.com>"]
- license = "Apache-2.0"
+ description = "CSV fileviewer" # 必要に応じて
+ authors = ["YYYY ZZZ <yyyy.zzz@gmail.com>"]
+ license = "MIT License" # 必要に応じて
```

### 03．`README.md`・`LICENSE`ファイルの変更
- `README.md`の変更：
  - タイトル、概要を変更する
  - LICENSEを変更する場合は、`README.md`の下段の表記と`LICENSE`ファイルを変更する

### 04．`src/pages`フォルダ配下などのページ更新
#### 04-1．例）`src/pages/11_csv_viewer.py`を作成
  - `task start`・`task check-format`などで確認
```py
import streamlit as st
import pandas as pd


def csv_viewer():
    st.title("CSVファイルアップローダー")

    ...

# if __name__ == '__main__':
#     csv_viewer()
csv_viewer()
```

#### 04-2．`tests/`フォルダにテストコード追加
- 例）`tests/test_pages_csv_viewer.py`を作成
```py
# test_pages_csv_viewer.py
import sys
import os
from streamlit.testing.v1 import AppTest

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

def test_show_title():
    """show title"""
    at = AppTest.from_file("src/pages/11_csv_viewer.py")
    at.run(timeout=30)  # タイムアウトを30秒に設定
    # print(f"at is {at}")
    assert at.title[0].value == "CSVファイルアップローダー"
```

### 05．テンプレートのファイルを削除
```sh
rm src/pages/01_example_app.py
rm src/components/spiral_chart.py src/functions/calculations.py
rm tests/test_pages_example_app.py
#
# 必要に応じてパッケージも削除
poetry remove altair
poetry remove pandas
#
# `src/main.py`のリンク削除
nano src/main.py
# 削除：st.page_link("pages/01_example_app.py", label="Go to Example App", icon="🚀")
```


## 使用ライブラリ

このプロジェクトは以下のオープンソースライブラリを使用しています：

- [Streamlit](https://streamlit.io/) - Apache License 2.0

  Copyright © 2019-2024 Streamlit Inc.

  Streamlitは、データアプリケーションを簡単に作成するためのオープンソースライブラリです。


## ライセンス
MIT License

このプロジェクトは MIT ライセンスの下で公開されています。詳細は [LICENSE](./LICENSE) ファイルをご覧ください。

ただし、このプロジェクトは Apache License 2.0 でライセンスされている Streamlit を使用しています。
Streamlit のライセンス全文は [こちら](https://github.com/streamlit/streamlit/blob/develop/LICENSE) でご確認いただけます。
