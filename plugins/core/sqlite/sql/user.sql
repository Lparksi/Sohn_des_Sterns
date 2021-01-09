create table user
(
    uid               integer default 1000
        constraint user_pk
            primary key autoincrement,
    qq                integer not null,
    nick_name         text,
    sign_time         real,
    money             integer default 1000,
    physical_strength integer default 100
);

