import sqlite3

connection = sqlite3.connect("products.db")
cursor = connection.cursor()

connection2 = sqlite3.connect("users.db")
cursor2 = connection2.cursor()

def initiate_db():
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS Products(
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            )
        """
    )
    connection.commit()
    cursor2.execute(
        """
            CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL
            )
        """
    )
    connection2.commit()


def add_product(title, description, price):
    cursor.execute(
        """
            INSERT INTO Products (title, description, price) 
            VALUES(?, ?, ?)
        """,
        (title, description, price),
    )
    connection.commit()


def get_all_products():
    cursor.execute("SELECT * FROM Products")
    data = cursor.fetchall()
    # connection.close()
    return data


def add_user(username, email, age):
    cursor2.execute(
        """
            INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)               
        """,
        (username, email, age, 1000)
    )
    connection2.commit()


def is_included(username):
    user = cursor2.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
    if user:
        return True
    return False


# def is_included(username):
#     return (
#         cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchone()
#         is not None
#     )


# initiate_db()
#
# add_product("Пингвин", "С ребрышками", 150)
# add_product("Пингвин", "Зелёный", 120)
# add_product("Пингвин", "Чёрный", 100)
# add_product("Пингвин", "Dart Penguin", 200)
#
# for prod in get_all_products():
#     print(prod)
connection.commit()
connection2.commit()
if __name__ == '__main__':
    # connection.commit()
    connection.close()
    connection2.close()
