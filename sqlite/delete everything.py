from dbworks import create_connection, execute_query

connection = create_connection("soc_media.db")

execute_query(connection, """DELETE FROM follows""")