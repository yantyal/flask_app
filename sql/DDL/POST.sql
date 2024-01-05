create table POST (
  post_id INT not null AUTO_INCREMENT comment '投稿ID'
  , image_path VARCHAR(256) comment '画像パス'
  , post TEXT not null comment '投稿'
  , updated_at DATETIME not null comment '最終更新日時'
  , constraint POST_PKC primary key (post_id)
) CHARACTER SET utf8mb4;
