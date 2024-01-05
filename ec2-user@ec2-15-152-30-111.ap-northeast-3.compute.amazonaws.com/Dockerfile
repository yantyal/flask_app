# ベースイメージを選択
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR .

# 依存パッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションを起動
CMD ["python", "app.py"]
