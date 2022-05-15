from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QComboBox, QFrame
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QRect

import sqlite3, os

class Teacher_Window():
    def __init__(self, user):
        self.user = user

        super().__init__()

        # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor().execute(f"SELECT * FROM teachers WHERE login = ?", (self.user, )).fetchone()


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

        username = database[1]
        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QRect(590, 30, 671, 81))
        self.label_welcome.setText(f"Добро пожаловать, {username}!")
        self.label_welcome.setFont(QFont('Corbel Light', 30))

        self.label_all_stat = QLabel(self.centralwidget)
        self.label_all_stat.setText("Общая статистика")
        self.label_all_stat.setGeometry(QRect(840, 120, 161, 31))
        self.label_all_stat.setFont(QFont('Corbel Light', 16))

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


        # Добавление кнопок
        """Кнопка еПроверка (главная рабочая область)"""
        self.menu_button = QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QRect(20, 30, 311, 81))
        self.menu_button.setText("еПроверка")
        self.menu_button.setFont(QFont('Corbel Light', 44))
        self.menu_button.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        """Кнокпка 'Список студентов'"""
        self.button_list_o_students = QPushButton(self.centralwidget)
        self.button_list_o_students.setGeometry(QRect(20, 170, 311, 81))
        self.button_list_o_students.setText("Список студентов")
        self.button_list_o_students.setFont(QFont('Corbel Light', 16))
        self.button_list_o_students.setStyleSheet(
            "color: black; background-color: white;"
        )

        """Кнопка Просмотр заданий курса"""
        self.button_view_tasks = QPushButton(self.centralwidget)
        self.button_view_tasks.setGeometry(QRect(20, 280, 311, 81))
        self.button_view_tasks.setText("Просмотр заданий курса")
        self.button_view_tasks.setFont(QFont('Corbel Light', 16))
        self.button_view_tasks.setStyleSheet(
            "color: black; background-color: white;"
        )

        """Кнопка Просмотр сданных работ"""
        self.button_view_works = QPushButton(self.centralwidget)
        self.button_view_works.setGeometry(QRect(20, 390, 311, 81))
        self.button_view_works.setText("Просмотр сданных работ")
        self.button_view_works.setFont(QFont('Corbel Light', 16))
        self.button_view_works.setStyleSheet(
            "color: black; background-color: white;"
        )

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


        # ---- Добавление выпадающего меню -----
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QRect(780, 170, 281, 22))
        self.comboBox.setStyleSheet(
            "border-color: rgba(255, 255, 255, 0);\n"
            "font: 25 14pt \"Corbel Light\";\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )

        lessons = database[-1].split("\n")
        for element in lessons:
            self.comboBox.addItem(element)


        # Добавление полосок
        self.main_window.setCentralWidget(self.centralwidget)

    def minimize_windows(self):
        self.main_window.showMinimized()
