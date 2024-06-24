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
task format
task lint
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


## License
Apache-2.0 license

