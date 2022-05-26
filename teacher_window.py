from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QComboBox, QFrame, QTextBrowser, QTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QRect

import sqlite3, os
from .function import sorter

class Teacher_Window():
    def __init__(self, user):
        self.user = user

        super().__init__()

    # - - - - СТАТУС ОКНА ДЛЯ ОТСЛЕЖИВАНИЯ - - - 

        self.window_status = "main"

    # - - - - - - - - - - - - - - - - - - - - - - 

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

    # - - - СБОР ДАННЫХ - - - |

        username = database.execute(f"SELECT lfp FROM users WHERE user_ID = ?", (self.user, )).fetchone()[0].split(" ")[1]

        lessons = database.execute(f"SELECT lessons FROM users WHERE user_ID = ?", (self.user, )).fetchone()

    # - - - - - - - - - - - - |

# Создание основого рабочего пространства
        self.main_window = QMainWindow()

        for _ in range(1):
            import ctypes

            myappid = 'mycompany.myproduct.subproduct.version'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.main_window.setWindowIcon(QIcon('eProverka_icon.png'))

        self.main_window.setWindowFlags(
            Qt.CustomizeWindowHint |
            Qt.Window   |
            Qt.WindowStaysOnTopHint
        )

        self.main_window.setStyleSheet("background-color: white;")
        self.main_window.setWindowTitle("еПроверка")
        self.main_window.setFixedSize(1466, 870)
        self.main_window.show()


# Добавление виджета, с помощью которого можно будет легально сделать полоски
        self.centralwidget = QWidget(self.main_window)


# Добавление линий
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(350, 10, 20, 831))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.VLine)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QRect(260, 130, 81, 16))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setFrameShape(QFrame.HLine)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setGeometry(QRect(10, 130, 81, 20))
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.line_right_all_stat = QFrame(self.centralwidget)
        self.line_right_all_stat.setGeometry(QRect(1010, 130, 441, 16))
        self.line_right_all_stat.setFrameShadow(QFrame.Plain)
        self.line_right_all_stat.setFrameShape(QFrame.HLine)

        self.line_left_all_stat = QFrame(self.centralwidget)
        self.line_left_all_stat.setGeometry(QRect(380, 130, 451, 16))
        self.line_left_all_stat.setFrameShadow(QFrame.Plain)
        self.line_left_all_stat.setFrameShape(QFrame.HLine)

        self.line_right_hint = QFrame(self.centralwidget)
        self.line_right_hint.setGeometry(QRect(1000, 600, 451, 20))
        self.line_right_hint.setFrameShadow(QFrame.Plain)
        self.line_right_hint.setFrameShape(QFrame.HLine)

        self.line_left_hint = QFrame(self.centralwidget)
        self.line_left_hint.setGeometry(QRect(380, 600, 471, 16))
        self.line_left_hint.setFrameShadow(QFrame.Plain)
        self.line_left_hint.setFrameShape(QFrame.HLine)


