import sqlite3
CONN = sqlite3.connect('blog.db')
CURSOR = CONN.cursor()


class Database:
    def create_tables(self):
        sql1 = """
        CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY, 
        name varchar(40),
        email varchar(40),
        age INTEGER)"""
        CURSOR.execute(sql1)

        sql2 = """CREATE TABLE IF NOT EXISTS posts(
        id INTEGER PRIMARY KEY, 
        title varchar(40), 
        content TEXT, 
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id))"""
        CURSOR.execute(sql2)

        sql3 = """CREATE TABLE IF NOT EXISTS comments(
        id INTEGER PRIMARY KEY,
        comment TEXT,
        post_id INTEGER,
        user_id INTEGER,

        FOREIGN KEY(post_id) REFERENCES posts(id),
        FOREIGN KEY(user_id) REFERENCES users(id))"""
        CURSOR.execute(sql3)


        CONN.commit()


    def drop_tables(self):
        sql = """DROP TABLE IF EXISTS users"""
        CURSOR.execute(sql)

        sql = """DROP TABLE IF EXISTS posts"""
        CURSOR.execute(sql)

        sql = """DROP TABLE IF EXISTS comments"""
        CURSOR.execute(sql)

        CONN.commit()


# db = Database()

# db.drop_tables()
# print("***********Dropped Tables*****************")

# print("***********Creating Tables-------->")
# db.create_tables()
# print("***********3 Tables Created*****************")
