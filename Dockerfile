# ベースイメージを選択
FROM python:3.8

# 作業ディレクトリを設定
WORKDIR /app

# 依存パッケージをインストール
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションを起動
CMD ["python", "app.py"]
