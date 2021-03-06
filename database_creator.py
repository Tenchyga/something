"""
Данный файл-исполнитель предназначен для того, чтобы создать по шаблону базу данных,
которую придется в дальнейшем редактировать вручную.

Made by DK - aka- Tenchyga
"""

from random import randint
from tkinter.messagebox import NO


def create_dabase():
    import os, sqlite3

    file_location = sqlite3.connect(os.getcwd() + '\database.db')
    database = file_location.cursor()

    # - - - СОЗДАНИЕ ТАБЛИЦИ ПОЛЬЗОВАТЕЛЕЙ - - -
    database.execute("""CREATE TABLE IF NOT EXISTS users (
        user_ID INT,
        login TEXT,
        password TEXT,
        lfp TEXT,
        role TEXT,
        group_ID INT,
        lessons TEXT
    )""")

    alphabet = "ABCDEFGHIJKMNOLPQUSTWXYZ"

    last_names = "Konovalov_Ivanov_Barsukov_Kirillov_Administrov_Kentov_Pushapov".split("_")
    passwords = "112233,234561,113141,22545,141516,213456,654321,1111111".split(",")

    roles = ["student", "teacher"]
    group_IDS = [21171, 21062, 2116]

    if database.execute("SELECT * FROM users").fetchone() is None:
        for i in range(50):

            # Счетчик преподавателей.
            teacher_counter = len(database.execute("SELECT user_ID FROM users WHERE role = ?", ("teacher", )).fetchall())

            # Если преподавателей больше 4, то создаются только студенты, иначе случайный выбор роли.
            if teacher_counter < 4:
                role = roles[randint(0, 1)]
            else:
                role = roles[0]

            # ГЕнерация разных данных для заполнения БД.
            login = alphabet[randint(0, len(alphabet)-1)] + last_names[randint(0, len(last_names) - 1)] + "-KI21"
            password = passwords[randint(0, len(passwords) - 1)]

            lfps = "Коновалов,Степанов,Бокаленко,Винокуров,Ершов,Болотников,Петров".split(",")[randint(0, 6)]
            name = lfps + " " + "Данил,Илья,Артем,Олег,Степан".split(",")[randint(0, 4)] + " Михалыч"

            if role == "teacher":
                group = None
                lessons = ["0-1", "0", "2", "0-2", "1"][randint(0,4)]
            else:
                group = group_IDS[randint(0, 2)]
                lessons = None

            database.execute(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (i, login, password, name, role, group, lessons))

    # - - - - СОЗДАНИЕ ТАБЛИЦ ДЛЯ ПРЕПОДАВАТЕЛЕЙ, ВКЛЮЧАЯ СВЯЗЬ ПРЕДМЕТОВ И ПОЛЬЗОВАТЕЛЕЙ-ПРЕПОДАВАТЕЛЕЙ - - - -
    database.execute("""CREATE TABLE IF NOT EXISTS lessons (
        lesson_ID INTEGER,
        lesson_name TEXT
    )""")

    lessons_names = "Основы программирования_Введение в проф. Деятельность_Алгоритмы".split("_")

    if database.execute("SELECT * FROM lessons").fetchone() is None:
        for i in range(3):
            database.execute(f"INSERT INTO lessons VALUES (?, ?)",
                            (i, lessons_names[i]))

    database.execute("""CREATE TABLE IF NOT EXISTS teacher_lessons (
        user_ID INTEGER,
        lesson_ID INTEGER
    )""")

    if database.execute("SELECT * FROM teacher_lessons").fetchone() is None:

        # Счетчик преподователей.
        teacher_counter = database.execute("SELECT user_ID, lessons FROM users WHERE role = ?", ("teacher", )).fetchall()

        for user_ID, lessons in teacher_counter:
            for lesson in lessons.split("-"):

                database.execute(f"INSERT INTO teacher_lessons VALUES (?, ?)",
                                (user_ID, lesson))

    # - - - - СОЗДАНИЕ ТАБЛИЦА ДЛЯ СТУДЕНТОВ, ВКЛЮЧАЯ СОДЕРЖАНИЕ ГРУПП - - - -

    database.execute("""CREATE TABLE IF NOT EXISTS groups(
        group_ID INT,
        group_name TEXT
    )""")

    groups_IDS = [21171, 21062, 2116]
    groups_names = "КИ21-17/1Б КИ21-17/2Б КИ21-06/2Ф".split(" ")

    if database.execute("SELECT * FROM groups").fetchone() is None:
        for i in range(3):
            database.execute(f"INSERT INTO groups VALUES (?, ?)",
                            (groups_IDS[i], groups_names[i]))

    database.execute("""CREATE TABLE IF NOT EXISTS students_groups(
        user_ID INT,
        group_ID INT
    )""")

    student_list = database.execute("SELECT user_ID, group_ID FROM users WHERE role = ?", ("student", )).fetchall()

    if database.execute("SELECT * FROM students_groups").fetchone() is None:
        for i in student_list:
            database.execute(f"INSERT INTO students_groups VALUES (?, ?)", i)

    # - - - - ТАБЛИЦА С РАБОТАМИ - - - - -

    database.execute("""CREATE TABLE IF NOT EXISTS tasks(
        work_ID INT,
        work_name TEXT,
        discription TEXT,
        lessons_key INT
    )""")

    work_names = "СТО.Знакомство._СТО. Аналаиз_Практическая 1. Алгоритмы_Практическая 2. Вывод числовой прогрессии.".split("_")
    works_disc = ["Необходимо ознакомиться с СТО.",
                "Анализировать пример СТО и найти ошибки.",
                "Нунжно создать алгоритм строго вашего варианта.",
                "Создать программу для вычисления заданной числовой прогрессии."]
    works_lessons_key = [1, 1, 0, 0]

    if database.execute("SELECT * FROM tasks").fetchone() is None:
        for i in range(4):
            database.execute("INSERT INTO tasks VALUES (?, ?, ?, ?)",
                            (i, work_names[i], works_disc[i], works_lessons_key[i]))

    # - - - - СОЗДАНИЕ ТАБЛИЦЫ ДЛЯ СВЯЗИ ПРЕДМЕТОВ И ГРУПП - - - -

    database.execute("""CREATE TABLE IF NOT EXISTS group_lessons(
        group_ID INT,
        lesson_ID INT
    )""")

    if database.execute("SELECT * FROM group_lessons").fetchone() is None:
        for group_ID in group_IDS:
            lessons = ["0-1", "0", "2", "0-2", "1"][randint(0,4)]

            for lesson in lessons.split("-"):
                database.execute("INSERT INTO group_lessons VALUES (?, ?)",
                                (group_ID, int(lesson)))

    database.execute(
        """CREATE TABLE IF NOT EXISTS student_tasks (
            task_ID INT,
            student_ID INT,
            file BLOB,
            comment TEXT,
            grade INT
        )""")

    if database.execute("SELECT * FROM student_tasks").fetchone() is None:
        for student_ID, group_ID in database.execute("SELECT user_ID, group_ID FROM users WHERE role = ?", ("student", )).fetchall():

            lessons = list()
            for lesson in database.execute("SELECT lesson_ID FROM group_lessons WHERE group_ID = ?", (group_ID, )).fetchall():
                lessons.append(lesson[0])

            for lesson in lessons:

                for work_ID in database.execute("SELECT work_ID FROM tasks WHERE lessons_key = ?", (lesson, )).fetchall():
                    database.execute(
                        "INSERT INTO student_tasks VALUES (?, ?, ?, ?, ?)", 
                        (work_ID[0], student_ID, None, None, None)
                    )

    file_location.commit()
