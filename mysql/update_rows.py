from dbworks import create_connection, execute_query

connection = create_connection("localhost", "root", "", "soc_media")

execute_query(connection, """UPDATE users SET username='Violet' WHERE handle='purple' """)
execute_query(connection, """UPDATE users SET handle='lime' WHERE username='Green' """)
execute_query(connection, """UPDATE follows SET followed_user_id='3' WHERE following_user_id='1'""")
execute_query(connection, """UPDATE follows SET followed_user_id='3' WHERE following_user_id='2'""")