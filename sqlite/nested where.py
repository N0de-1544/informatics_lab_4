from dbworks import create_connection, execute_read_query

connection = create_connection("soc_media.db")

print(execute_read_query(connection, """SELECT handle, username FROM users
WHERE users.id in (SELECT user_id FROM posts_history WHERE action='like')"""))
print(execute_read_query(connection, """SELECT * FROM posts
WHERE posts.id in (SELECT post_id from posts_history)"""))