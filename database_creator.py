"""
Данный файл-исполнитель предназначен для того, чтобы создать по шаблону базу данных,
которую придется в дальнейшем редактировать вручную.

Made by DK - aka- Tenchyga
"""

def create_dabase():
    import os, sqlite3

    file_location = sqlite3.connect(os.getcwd() + '\database.db')
    database = file_location.cursor()

    database.execute("""CREATE TABLE IF NOT EXISTS users (
        login TEXT,
        password TEXT,
        lfp TEXT,
        squad TEXT,
        role TEXT
    )""")

    if database.execute("SELECT * FROM users").fetchone() is None:
        database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                        ("DKonKI21", "135642", "Коновалов Данил", "КИ21-17/1Б", "student"))
        database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                        ("BykovKI21", "112233", "Владимир Быков", "ИК21-06/2Ф", "student"))
        database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                        ("BokalKI21", "111111", "Бокаленко Илья", "КИ21-17/1Б", "student"))
        database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                        ("Мужик", "Мужик", None, None, None))
        database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                        ("admin", "admin", "admin", "ADM/IN1", "teacher"))
        database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?)", 
                        ("admin2", "admin2", "admin2", "ADM/IN2", "teacher"))

    file_location.commit()
