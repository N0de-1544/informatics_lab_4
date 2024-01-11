from dbworks import create_connection, execute_read_query

connection = create_connection("localhost", "root", "", "soc_media")


print(execute_read_query(connection, """SELECT user_id FROM posts
UNION
SELECT user_id FROM posts_history"""))
print(execute_read_query(connection, """SELECT following_user_id FROM follows
UNION
SELECT followed_user_id FROM follows"""))