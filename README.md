# streamlit-docker-example

このリポジトリは、[Streamlit](https://github.com/streamlit/streamlit) アプリケーションをDocker環境で開発・運用するためのサンプルです。

<p align="center">
<img src="/img/screenshot.png" alt="streamlit in docker">
</p>

## セットアップ手順

1. リポジトリをクローンします。

```bash
git clone <このリポジトリのURL>
cd <クローンしたディレクトリ>
```

2. 必要に応じて `config/st_users.csv` を編集し、ユーザー情報を追加します。

3. ユーザー情報をもとにパスワードをハッシュ化し、設定ファイルを生成します。

```bash
python src/create_yml.py
```

4. Dockerコンテナをビルド・起動します。

```bash
docker-compose up -d --build
```

5. ブラウザで [localhost:8501](http://localhost:8501) または [localhost:5000](http://localhost:5000) にアクセスしてアプリを利用できます。

6. アプリの停止:

```bash
docker-compose stop
```

7. アプリとイメージの完全削除:

```bash
docker-compose down --rmi all
```

## 構成ファイル

- `config/st_users.csv`: ユーザー情報（id, name, password, email）を記載
- `config/st_config.yml`: Streamlit Authenticator用の設定ファイル（`create_yml.py`で自動生成）
- `.env`: 環境変数ファイル。ポート番号やAPIキーなど、Dockerやアプリで利用する設定値を記載します。
    - 例: `STREAMLIT_PORT=8501` など

## 補足

- ユーザー追加・パスワード変更時は再度 `python src/create_yml.py` を実行してください。
- その他の設定やカスタマイズは `src/` 配下のPythonファイルを編集してください。