# Добавление надписей
        self.manage = QLabel(self.centralwidget)
        self.manage.setText("Управление")
        self.manage.setGeometry(QRect(120, 120, 111, 41))
        self.manage.setFont(QFont('Corbel Light', 16))

        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QRect(590, 30, 671, 81))
        self.label_welcome.setText(f"Добро пожаловать, {username}!")
        self.label_welcome.setFont(QFont('Corbel Light', 30))
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.label_all_stat = QLabel(self.centralwidget)
        self.label_all_stat.setText("Общая статистика")
        self.label_all_stat.setGeometry(QRect(840, 120, 161, 31))
        self.label_all_stat.setFont(QFont('Corbel Light', 16))
        self.label_all_stat.setAlignment(Qt.AlignCenter)

        self.label_all_works = QLabel(self.centralwidget)
        self.label_all_works.setText("Всего загруженных работ: ??")
        self.label_all_works.setGeometry(QRect(740, 200, 351, 41))
        self.label_all_works.setFont(QFont('Corbel Light', 22))
        self.label_all_works.setAlignment(Qt.AlignCenter)

        self.label_all_works_checked = QLabel(self.centralwidget)
        self.label_all_works_checked.setText("Всего работ зачтено: ??")
        self.label_all_works_checked.setGeometry(QRect(740, 240, 351, 41))
        self.label_all_works_checked.setFont(QFont('Corbel Light', 22))
        self.label_all_works_checked.setAlignment(Qt.AlignCenter)

        self.label_hints = QLabel(self.centralwidget)
        self.label_hints.setText("Справочник")
        self.label_hints.setGeometry(QRect(870, 590, 111, 31))
        self.label_hints.setFont(QFont('Corbel Light', 16))

        self.label_hint_1 = QLabel(self.centralwidget)
        self.label_hint_1.setGeometry(QRect(380, 640, 751, 41))
        self.label_hint_1.setFont(QFont('Corbel Light', 16))
        self.label_hint_1.setText(
            "Список студентов - отображает сколько"
            " человек в каждой группе сдал работ."
        )

        self.label_hint_2 = QLabel(self.centralwidget)
        self.label_hint_2.setGeometry(QRect(380, 690, 841, 41))
        self.label_hint_2.setFont(QFont('Corbel Light', 16))
        self.label_hint_2.setText(
            "Просмотр заданий курса - дает возможность просмотреть"
            " задания или изменить их описание."
        )

        self.label_hint_3 = QLabel(self.centralwidget)
        self.label_hint_3.setGeometry(QRect(380, 740, 841, 41))
        self.label_hint_3.setFont(QFont('Corbel Light', 16))
        self.label_hint_3.setText(
            "Проверка работ - проверка сданных работ"
            " и дальнейшее их возможное зачтение."
        )


    # - / - / - / НАДПИСИ ДЛЯ ЛИСТА СТУДЕНТОВ - / - / - / - /

        self.label_lesson = QLabel(self.main_window)
        self.label_lesson.setGeometry(QRect(530, 170, 91, 31))
        self.label_lesson.setFont(QFont('Corbel Light', 16))
        self.label_lesson.setText("Предмет:")

        self.label_group = QLabel(self.main_window)
        self.label_group.setGeometry(QRect(950, 170, 161, 31))
        self.label_group.setFont(QFont('Corbel Light', 16))
        self.label_group.setText("Группа:")

    #  - / - / - / - / - / - / - / - / - / - / - / - / - / - /


    # - / - / - / НАДПИСИ ДЛЯ СМЕНЫ ЗАДАНИЙ В РОЛИ ПРЕПОДАВАТЕЛЯ - / - / - / - /

        self.label_task_lesson = QLabel(self.main_window)
        self.label_task_lesson.setGeometry(QRect(520, 180, 91, 31))
        self.label_task_lesson.setFont(QFont('Corbel Light', 16))
        self.label_task_lesson.setText("Предмет:")

        self.label_task = QLabel(self.main_window)
        self.label_task.setGeometry(QRect(950, 180, 91, 31))
        self.label_task.setFont(QFont('Corbel Light', 16))
        self.label_task.setText("Задание:")

        self.label_discription = QLabel(self.main_window)
        self.label_discription.setGeometry(QRect(840, 230, 171, 31))
        self.label_discription.setFont(QFont('Corbel Light', 16))
        self.label_discription.setText("Описание задания")

    # ------------------ ДЛЯ ДОБАВЛЕНИЯ НОВОГО ЗАДАНИЯ -----------------------

        self.label_add_to_lesson = QLabel(self.main_window)
        self.label_add_to_lesson.setGeometry(QRect(710, 180, 91, 31))
        self.label_add_to_lesson.setText("Предмет:")
        self.label_add_to_lesson.setFont(QFont('Corbel Light', 16))

        self.label_add_new_task = QLabel(self.main_window)
        self.label_add_new_task.setGeometry(QRect(410, 240, 171, 31))
        self.label_add_new_task.setText("Название задания:")
        self.label_add_new_task.setFont(QFont('Corbel Light', 16))

        self.label_add_descr = QLabel(self.main_window)
        self.label_add_descr.setGeometry(QRect(410, 300, 181, 31))
        self.label_add_descr.setText("Описание задания:")
        self.label_add_descr.setFont(QFont('Corbel Light', 16))

    # - / - / - / - /- / - /- /- / -/ -/ - /- /- /- /- /- /- /- /- /- /- /- /-


