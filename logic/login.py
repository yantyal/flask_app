from .base import BaseLogic
from flask import current_app, render_template, redirect, url_for
from models.models import UserInfo

class LoginLogic(BaseLogic):

    def response(self, request, session):
        email = request.form['email']
        password = request.form['password']
        # ログを出力
        current_app.logger.info(f"email: {email}  password: {password} ") 

        user = UserInfo.query.filter_by(mail=email).first()
        if self.getUser(email, password):  # パスワードの検証関数
            session['logged_in'] = True
            session['user_email'] = email
            session['user_id'] = user.user_id  # ユーザーIDをセッションに保存
            # ログを出力
            current_app.logger.info(f"ユーザーが見つかりました。UserId: {user.user_id}") 
            return redirect(url_for('main.dashboard'))
        else:
            # ログを出力
            current_app.logger.info(f"ユーザーが見つかりません。") 
            return render_template('login.html', show_error_modal=True)

    @staticmethod
    def getUser(email, password):
        """
        Fetches the user from the UserInfo table using the provided email and password.

        Parameters:
        - email (str): The email of the user.
        - password (str): The provided plaintext password to be verified.

        Returns:
        - UserInfo: The user object if credentials match, None otherwise.
        """
        user = UserInfo.query.filter_by(mail=email).first()

        from app import bcrypt
        # If the user exists and the hashed password matches the given password
        if user and bcrypt.check_password_hash(user.password, password):
            return user

        return None
    

    def hash_password(password):
        """パスワードをハッシュ化する関数"""
        from app import bcrypt
        return bcrypt.generate_password_hash(password).decode('utf-8')

    # # テスト用のパスワード
    # password = "password123"
    # hashed_pw = hash_password(password)

    # print(f"Original Password: {password}")
    # print(f"Hashed Password: {hashed_pw}")