from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QComboBox, QFrame
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QRect

import sqlite3, os

class StudentWindow():
    def __init__(self, user):
        self.user = user

        super().__init__()

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

    # - - - СБОР ДАННЫХ - - - |

        group_ID = database.execute(f"SELECT group_ID FROM users WHERE user_ID = ?", (self.user, )).fetchone()[0]
        student_group = database.execute(f"SELECT group_name FROM groups WHERE group_ID = ?", (group_ID, )).fetchone()[0]

        lessons = database.execute("SELECT lessons_IDS from group_lessons WHERE group_ID = ?", (group_ID, )).fetchone()[0]
    # - - - - - - - - - - - - |

    # ----- Создание основого рабочего пространства -----
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

    # - - - - - - ВЫКЛЮЧЕНИЕ КНОПОК

        self.button_task_1.hide()
        self.button_task_2.hide()
        self.button_task_3.hide()
        self.button_task_4.hide()
        self.button_task_5.hide()

        for current_button in range(len(lessons.split("-"))):

            if current_button == 0:
                self.button_task_1.setText(database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", 
                                            (lessons.split("-")[current_button], )).fetchone()[0])
                self.button_task_1.show()

            elif current_button == 1:
                self.button_task_2.setText(database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", 
                                            (lessons.split("-")[current_button], )).fetchone()[0])
                self.button_task_2.show()

            elif current_button == 2:
                self.button_task_3.setText(database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", 
                                            (lessons.split("-")[current_button], )).fetchone()[0])
                self.button_task_3.show()

            elif current_button == 3:
                self.button_task_4.setText(database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", 
                                            (lessons.split("-")[current_button], )).fetchone()[0])
                self.button_task_4.show()

            elif current_button == 4:
                self.button_task_5.setText(database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", 
                                            (lessons.split("-")[current_button], )).fetchone()[0])
                self.button_task_5.show()


    # - - - - - - - - - - - -- - - -

        self.minimize_button = QPushButton(self.main_window)
        self.minimize_button.setText("-")
        self.minimize_button.setFont(QFont('Corbel', 20))
        self.minimize_button.setStyleSheet("background-color: #E73F11; color: white")

        self.minimize_button.setFixedSize(51, 31)
        self.minimize_button.move(1400, 10)
        self.minimize_button.show()

        self.minimize_button.clicked.connect(self.minimize_window)

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

        username = database.execute(f"SELECT lfp FROM users WHERE user_ID = ?", (self.user, )).fetchone()[0]
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
        teacher_names = list()
        teacher_name = str()

        for element in lessons.split("-"):
            temp_full_name = database.execute("SELECT lfp FROM users WHERE user_ID = ?", 
                (database.execute("SELECT user_ID FROM teacher_lessons WHERE lesson_ID = ?", (element, )).fetchone()[0], )).fetchone()[0]

            temp_name = str()

            temp_lfp = temp_full_name.split(" ")

            temp_name = temp_lfp[0] + " " + temp_lfp[1][0] + ". " + temp_lfp[2][0] + ". "

            teacher_names.append(temp_name)

        for name in teacher_names:
            teacher_name += name

            if (teacher_names.index(name) != len(teacher_names) - 1):
                teacher_name += ", "

        self.label_teacher = QLabel(self.centralwidget)
        self.label_teacher.setText(f'Преподаватели: {teacher_name}')
        self.label_teacher.setGeometry(QRect(410, 350, 1400, 41))
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

        for element in lessons.split("-"):
            lesson_name = database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", (element, )).fetchone()[0]
            self.comboBox_work.addItem(lesson_name)

    # ---- Вывод всего на экран ----
        self.main_window.setCentralWidget(self.centralwidget)

    def minimize_window(self):
        self.main_window.showMinimized()
