import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT
)
""")

conn.commit()

def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )
    conn.commit()
    print("Registration Successful")

def login():
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    if cursor.fetchone():
        print("Login Successful")
    else:
        print("Invalid Username or Password")

while True:
    print("\n1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")

conn.close()