# Добавление кнопок
        """Кнопка еПроверка (главная рабочая область)"""
        self.menu_button = QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QRect(20, 30, 311, 81))
        self.menu_button.setText("еПроверка")
        self.menu_button.setFont(QFont('Corbel Light', 44))
        self.menu_button.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        self.menu_button.clicked.connect(self.main_lobby)


        """Кнопка для перехда на вкладку добавления нового таска"""
        self.button_add_task = QPushButton(self.centralwidget)
        self.button_add_task.setGeometry(QRect(20, 500, 311, 81))
        self.button_add_task.setText("Добавить новое задание")
        self.button_add_task.setFont(QFont('Corbel Light', 16))
        self.button_add_task.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_add_task.clicked.connect(self.add_new_task)

        """Кнокпка 'Список студентов'"""
        self.button_list_o_students = QPushButton(self.centralwidget)
        self.button_list_o_students.setGeometry(QRect(20, 170, 311, 81))
        self.button_list_o_students.setText("Список студентов")
        self.button_list_o_students.setFont(QFont('Corbel Light', 16))
        self.button_list_o_students.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_list_o_students.clicked.connect(self.list_of_students)


        """Кнопка Просмотр заданий курса"""
        self.button_view_tasks = QPushButton(self.centralwidget)
        self.button_view_tasks.setGeometry(QRect(20, 280, 311, 81))
        self.button_view_tasks.setText("Просмотр заданий курса")
        self.button_view_tasks.setFont(QFont('Corbel Light', 16))
        self.button_view_tasks.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_view_tasks.clicked.connect(self.view_tasks)


        """Кнопка Просмотр сданных работ"""
        self.button_view_works = QPushButton(self.centralwidget)
        self.button_view_works.setGeometry(QRect(20, 390, 311, 81))
        self.button_view_works.setText("Просмотр сданных работ")
        self.button_view_works.setFont(QFont('Corbel Light', 16))
        self.button_view_works.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_view_works.clicked.connect(self.view_answers)


        """Кнокп выхода"""
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QRect(120, 800, 121, 41))
        self.exit_button.setText("Выход")
        self.exit_button.setFont(QFont('Corbel Light', 20))
        self.exit_button.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        self.exit_button.clicked.connect(exit)


        """Кнопка сворачивания"""
        self.minimize_button = QPushButton(self.main_window)
        self.minimize_button.setText("-")
        self.minimize_button.setFont(QFont('Corbel', 20))
        self.minimize_button.setStyleSheet("background-color: #E73F11; color: white")

        self.minimize_button.setFixedSize(51, 31)
        self.minimize_button.move(1400, 10)
        self.minimize_button.show()

        self.minimize_button.clicked.connect(self.minimize_windows)


        self.button_change_disc_task = QPushButton(self.main_window)
        self.button_change_disc_task.setGeometry(QRect(850, 480, 151, 41))
        self.button_change_disc_task.setText("Изменить")
        self.button_change_disc_task.setFont(QFont('Corbel Light', 22))
        self.button_change_disc_task.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        self.button_change_disc_task.clicked.connect(self.change_disc_task)


        self.button_save_changes_disc_task = QPushButton(self.main_window)
        self.button_save_changes_disc_task.setGeometry(QRect(850, 760, 151, 41))
        self.button_save_changes_disc_task.setText("Сохранить")
        self.button_save_changes_disc_task.setFont(QFont('Corbel Light', 22))
        self.button_save_changes_disc_task.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        self.button_save_changes_disc_task.clicked.connect(self.update_disc)

