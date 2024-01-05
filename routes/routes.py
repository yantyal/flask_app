from flask import Blueprint, current_app, render_template, request, redirect, url_for, session, jsonify  # jsonifyをインポート
from flask import request
from logic.login import LoginLogic
from logic.dashboard import DashboardLogic
from logic.validator import Validator
from datetime import datetime

main = Blueprint('main', __name__)

# リクエスト前の共通処理
@main.before_request
def log_request_info():
    # ルートごとにログを出力
    current_app.logger.info(f"Request received at {datetime.now()} for {request.endpoint}")

@main.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@main.route('/logout')
def logout():
    # ログを出力
    current_app.logger.info(f"User ID: {session.get('user_id')} のユーザーのセッションをクリアします")
    session.clear()  # セッションをクリア
    # JSONレスポンスを返す
    return jsonify({"success": True, "message": "Logged out successfully"})

@main.route('/login_logic', methods=['POST'])
def login_logic():

    # ログを出力
    current_app.logger.info(f"Login request received at {datetime.now()}")
    login_logic_instance = LoginLogic()
    return login_logic_instance.response(request, session)

@main.route('/dashboard', endpoint='dashboard')
def dashboard():
    # ログインしているかチェック
    Validator.redirect(session)

    dashboard_logic_instance = DashboardLogic()
    return dashboard_logic_instance.response(request, session)

@main.route('/create-post', methods=['GET', 'POST'])
def create_post():

    # ログインしているかチェック
    Validator.redirect(session)
    
    dashboard_logic_instance = DashboardLogic()
    if request.method == 'POST':
        dashboard_logic_instance.create_post(request, session)

    return dashboard_logic_instance.response(request, session)

@main.errorhandler(Exception)
def handle_all_errors(error):
    session.clear()
    # エラー情報をログに出力
    current_app.logger.error(f"An error occurred: {error}")
    # エラーダイアログを表示するHTMLをレンダリング
    return render_template('error_dialog.html', error_message=str(error))








