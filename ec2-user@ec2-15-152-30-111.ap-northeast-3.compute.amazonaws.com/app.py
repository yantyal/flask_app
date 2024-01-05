import logging
from flask import Flask
from flask_bcrypt import Bcrypt
from models.models import db
import config
from routes.routes import main
from waitress import serve  # Waitressをインポート

bcrypt = Bcrypt()

def create_app():
    """
    アプリケーションの初期化を行い、アプリケーションのインスタンスを返す。

    Returns:
        Flask: Flaskアプリケーションのインスタンス
    """
    
    app = Flask(__name__)  # Flaskアプリケーションのインスタンス生成
    app.config.from_object(config)  # 設定の読み込み

    initialize_extensions(app)  # 拡張機能の初期化
    register_blueprints(app)    # Blueprintの登録
    configure_logging(app)      # ロギングの設定

    return app

def initialize_extensions(app):
    """
    Flaskアプリケーションに拡張機能を初期化・関連付ける。

    Args:
        app (Flask): Flaskアプリケーションのインスタンス
    """
    
    # Bcryptの初期化
    bcrypt.init_app(app)

    # データベースの初期化・Flaskアプリケーションとの関連付け
    db.init_app(app)

def register_blueprints(app):
    """
    FlaskアプリケーションにBlueprintを登録する。

    Args:
        app (Flask): Flaskアプリケーションのインスタンス
    """
    
    # Blueprintの登録
    app.register_blueprint(main)

def configure_logging(app):
    """
    Flaskアプリケーションのロギング設定を行う。

    Args:
        app (Flask): Flaskアプリケーションのインスタンス
    """
    
    # デバッグモードに応じてログレベルを設定
    if app.debug:
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)

    # ログ出力先ファイルのハンドラを設定
    handler = logging.FileHandler('flask_app.log', encoding='utf-8')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    # ハンドラをアプリケーションのロガーに追加
    app.logger.addHandler(handler)

if __name__ == '__main__':
    app = create_app()  # Flaskアプリケーションを生成
    # Waitressを使用してFlaskアプリケーションを起動
    serve(app, host='0.0.0.0', port=5000)



"""
set FLASK_ENV=development
set FLASK_APP=app.py
flask run
"""

# １，ログを出す
# ２，エラーハンドリング
# ３，トランザクション管理
# ４，フォームの再送をさせないPRGパターン