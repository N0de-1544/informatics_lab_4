from dbworks import create_connection, execute_query

connection = create_connection("localhost", "root", "", "soc_media")

execute_query(connection, """DELETE FROM users WHERE id=6""")
execute_query(connection, """DELETE FROM posts WHERE id=2""")
execute_query(connection, """DELETE FROM posts_history WHERE id=6""")
execute_query(connection, """DELETE FROM follows WHERE following_user_id=4""")