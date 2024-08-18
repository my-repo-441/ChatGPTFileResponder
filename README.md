# ChatGPTFileResponder

# プロジェクト概要

ChatGPTFileResponderは、指定したディレクトリ内のファイルを検索し、ユーザーからの質問を返答するPythonベースのアプリケーションです。結果はデータベースにキャッシュされ、後で再利用することができます。

# フォルダ構成
.
├── README.md
├── .env                    # 環境変数の設定ファイル
├── data                    # データ用ディレクトリ
│   ├── input               # 入力ファイルが保存されるディレクトリ
│   └── output              # 出力ファイルが保存されるディレクトリ
├── logs                    # ログファイル保存用ディレクトリ
│   └── app.log             # ログファイル
├── requirements.txt        # 必要なPythonパッケージ一覧
├── src                     # ソースコードディレクトリ
│   ├── chatgpt_api.py      # ChatGPT APIにテキストを送信し要約を生成するモジュール
│   ├── database.py         # データベース関連の処理を行うモジュール
│   ├── file_reader.py      # ファイルの読み取りを行うモジュール
│   ├── file_search.py      # ファイル検索を行うモジュール
│   ├── main.py             # メインの実行スクリプト
└── tests                   # テストコード用ディレクトリ
    ├── test_file_reader.py # file_reader.pyのテスト
    ├── test_file_search.py # file_search.pyのテスト
    └── test_main.py        # main.pyのテスト

# 主要ファイルの説明
## main.py
アプリケーションのエントリーポイントです。ファイルパスと質問を入力し、該当ファイルの要約を生成します。

## database.py
SQLiteデータベースを使用して、ファイルの内容をキャッシュするモジュールです。キャッシュされた内容を再利用することで、効率的な処理が可能になります。

## file_search.py
指定したディレクトリ内のファイルを検索し、条件に合うファイルリストを生成します。

## file_reader.py
ファイルを読み取り、その内容を返すモジュールです。テキストファイルとPDFファイルに対応しています。

## chatgpt_api.py
ChatGPT APIを使用して、ファイルの内容に基づいた要約を生成するモジュールです。

# 仮想環境の作成＆アクティベート
以下の手順に従って、仮想環境を作成します。

## 仮想環境の作成
python -m venv path/to/your/venv
(例：python -m venv python-test)

## 仮想環境のアクティベート
source path/to/your/venv/bin/activate
（例：source ~/venv/python-test/bin/activate）

# 実行手順
以下の手順に従って、アプリケーションを実行し、PDFファイルの要約を取得することができます。

## ターミナルを開き、プロジェクトのルートディレクトリに移動します。
cd /path/to/ChatGPTFileResponder

## main.py を実行します。
python ./src/main.py
実行後、ターミナルに以下のようなプロンプトが表示されます。

ファイル名：
読み込み対象のPDFファイルのパスを入力します。
例：ChatGPTFileResponder/data/input/20230822_Report_J.pdf
次に、要約してほしい内容に関する質問を入力します。
例：質問：記事を要約して

入力が完了すると、ChatGPT APIを使用して指定されたPDFファイルの要約が生成され、ターミナルに表示されます。