import mysql.connector
from dbworks import create_connection, execute_read_query

connection = create_connection("soc_media.db")
query = """SELECT * FROM users"""
print(execute_read_query(connection, query))
