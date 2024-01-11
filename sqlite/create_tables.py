from dbworks import create_connection, execute_query

connection = create_connection("soc_media.db")
execute_query(connection, """CREATE TABLE IF NOT EXISTS posts(
	id integer auto_increment,
    title varchar(300),
    body text NOT NULL,
    user_id integer,
    status varchar(300),
    created_at timestamp,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id)
)""")
execute_query(connection, """CREATE TABLE IF NOT EXISTS users(
	id integer auto_increment,
    handle varchar(128),
    username varchar(128),
    role varchar(64),
    created_at timestamp,
    PRIMARY KEY (id)
)""")
execute_query(connection, """CREATE TABLE IF NOT EXISTS follows(
	following_user_id integer,
    followed_user_id integer,
    created_at timestamp,
    FOREIGN KEY (following_user_id) REFERENCES users(id),
    foreign key (followed_user_id) REFERENCES users(id)
)""")
execute_query(connection, """CREATE TABLE IF NOT EXISTS posts_history(
	id integer auto_increment,
    user_id integer,
    post_id integer,
    action varchar(64),
    made_at timestamp,
    PRIMARY KEY (id),
    foreign key (user_id) references users(id),
    foreign key (post_id) references posts(id)
)""")


