# config.py

import socket

# MySQLコンテナのIPアドレスを取得
# mysql_container_ip = socket.gethostbyname('mysql-container')
mysql_container_ip = "falsk_app-db-1" 

# DB接続情報
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://user21:user21(PASS)@{mysql_container_ip}/flask_app'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'flask_app_113333555555'
UPLOAD_FOLDER = 'static/img'
FILE_PATH = 'img'