from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QComboBox, QMessageBox, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect

import sqlite3, os

class StudentWindow():
    def __init__(self, user):
        self.user = user

        super().__init__()

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor().execute(f"SELECT * FROM users WHERE login = ?", (self.user, )).fetchone()

    # ----- Создание основого рабочего пространства -----
        self.main_window = QMainWindow()

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


    # ---- Добавление кнопок -----
        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QRect(120, 800, 121, 41))
        self.exit_button.setText("Выход")
        self.exit_button.setFont(QFont('Corbel Light', 20))
        self.exit_button.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        self.exit_button.clicked.connect(exit)

        self.menu_button = QPushButton(self.centralwidget)
        self.menu_button.setGeometry(QRect(20, 30, 311, 81))
        self.menu_button.setText("еПроверка")
        self.menu_button.setFont(QFont('Corbel Light', 44))
        self.menu_button.setStyleSheet(
            "background-color: #E73F11; color: white"
        )

        self.button_task_1 = QPushButton(self.centralwidget)
        self.button_task_1.setGeometry(QRect(20, 170, 311, 81))
        self.button_task_1.setText("Первый предмет")
        self.button_task_1.setFont(QFont('Corbel Light', 16))
        self.button_task_1.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_task_2 = QPushButton(self.centralwidget)
        self.button_task_2.setGeometry(QRect(20, 280, 311, 81))
        self.button_task_2.setText("Второй предмет")
        self.button_task_2.setFont(QFont('Corbel Light', 16))
        self.button_task_2.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_task_3 = QPushButton(self.centralwidget)
        self.button_task_3.setGeometry(QRect(20, 390, 311, 81))
        self.button_task_3.setText("Третий предмет")
        self.button_task_3.setFont(QFont('Corbel Light', 16))
        self.button_task_3.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_task_4 = QPushButton(self.centralwidget)
        self.button_task_4.setGeometry(QRect(20, 500, 311, 81))
        self.button_task_4.setText("Четвертый предмет")
        self.button_task_4.setFont(QFont('Corbel Light', 16))
        self.button_task_4.setStyleSheet(
            "color: black; background-color: white;"
        )

        self.button_task_5 = QPushButton(self.centralwidget)
        self.button_task_5.setGeometry(QRect(20, 610, 311, 81))
        self.button_task_5.setText("Пятый предмет")
        self.button_task_5.setFont(QFont('Corbel Light', 16))
        self.button_task_5.setStyleSheet(
            "color: black; background-color: white;"
        )


    # ---- Добавление линий ----
        """ Линии, отделяющие кнопки предметов от основоой рабочей области """
        self.line_main = QFrame(self.centralwidget)
        self.line_main.setGeometry(QRect(350, 10, 20, 831))
        self.line_main.setFrameShadow(QFrame.Plain)
        self.line_main.setFrameShape(QFrame.VLine)


        """ Линии по бокам надписи 'Обзорная панель' """
        self.line_view_right = QFrame(self.centralwidget)
        self.line_view_right.setGeometry(QRect(260, 130, 81, 16))
        self.line_view_right.setFrameShadow(QFrame.Plain)
        self.line_view_right.setFrameShape(QFrame.HLine)

        self.line_view_left = QFrame(self.centralwidget)
        self.line_view_left.setGeometry(QRect(10, 130, 81, 20))
        self.line_view_left.setFrameShadow(QFrame.Plain)
        self.line_view_left.setFrameShape(QFrame.HLine)


        """ Линии по бокам надписи 'Общая статистика' """
        self.line_right_all_stat = QFrame(self.centralwidget)
        self.line_right_all_stat.setGeometry(QRect(1010, 130, 441, 16))
        self.line_right_all_stat.setFrameShadow(QFrame.Plain)
        self.line_right_all_stat.setFrameShape(QFrame.HLine)
        self.line_right_all_stat.setObjectName("line_right_all_stat")

        self.line_left_all_stat = QFrame(self.centralwidget)
        self.line_left_all_stat.setGeometry(QRect(380, 130, 451, 16))
        self.line_left_all_stat.setFrameShadow(QFrame.Plain)
        self.line_left_all_stat.setFrameShape(QFrame.HLine)
        self.line_left_all_stat.setObjectName("line_left_all_stat")


        """ Линии по бокам надписи 'Предметная статистика' """
        self.line_left_work_stat = QFrame(self.centralwidget)
        self.line_left_work_stat.setGeometry(QRect(1030, 290, 421, 20))
        self.line_left_work_stat.setFrameShadow(QFrame.Plain)
        self.line_left_work_stat.setFrameShape(QFrame.HLine)

        self.line_right_work_stat = QFrame(self.centralwidget)
        self.line_right_work_stat.setGeometry(QRect(380, 290, 421, 20))
        self.line_right_work_stat.setFrameShadow(QFrame.Plain)
        self.line_right_work_stat.setFrameShape(QFrame.HLine)


        """ Линии для отсечения советов """
        self.line_above_advice = QFrame(self.centralwidget)
        self.line_above_advice.setGeometry(QRect(380, 670, 1061, 16))
        self.line_above_advice.setFrameShadow(QFrame.Plain)
        self.line_above_advice.setFrameShape(QFrame.HLine)


    # ---- Добавление разных надписей ----
        """ Добавление надписи 'Обзорная панель' """
        self.label_review = QLabel(self.centralwidget)
        self.label_review.setText("Обзорная панель")
        self.label_review.setGeometry(QRect(100, 120, 161, 41))
        self.label_review.setFont(QFont('Corbel Light', 16))


        """ Добавление надписи 'Добро пожаловать, {name}' """

        username = database[2]
        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QRect(590, 30, 671, 81))
        self.label_welcome.setText(f"Добро пожаловать, {username}!")
        self.label_welcome.setFont(QFont('Corbel Light', 30))


        """ Добавление надписи 'Общая статистика' """
        self.label_all_stat = QLabel(self.centralwidget)
        self.label_all_stat.setText("Общая статистика")
        self.label_all_stat.setGeometry(QRect(840, 120, 161, 31))
        self.label_all_stat.setFont(QFont('Corbel Light', 16))


        """ Добавление надписи 'Всего загружено работ' """

        all_works = 20                      # Получение общего числа работ сданных из базы данных

        self.label_all_works = QLabel(self.centralwidget)
        self.label_all_works.setText(f"Всего загружено работ: {all_works}")
        self.label_all_works.setGeometry(QRect(750, 160, 351, 31))
        self.label_all_works.setFont(QFont('Corbel Light', 22))
        self.label_all_works.setAlignment(Qt.AlignCenter)


        """ Добавление надписи 'Всего проверенно работ' """

        all_checked_works = 10              # Всего проверенно работ из базы данных

        self.label_all_works_checked = QLabel(self.centralwidget)
        self.label_all_works_checked.setText(f"Всего проверенно работ: {all_checked_works}")
        self.label_all_works_checked.setGeometry(QRect(750, 200, 351, 31))
        self.label_all_works_checked.setFont(QFont('Corbel Light', 22))
        self.label_all_works_checked.setAlignment(Qt.AlignCenter)


        """ Добавление надписи 'Группа:' """

        student_group = database[3]

        self.label_group = QLabel(self.centralwidget)
        self.label_group.setText(f"Группа: {student_group}")
        self.label_group.setGeometry(QRect(750, 240, 351, 31))
        self.label_group.setFont(QFont('Corbel Light', 22))
        self.label_group.setAlignment(Qt.AlignCenter)


        """ Добавление надписи 'Предметная статистика' """
        self.label_work_stat = QLabel(self.centralwidget)
        self.label_work_stat.setText("Предметная статистика")
        self.label_work_stat.setGeometry(QRect(810, 280, 211, 41))
        self.label_work_stat.setFont(QFont('Corbel Light', 16))


        """ Добавление надписи про количество загруженных работ выбранного курса """
        selected_works_uploaded = 15

        self.label_works_upload = QLabel(self.centralwidget)
        self.label_works_upload.setText(f"Загружено работ: {selected_works_uploaded}")
        self.label_works_upload.setGeometry(QRect(410, 390, 351, 41))
        self.label_works_upload.setFont(QFont('Corbel Light', 22))
        self.label_works_upload.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)


        """ Добавление имени преподавателя на выбранный предмет """
        teacher_name = 'Воронов В. С.'

        self.label_teacher = QLabel(self.centralwidget)
        self.label_teacher.setText(f'Преподаватель: {teacher_name}')
        self.label_teacher.setGeometry(QRect(410, 350, 391, 41))
        self.label_teacher.setFont(QFont('Corbel Light', 22))
        self.label_teacher.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)


        """ Добавление надписи про проверенные работы выбранного курса """
        selected_works_checked = 5

        self.label_woks_checked = QLabel(self.centralwidget)
        self.label_woks_checked.setText(f"Работ зачтено: {selected_works_checked}")
        self.label_woks_checked.setGeometry(QRect(410, 430, 351, 41))
        self.label_woks_checked.setFont(QFont('Corbel Light', 22))
        self.label_woks_checked.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)


        """ Добавление надписи 'Совет' """
        self.label_advice = QLabel(self.centralwidget)
        self.label_advice.setText("Совет:")
        self.label_advice.setGeometry(QRect(910, 690, 81, 31))
        self.label_advice.setFont(QFont('Corbel Light', 22))
 

        """ Добавление разных советов внизу """
        self_advice = "Иногда стоит лишний раз подумать над решением, прежде чем приступать к его выполнению."

        self.label_advices = QLabel(self.centralwidget)
        self.label_advices.setText(self_advice)
        self.label_advices.setGeometry(QRect(380, 730, 1051, 91))
        self.label_advices.setFont(QFont('Corbel Light', 18))
        self.label_advices.setTextFormat(Qt.AutoText)
        self.label_advices.setScaledContents(False)


    # ---- Добавление выпадающего меню -----
        """ Добавление меню для выбора предметной статистики """
        self.comboBox_work = QComboBox(self.centralwidget)
        self.comboBox_work.setGeometry(QRect(800, 320, 231, 21))
        self.comboBox_work.setStyleSheet(
            "font: 25 12pt \"Corbel Light\";"
            "selection-color: black;"
            "selection-background-color: white;"
            "background-color: #E73F11;"
            "color: white;"
        )

        self.comboBox_work.addItem("Тестовое название 1")
        self.comboBox_work.addItem("Тестовое название 2")
        self.comboBox_work.addItem("Тестовое название 3")

    # ---- Вывод всего на экран ----
        self.main_window.setCentralWidget(self.centralwidget)
