from dbworks import create_connection, execute_read_query

connection = create_connection("localhost", "root", "", "soc_media")

print(execute_read_query(connection, """SELECT users.handle, posts_history.post_id, posts_history.action  FROM posts_history
INNER JOIN users ON posts_history.user_id=users.id"""))