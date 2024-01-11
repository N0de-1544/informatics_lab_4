from dbworks import create_connection, execute_read_query

connection = create_connection("soc_media.db")


print(execute_read_query(connection, """SELECT count(id), role FROM users
WHERE role LIKE "%user"
GROUP BY role"""))