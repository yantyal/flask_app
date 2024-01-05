from .base import BaseLogic
from flask import current_app, render_template, redirect, request, current_app, session, url_for
from models.models import db, Post, PostUser
from sqlalchemy import text
import os
from werkzeug.utils import secure_filename
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class DashboardLogic(BaseLogic):

    def response(self, request, session):
        posts = self.get_posts()
        # ログを出力
        current_app.logger.info(f"posts: {posts}") 
        return render_template("dashboard.html", posts=posts)

    def get_posts(self):
        # データベースからデータを取得
        result = db.session.execute(text("""
            SELECT p.image_path, p.post, u.name 
            FROM POST p
            JOIN POST_USER pu ON p.post_id = pu.post_id
            JOIN user_info u ON pu.user_id = u.user_id
            ORDER BY p.updated_at DESC
        """))
        return [row for row in result]

    def create_post(self, request, session):
        # 投稿の処理
        if 'image' not in request.files:
            # ログを出力
            current_app.logger.info("画像がアップロードされていません。") 
            return "画像がアップロードされていません。"

        file = request.files['image']
        if file.filename == '':
            # ログを出力
            current_app.logger.info("画像がアップロードされていません。") 
            return"画像がアップロードされていません。"

        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

            # フォルダの存在を確認し、存在しない場合は作成する
            if not os.path.exists(current_app.config['UPLOAD_FOLDER']):
                # ログを出力
                current_app.logger.info(f"updoad_folder: {current_app.config['UPLOAD_FOLDER']}") 
                os.makedirs(current_app.config['UPLOAD_FOLDER'])
            file.save(upload_folder_path)
            filepath = os.path.join(current_app.config['FILE_PATH'], filename).replace('\\', '/')
            # ログを出力
            current_app.logger.info(f"file_path: {filepath}") 

            # Check if 'post' key exists in form
            post_content = request.form.get('post')
            if not post_content:
                # Handle error: post content not provided or empty
                # ログを出力
                current_app.logger.info(f"post_content: {post_content}") 
                return "投稿内容が空です。"

            # 1. POSTテーブルに新しい投稿データを登録
            now = datetime.now()
            # ログを出力
            current_app.logger.info(f"filepath: {filepath} post_content: {post_content} updated_at: {now}") 
            new_post = Post(image_path=filepath, post=post_content, updated_at=now)
            db.session.add(new_post)
            db.session.commit()

            # 2. POST_USERテーブルにデータを登録
            # Get the user ID from the session
            new_post_post_id = new_post.post_id
            user_id = session.get('user_id')
            # ログを出力
            current_app.logger.info(f"post_id: {new_post_post_id} user_id: {user_id}") 
            post_user_entry = PostUser(post_id=new_post_post_id, user_id=user_id)
            db.session.add(post_user_entry)
            db.session.commit()

            return "投稿が成功しました。"
    
        # ログを出力
        current_app.logger.info("投稿が失敗しました。") 
        return "投稿が失敗しました。"


    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS