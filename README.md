# stpyapp-template
[streamlit](https://streamlit.io/)のアプリ開発するためのテンプレートを作ってみる

## コンテンツ
- サンプルコード（[streamlit-example](https://github.com/streamlit/streamlit-example)）を追加

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
PROJECT_FOLDER="stapp-excel2csv"
GITHUB_URL="https://github.com/sgtao/${PROJECT_FOLDER}.git"
git clone https://github.com/sgtao/stpyapp-template.git $PROJECT_FOLDER
cd  $PROJECT_FOLDER
# git remote add origin $GITHUB_URL
git remote set-url origin $GITHUB_URL
git branch -M main
git push -u origin main
```

### 02．`README.md`・`LICENSE`ファイルの変更
- `README.md`の変更：
  - タイトル、概要を変更する
  - LICENSEを変更する場合は、`README.md`の下段の表記と`LICENSE`ファイルを変更する

### 03．`src/pages`フォルダ配下にアプリケーション追加
- 例）`src/pages/11_csv_viewer.py`を作成
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
