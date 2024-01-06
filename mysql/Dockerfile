# MySQLの公式イメージをベースにする
FROM mysql:8.0-debian

# パッケージリストを更新し、必要なパッケージをインストール
RUN apt-get update && apt-get install -y locales gnupg \
    # ja_JP.UTF-8ロケールを生成
    && echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen ja_JP.UTF-8

# GPGキーの取得
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5072E1F5

# 環境変数を設定
ENV LC_ALL ja_JP.UTF-8
ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8

CMD ["mysqld"]