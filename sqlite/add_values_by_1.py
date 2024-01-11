from dbworks import create_connection, execute_query

connection = create_connection("soc_media.db")
execute_query(connection, """INSERT INTO users(id, handle, username, role)
VALUES
(5, 'purple', 'Purple', 'user');""")
execute_query(connection, """INSERT INTO posts(title, body, user_id, status)
VALUES
('ay', 'ayyyyy', 5, 'open'),
("Don't use platform as means of reporting problems", "There's email for it.", 2048, 'open');""")
execute_query(connection, """INSERT INTO posts_history(user_id, post_id, action)
VALUES
(5, 1, 'like');""")
execute_query(connection, """INSERT INTO follows(following_user_id, followed_user_id)
VALUES
(5, 2048);""")