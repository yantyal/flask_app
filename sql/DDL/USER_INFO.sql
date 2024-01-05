create table user_info (
  user_id INT not null auto_increment comment 'ユーザーID'
  , name VARCHAR(256) not null comment 'ユーザー名'
  , mail VARCHAR(256) not null comment 'メールアドレス'
  , password VARCHAR(256) not null comment 'パスワード'
  , constraint user_info_PKC primary key (user_id)
) CHARACTER SET utf8mb4 comment 'ユーザー情報' ;
