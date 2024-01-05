from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='ユーザーID')
    name = db.Column(db.String(256), nullable=False, comment='ユーザー名')
    mail = db.Column(db.String(256), nullable=False, comment='メールアドレス')
    password = db.Column(db.String(256), nullable=False, comment='パスワード')

    posts = db.relationship('PostUser', back_populates='user')
    
    def __repr__(self):
        return f"<UserInfo(user_id={self.user_id}, name={self.name}, mail={self.mail})>"

class Post(db.Model):
    __tablename__ = 'POST'
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="投稿ID")
    image_path = db.Column(db.String(256), nullable=False, comment="画像パス")
    post = db.Column(db.String(500), nullable=False, comment="投稿")
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, comment="最終更新日時")

    post_users = db.relationship('PostUser', back_populates='related_post')

class PostUser(db.Model):
    __tablename__ = 'POST_USER'
    post_user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='投稿ユーザーID')
    post_id = db.Column(db.Integer, db.ForeignKey('POST.post_id'), nullable=False, comment='投稿ID')
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'), nullable=False, comment='ユーザーID')
    delete_flag = db.Column(db.String(1), default='0', nullable=False, comment='削除フラグ')

    user = db.relationship('UserInfo', back_populates='posts')
    related_post = db.relationship('Post', back_populates='post_users')

    def __repr__(self):
        return f"<PostUser(post_user_id={self.post_user_id}, post_id={self.post_id}, user_id={self.user_id})>"