# ----- Добавление текстовых областей ---------

        self.text_box = QTextBrowser(self.main_window)
        self.text_box.setGeometry(QRect(530, 210, 781, 631))
        self.text_box.setFont(QFont('Corbel Light', 24))
        self.text_box.setReadOnly(True)


        self.text_discription_tasks = QTextBrowser(self.main_window)
        self.text_discription_tasks.setGeometry(QRect(390, 280, 1051, 181))
        self.text_discription_tasks.setFont(QFont('Corbel Light', 18))
        self.text_discription_tasks.setReadOnly(True)

        self.text_new_discription_tasks = QTextEdit(self.main_window)
        self.text_new_discription_tasks.setGeometry(QRect(390, 550, 1051, 181))
        self.text_new_discription_tasks.setFont(QFont('Corbel Light', 18))
    
    # ------------------- ДЛЯ ДОБАВЛЕНИЯ НОВОГО -------------------

        self.text_add_new_task = QTextEdit(self.main_window)
        self.text_add_new_task.setGeometry(QRect(610, 240, 721, 36))
        self.text_add_new_task.setFont(QFont('Corbel Light', 16))
        self.text_add_new_task.setPlaceholderText("Введите название задания")

        self.text_add_descr = QTextEdit(self.main_window)
        self.text_add_descr.setGeometry(QRect(610, 310, 721, 211))
        self.text_add_descr.setFont(QFont('Corbel Light', 16))
        self.text_add_descr.setPlaceholderText("Опишите суть задания")

# ---------------------------------------------


