from dbworks import create_connection, execute_query

connection = create_connection("localhost", "root", "", "soc_media")
query = """INSERT INTO users(handle, username, role)
VALUES
('red', 'Red', 'user'),
('blue', 'Blue', 'user'),
('yellow', 'Yellow', 'user'),
('green', 'Green', 'user');
INSERT INTO users(id, handle, username, role)
VALUES
(2048, 'admin', 'Admin', 'admin');
INSERT INTO posts(title, body, user_id, status)
VALUES
('beta start', 'This social network is in closed beta!', 2048, 'open'),
('test', 'test', 1,'open'),
("Handles aren't working", 2, "Can't mention anyone", 'open'),
('Has anyone heard from Green?', "He isn't answering my calls", 3, 'open'),
("I'm here", "My internet provider had some problems, couldn't join here in time", 4, 'open');
INSERT INTO posts_history(user_id, post_id, action)
VALUES
(1, 1, 'like'),
(2, 1, 'like'),
(3, 1, 'like'),
(4, 1, 'like'),
(2048, 1, 'like');
INSERT INTO follows(following_user_id, followed_user_id)
VALUES
(1, 2048),
(2, 2048),
(3, 2048),
(4, 2048),
(1, 2),
(2, 1);"""
execute_query(connection, query)
