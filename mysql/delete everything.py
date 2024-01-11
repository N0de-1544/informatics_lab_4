from dbworks import create_connection, execute_query

connection = create_connection("localhost", "root", "", "soc_media")

execute_query(connection, """DELETE FROM follows""")