# ---- Добавление выпадающего меню -----
        self.lesson = QComboBox(self.centralwidget)
        self.lesson.setGeometry(QRect(780, 170, 281, 22))
        self.lesson.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        for id in lessons[0].split("-"):
            lessons_name = database.execute(f"SELECT lesson_name FROM lessons WHERE lesson_ID = ?", (id, )).fetchone()[0]
            self.lesson.addItem(lessons_name)


    # - / - / - / МЕНЮ ДЛЯ ЛИСТА СТУДЕНТОВ - / - / - / - /

        self.lesson_choose = QComboBox(self.main_window)
        self.lesson_choose.setGeometry(QRect(620, 180, 281, 22))
        self.lesson_choose.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        for id in lessons[0].split("-"):
            lessons_name = database.execute(f"SELECT lesson_name FROM lessons WHERE lesson_ID = ?", (id, )).fetchone()[0]
            self.lesson_choose.addItem(lessons_name)

        self.lesson_choose.currentTextChanged.connect(self.update_connected_groups)


        self.group_choose = QComboBox(self.main_window)
        self.group_choose.setGeometry(QRect(1020, 180, 281, 22))
        self.group_choose.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        self.group_choose.currentTextChanged.connect(self.recieve_list_of_students)

        # ------------------ ДЛЯ ДОБАВЛЕНИЯ ЗАДАНИЙ ------------------

        self.button_confirm_new_task = QPushButton(self.main_window)
        self.button_confirm_new_task.setGeometry(QRect(850, 560, 151, 41))
        self.button_confirm_new_task.setStyleSheet(
            "font: 25 22pt \"Corbel Light\";\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )
        self.button_confirm_new_task.setText("Добавить")

        self.button_confirm_new_task.clicked.connect(self.confirm_new_task)
    #  - / - / - / - / - / - / - / - / - / - / - / - / - / - /


    # - \- \- \- \ -\- МЕНЮ ДЛЯ ПРОСМОТРА ЗАДАНИЙ ПРЕПОДОМ \- \- \- \- \- \- \- \ 

        self.task_lesson_choose = QComboBox(self.main_window)
        self.task_lesson_choose.setGeometry(QRect(610, 190, 281, 22))
        self.task_lesson_choose.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        for id in lessons[0].split("-"):
            lessons_name = database.execute(f"SELECT lesson_name FROM lessons WHERE lesson_ID = ?", (id, )).fetchone()[0]
            self.task_lesson_choose.addItem(lessons_name)

        self.task_lesson_choose.currentTextChanged.connect(self.update_all_tasks)

        self.task_choose = QComboBox(self.main_window)
        self.task_choose.setGeometry(QRect(1040, 190, 281, 22))
        self.task_choose.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        self.task_choose.currentTextChanged.connect(self.recieve_task)

        # -------------- ДЛЯ ДОБАВЛЕНИЯ ЗАДАЧ -------------------------

        self.add_lesson_choose = QComboBox(self.main_window)
        self.add_lesson_choose.setGeometry(QRect(800, 190, 281, 22))
        self.add_lesson_choose.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        for id in lessons[0].split("-"):
            lessons_name = database.execute(f"SELECT lesson_name FROM lessons WHERE lesson_ID = ?", (id, )).fetchone()[0]
            self.add_lesson_choose.addItem(lessons_name)

        self.add_lesson_choose.currentTextChanged.connect(self.new_task_clener)

    # - \ - \ -\ -\ - \- \- \- \- \- \- \- \- \- \ -\ -\ -\ -\

# --- УЧАСТКИ ДЛЯ ПРЕДУПРЖЕДЕНИЯ

        self.line_warning = QFrame(self.centralwidget)
        self.line_warning.setGeometry(QRect(610, 620, 721, 171))
        self.line_warning.setStyleSheet("color: #E73F11")
        self.line_warning.setFrameShadow(QFrame.Plain)
        self.line_warning.setLineWidth(200)
        self.line_warning.setMidLineWidth(0)
        self.line_warning.setFrameShape(QFrame.HLine)
        self.line_warning.hide()

        self.warning_1_line = QLabel(self.main_window)
        self.warning_1_line.setText("Одно или более полей пустые. Пожалуйста, заполните")
        self.warning_1_line.setGeometry(QRect(660, 660, 641, 31))
        self.warning_1_line.setStyleSheet(
            "font: 25 20pt \"Corbel Light\";\n"
            "color: white; background-color: rgba(255, 255, 255, 0);"
        )
        self.warning_1_line.setAlignment(Qt.AlignCenter)

        self.warning_2_line = QLabel(self.main_window)
        self.warning_2_line.setText("поля соответствующим тектом и повторите попытку.")
        self.warning_2_line.setGeometry(QRect(630, 710, 681, 31))
        self.warning_2_line.setStyleSheet(
            "font: 25 20pt \"Corbel Light\";\n"
            "color: white; background-color: rgba(255, 255, 255, 0);"
        )
        self.warning_2_line.setAlignment(Qt.AlignCenter)

# Добавление полосок
        self.main_window.setCentralWidget(self.centralwidget)

    def minimize_windows(self):
        self.main_window.showMinimized()

    def warning_on(self):
        self.warning_1_line.show()
        self.warning_2_line.show()
        self.line_warning.show()

    def warning_off(self):
        self.warning_1_line.hide()
        self.warning_2_line.hide()
        self.line_warning.hide()

    def update_connected_groups(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        self.group_choose.clear()
        groups = list()

        for (group_ID, ) in database.execute(
            "SELECT group_ID FROM group_lessons WHERE lesson_ID = ?",
                database.execute(
                    "SELECT lesson_ID FROM lessons WHERE lesson_name = ?", (self.lesson_choose.currentText(), )
                ).fetchone()
        ).fetchall():
            groups.append(group_ID)

        for group in sorter(groups):
            self.group_choose.addItem(
                database.execute(
                    "SELECT group_name FROM groups WHERE group_ID = ?", (group, )
                ).fetchone()[0]
            )

    def recieve_list_of_students(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        group_ID = database.execute(
            "SELECT group_ID FROM groups WHERE group_name = ?", (self.group_choose.currentText() ,)
        ).fetchone()

        if group_ID is None:
            pass
        else:
            result = ""

            students_ID = database.execute(
                "SELECT user_ID FROM students_groups WHERE group_ID = ?", group_ID
            ).fetchall()

            for student in students_ID:
                result = result + database.execute(
                    "SELECT lfp FROM users WHERE user_ID = ?", student
                ).fetchone()[0]

                if student != students_ID[-1]:
                    result += "\n"

            self.text_box.setText(result)

    def update_all_tasks(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        self.disc_status_checker()

        self.task_choose.clear()

        for (work_name, ) in database.execute(
            "SELECT work_name FROM tasks WHERE lessons_key = ?", database.execute(
                "SELECT lesson_ID FROM lessons WHERE lesson_name = ?", (self.task_lesson_choose.currentText() ,)
            ).fetchone()
        ).fetchall():
            self.task_choose.addItem(work_name)

    def recieve_task(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        self.disc_status_checker()

        work_ID = database.execute(
            "SELECT work_ID FROM tasks WHERE work_name = ?", (self.task_choose.currentText(), )
        ).fetchone()

        if work_ID is None:
            pass
        else:
            self.text_discription_tasks.setText(database.execute(
                "SELECT discription FROM tasks WHERE work_ID = ?", work_ID
            ).fetchone()[0])

    def change_disc_task(self):

        self.button_change_disc_task.setEnabled(False)

        self.text_new_discription_tasks.show()
        self.text_new_discription_tasks.clear()

        self.button_save_changes_disc_task.show()

        self.button_change_disc_task.setEnabled(False)

    def update_disc(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        database.execute(
            "UPDATE tasks set discription = ? WHERE work_name  = ?", 
                (self.text_new_discription_tasks.toPlainText(), self.task_choose.currentText())
        )

        file_location.commit()

        self.text_new_discription_tasks.clear()
        self.text_new_discription_tasks.hide()
        self.button_save_changes_disc_task.hide()

        self.button_change_disc_task.setEnabled(True)

        self.recieve_task()

    def disc_status_checker(self):
        if not self.button_change_disc_task.isEnabled():
            self.text_new_discription_tasks.clear()
            self.text_new_discription_tasks.hide()

            self.button_save_changes_disc_task.hide()
            self.button_change_disc_task.setEnabled(True)

    def new_task_clener(self):

        self.text_add_descr.clear()
        self.text_add_new_task.clear()

    def confirm_new_task(self):

        if (self.text_add_descr.toPlainText() == "") or (self.text_add_new_task.toPlainText() == ""):
            self.warning_on()
        else:
        # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
            file_location = sqlite3.connect(os.getcwd() + '\database.db')
            database = file_location.cursor()

            work_ID = database.execute(
                "SELECT max(work_ID) FROM tasks"
            ).fetchone()[0] + 1

            lesson_key = database.execute(
                "SELECT lesson_ID FROM lessons WHERE lesson_name = ?", (self.add_lesson_choose.currentText(), )
            ).fetchone()[0]

            work_name = self.text_add_new_task.toPlainText()
            work_descr = self.text_add_descr.toPlainText()

            database.execute(
                "INSERT INTO tasks VALUES (?, ?, ?, ?)", (work_ID, work_name, work_descr, lesson_key)
            )

            for group_ID in database.execute("SELECT group_ID FROM group_lessons WHERE lesson_ID = ?", (lesson_key, )).fetchall():

                for student_ID in database.execute("SELECT user_ID FROM users WHERE group_ID = ?", group_ID).fetchall():

                    database.execute(
                            "INSERT INTO student_tasks VALUES (?, ?, ?, ?, ?)", 
                            (work_ID, student_ID[0], None, None, None)
                        )

            file_location.commit()

            self.text_add_descr.clear()
            self.text_add_new_task.clear()

            if not self.line_warning.isHidden():
                self.warning_off()

# - - - - ОПРЕДЕЛЕНИЕ СКРЫТИЯ ЭЛЕМЕНТОВ - - - -

    def auto_off(self):
        """
        Функция определяет последний известный статус окна
        и деактивирует (скрывает) элементы окна с подобным статусом,
        чтобы было легче включить элементы нового.
        """

        {
            "main" : self.main_lobby_off,
            "list" : self.list_of_students_0ff,
            "tasks" : self.view_tasks_off,
            "answers" : self.view_answers_off,
            "add" : self.add_new_task_off
        }[self.window_status]()

# - - - - - - - - - - - - - - - - - - - - - - -


# - - - - ФУНКЦИИ СКРЫТИЯ ЭЛЕМЕНТОВ - - - - 
    def main_lobby_off(self):

        self.label_hint_1.hide()
        self.label_hint_2.hide()
        self.label_hint_3.hide()
        self.label_hints.hide()

        self.line_left_hint.hide()
        self.line_right_hint.hide()

        self.label_all_works_checked.hide()
        self.label_all_works.hide()

        self.lesson.hide()

    def list_of_students_0ff(self):

        self.group_choose.hide()
        self.label_group.hide()
        self.label_lesson.hide()
        self.text_box.clear()
        self.text_box.hide()

        self.lesson_choose.hide()

    def view_tasks_off(self):

        if not self.button_change_disc_task.isEnabled():
            self.button_change_disc_task.setEnabled(True)

            self.text_new_discription_tasks.clear()
            self.text_new_discription_tasks.hide()

            self.button_save_changes_disc_task.hide()

        self.button_change_disc_task.hide()

        self.label_discription.hide()
        self.label_task_lesson.hide()
        self.label_task.hide()

        self.text_discription_tasks.hide()
        self.text_discription_tasks.hide()

        self.task_choose.hide()
        self.task_lesson_choose.hide()

    def view_answers_off(self):
        pass

    def add_new_task_off(self):

        if not self.line_warning.isHidden():
                self.warning_off()

        self.label_add_new_task.hide()
        self.label_add_descr.hide()
        self.label_add_to_lesson.hide()

        self.button_confirm_new_task.hide()

        self.text_add_descr.hide()
        self.text_add_new_task.hide()
        self.text_add_descr.clear()
        self.text_add_new_task.clear()

        self.add_lesson_choose.hide()


 # - - - - ФУНКЦИИ ПЕРЕХОДА НА ЭЛЕМЕНТЫ - - - -

    def main_lobby(self):
    
        self.auto_off()
        self.window_status = "main"

        self.label_hint_1.show()
        self.label_hint_2.show()
        self.label_hint_3.show()
        self.label_hints.show()

        self.line_left_hint.show()
        self.line_right_hint.show()

        self.label_all_works_checked.show()
        self.label_all_works.show()

        self.lesson.show()
        self.label_all_stat.setText("Общая статистика")

    def list_of_students(self):

        self.auto_off()
        self.window_status = "list"

        self.lesson_choose.show()

        self.group_choose.show()
        self.label_group.show()
        self.label_lesson.show()

        self.text_box.show()

        self.label_all_stat.setText("Список студентов")

        self.update_connected_groups()
        self.recieve_list_of_students()

    def view_tasks(self):

        self.auto_off()
        self.window_status = "tasks"

        self.button_change_disc_task.show()

        self.label_discription.show()
        self.label_task_lesson.show()
        self.label_task.show()

        self.text_discription_tasks.show()

        self.task_choose.show()
        self.task_lesson_choose.show()

        self.label_all_stat.setText("Задания курса")

        self.update_all_tasks()
        self.recieve_task()

    def view_answers(self):

        self.auto_off()
        self.window_status = "answers"

    def add_new_task(self):

        self.auto_off()
        self.window_status = "add"

        self.label_add_new_task.show()
        self.label_add_descr.show()
        self.label_add_to_lesson.show()

        self.button_confirm_new_task.show()

        self.text_add_descr.show()
        self.text_add_new_task.show()

        self.add_lesson_choose.show()

        self.label_all_stat.setText("Новые задания")
