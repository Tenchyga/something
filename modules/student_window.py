from re import I
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QComboBox, QFrame, QTextBrowser
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QRect

import sqlite3, os

class StudentWindow():
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
        self.group_ID = database.execute(f"SELECT group_ID FROM users WHERE user_ID = ?", (self.user, )).fetchone()[0]
        self.student_group = database.execute(f"SELECT group_name FROM groups WHERE group_ID = ?", (self.group_ID, )).fetchone()[0]

        self.lessons = database.execute("SELECT lesson_ID FROM group_lessons WHERE group_ID = ?", (self.group_ID, )).fetchall()

        self.file_directory = ''
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

# ТЕКСТОВЫЕ ПОЛЯ

        self.text_comment = QTextBrowser(self.centralwidget)
        self.text_comment.setGeometry(QRect(410, 570, 901, 81))
        self.text_comment.setFont(QFont('Corbel Light', 20))
        self.text_comment.setPlaceholderText("Преподаватель еще прикреплял комментарий")
        self.text_comment.setReadOnly(True)

        self.text_grade = QTextBrowser(self.centralwidget)
        self.text_grade.setGeometry(QRect(1340, 610, 101, 41))
        self.text_grade.setFont(QFont('Corbel Light', 16))
        self.text_grade.setPlaceholderText("Оценка")
        self.text_grade.setReadOnly(True)

        self.text_to_send = QTextBrowser(self.main_window)
        self.text_to_send.setGeometry(QRect(570, 290, 801, 192))
        self.text_to_send.setFont(QFont('Corbel Light', 18))
        self.text_to_send.setReadOnly(True)

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

        self.menu_button.clicked.connect(self.main_lobby_show)


        self.button_to_upload = QPushButton(self.main_window)
        self.button_to_upload.setGeometry(QRect(650, 500, 261, 51))
        self.button_to_upload.setStyleSheet(
            "font: 25 22pt \"Corbel Light\";\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);"
        )
        self.button_to_upload.setText("Загрузить работу")

        self.button_to_upload.clicked.connect(self.get_directory)


        self.button_to_send = QPushButton(self.main_window)
        self.button_to_send.setGeometry(QRect(1040, 500, 261, 51))
        self.button_to_send.setStyleSheet(
            "font: 25 22pt \"Corbel Light\";\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(139, 35, 9);"
        )
        self.button_to_send.setEnabled(False)
        self.button_to_send.setText("Отправить")

        self.button_to_send.clicked.connect(self.upload_work)


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

        for current_button in range(len(self.lessons)):

            if current_button == 0:
                self.button_1_ID = self.lessons[current_button]
                self.button_task_1.setText(database.execute(
                    "SELECT lesson_name FROM lessons WHERE lesson_ID = ?", self.button_1_ID
                ).fetchone()[0])
                self.button_task_1.show()

                self.button_task_1.clicked.connect(lambda: self.work_to_sent(self.button_1_ID))

            elif current_button == 1:
                self.button_2_ID = self.lessons[current_button]
                self.button_task_2.setText(database.execute(
                    "SELECT lesson_name FROM lessons WHERE lesson_ID = ?", self.button_2_ID
                ).fetchone()[0])
                self.button_task_2.show()

                self.button_task_2.clicked.connect(lambda: self.work_to_sent(self.button_2_ID))

            elif current_button == 2:
                self.button_3_ID = self.lessons[current_button]
                self.button_task_3.setText(database.execute(
                    "SELECT lesson_name FROM lessons WHERE lesson_ID = ?", self.button_3_ID
                ).fetchone()[0])
                self.button_task_3.show()

                self.button_task_3.clicked.connect(lambda: self.work_to_sent(self.button_3_ID))

            elif current_button == 3:
                self.button_4_ID = self.lessons[current_button]
                self.button_task_4.setText(database.execute(
                    "SELECT lesson_name FROM lessons WHERE lesson_ID = ?", self.button_task_4
                ).fetchone()[0])
                self.button_task_4.show()

                self.button_task_4.clicked.connect(lambda: self.work_to_sent(self.button_4_ID))

            elif current_button == 4:
                self.button_5_ID = self.lessons[current_button]
                self.button_task_5.setText(database.execute(
                    "SELECT lesson_name FROM lessons WHERE lesson_ID = ?", self.button_5_ID
                ).fetchone()[0])
                self.button_task_5.show()

                self.button_task_5.clicked.connect(lambda: self.work_to_sent(self.button_5_ID))

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

        username = database.execute(f"SELECT lfp FROM users WHERE user_ID = ?", (self.user, )).fetchone()[0].split(" ")[1]
        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setGeometry(QRect(590, 30, 671, 81))
        self.label_welcome.setText(f"Добро пожаловать, {username}!")
        self.label_welcome.setFont(QFont('Corbel Light', 30))
        self.label_welcome.setAlignment(Qt.AlignCenter)


        """ Добавление надписи 'Общая статистика' """
        self.label_all_stat = QLabel(self.centralwidget)
        self.label_all_stat.setText("Общая статистика")
        self.label_all_stat.setGeometry(QRect(840, 120, 161, 31))
        self.label_all_stat.setFont(QFont('Corbel Light', 16))
        self.label_all_stat.setAlignment(Qt.AlignCenter)


        """ Добавление надписи 'Всего проверенно работ' """
        self.label_all_works_checked = QLabel(self.centralwidget)
        self.label_all_works_checked.setGeometry(QRect(750, 190, 351, 61))
        self.label_all_works_checked.setFont(QFont('Corbel Light', 22))
        self.label_all_works_checked.setAlignment(Qt.AlignCenter)

        self.label_all_works_checked.setText("Всего зачтено работ: " + str(
            len(database.execute(
                "SELECT grade FROM student_tasks WHERE grade IS NOT NULL AND student_ID = ?", (self.user, )
            ).fetchall())
            )
        )

        """ Добавление надписи 'Всего загружено работ' """

        self.label_all_works = QLabel(self.centralwidget)
        self.label_all_works.setGeometry(QRect(750, 150, 351, 61))
        self.label_all_works.setFont(QFont('Corbel Light', 22))
        self.label_all_works.setAlignment(Qt.AlignCenter)

        self.label_all_works.setText("Всего загружено работ: " + str(
            (len(database.execute(
                "SELECT file FROM student_tasks WHERE file IS NOT NULL AND student_ID = ?", (self.user, )
            ).fetchall()))
        ))


        """ Добавление надписи 'Группа:' """

        self.label_group = QLabel(self.centralwidget)
        self.label_group.setText(f"Группа: {self.student_group}")
        self.label_group.setGeometry(QRect(750, 240, 351, 31))
        self.label_group.setFont(QFont('Corbel Light', 22))
        self.label_group.setAlignment(Qt.AlignCenter)


        """ Добавление надписи 'Предметная статистика' """
        self.label_work_stat = QLabel(self.centralwidget)
        self.label_work_stat.setText("Предметная статистика")
        self.label_work_stat.setGeometry(QRect(810, 280, 211, 41))
        self.label_work_stat.setFont(QFont('Corbel Light', 16))


        """ Добавление надписи про количество загруженных работ выбранного курса """
        self.label_works_upload = QLabel(self.centralwidget)
        self.label_works_upload.setGeometry(QRect(410, 390, 351, 41))
        self.label_works_upload.setFont(QFont('Corbel Light', 22))
        self.label_works_upload.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        """ Добавление надписи про проверенные работы выбранного курса """
        self.label_woks_checked = QLabel(self.centralwidget)
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


        """ Добавление надписи для выбора задания"""
        self.label_task_to_send = QLabel(self.main_window)
        self.label_task_to_send.setGeometry(QRect(480, 230, 91, 31))
        self.label_task_to_send.setText("Задание:")
        self.label_task_to_send.setFont(QFont('Corbel Light', 16))


        """ Добавление надписи для описания задания"""

        self.label_task_descr_to_send = QLabel(self.main_window)
        self.label_task_descr_to_send.setGeometry(QRect(390, 280, 171, 31))
        self.label_task_descr_to_send.setText("Описание задания:")
        self.label_task_descr_to_send.setFont(QFont('Corbel Light', 16))

        """ Добавление надписи 'Личный комментарий' """
        self.label_comment = QLabel(self.centralwidget)
        self.label_comment.setGeometry(QRect(410, 520, 391, 41))
        self.label_comment.setFont(QFont('Corbel Light', 22))
        self.label_comment.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.label_comment.setText("Комментарий преподавателя:")

    # ---- Добавление выпадающего меню -----
        """ Добавление меню для выбора предметной статистики """

        self.comboBox_work = QComboBox(self.centralwidget)
        self.comboBox_work.setGeometry(QRect(1050, 500, 261, 21))
        self.comboBox_work.setStyleSheet(
            "font: 25 12pt \"Corbel Light\";"
            "selection-color: black;"
            "selection-background-color: white;"
            "background-color: #E73F11;"
            "color: white;"
        )

        self.comboBox_task = QComboBox(self.centralwidget)
        self.comboBox_task.setGeometry(QRect(1050, 530, 261, 21))
        self.comboBox_task.setStyleSheet(
            "font: 25 12pt \"Corbel Light\";\n"
            "selection-color: rgb(0, 0, 0);\n"
            "selection-background-color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);\n"
            "color: rgb(255, 255, 255);"
        )

        for element in self.lessons:
            lesson_name = database.execute("SELECT lesson_name FROM lessons WHERE lesson_ID = ?", element).fetchone()[0]
            self.comboBox_work.addItem(lesson_name)

        self.change_stat_lesson()
        self.comboBox_work.currentTextChanged.connect(self.change_stat_lesson)

        self.print_information()
        self.comboBox_task.currentTextChanged.connect(self.print_information)

        self.task_to_send = QComboBox(self.main_window)
        self.task_to_send.setGeometry(QRect(570, 240, 321, 21))
        self.task_to_send.setStyleSheet(
            "font: 25 12pt \"Corbel Light\";\n"
            "selection-color: rgb(0, 0, 0);\n"
            "selection-background-color: rgb(255, 255, 255);\n"
            "background-color: rgb(231, 63, 17);\n"
            "color: rgb(255, 255, 255);"
        )

        self.task_to_send.currentTextChanged.connect(self.show_descr_of_task)

# --------------
    # ---- Вывод всего на экран ----
        self.main_window.setCentralWidget(self.centralwidget)

    def minimize_window(self):
        self.main_window.showMinimized()

    def show_descr_of_task(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        descr = database.execute(
            "SELECT discription FROM tasks WHERE work_name = ?", (self.task_to_send.currentText(), )
        ).fetchone()

        if descr is None:
            pass
        else:
            self.text_to_send.setText(descr[0])

# - - - - ОПРЕДЕЛЕНИЕ СКРЫТИЯ ЭЛЕМЕНТОВ - - - -

    def auto_off(self):
        """
        Функция определяет последний известный статус окна
        и деактивирует (скрывает) элементы окна с подобным статусом,
        чтобы было легче включить элементы нового.
        """

        {
            "main" : self.main_lobby_off,
            "send" : self.send_off
        }[self.window_status]()

    def auto_on(self):
        """
        Функция определяет последний известный статус окна
        и активирует (показывает) элементы окна с подобным статусом,
        чтобы было легче выключить элементы старого.
        """

        {
            "main" : self.main_lobby_show,
            "send" : self.send_show
        }[self.window_status]()

# - - - - - - - - - - - - - - - - - - - - - - -

    def change_stat_lesson(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        all_works = 0
        all_checked_works = 0

        for (task_ID, grade) in database.execute(
            "SELECT task_ID, grade FROM student_tasks WHERE file IS NOT NULL AND student_ID = ?", (self.user, )
        ).fetchall():
            if (task_ID, ) in database.execute(
                "SELECT work_ID FROM tasks WHERE lessons_key = ?", database.execute(
                    "SELECT lesson_ID FROM lessons WHERE lesson_name = ?", (self.comboBox_work.currentText(), )
                ).fetchone()
            ).fetchall():
                all_works += 1

                if grade is not None:
                    if (0 <= grade <= 100): 
                        all_checked_works += 1

        self.label_works_upload.setText(
            "Загруженных работ: " + str(all_works)
        )

        self.label_woks_checked.setText(
            "Работ зачтено: " + str(all_checked_works)
        )

        self.comboBox_task.clear()

        for (task, ) in database.execute(
            "SELECT work_name FROM tasks WHERE lessons_key = ?",
                database.execute(
                    "SELECT lesson_ID FROM lessons WHERE lesson_name = ?", (self.comboBox_work.currentText(), )
                ).fetchone()
        ).fetchall():
            self.comboBox_task.addItem(task)

# ---- ФУНКЦИИ НА СКРЫТИЕ / ПОКАЗ ОКОН ------

    def main_lobby_off(self):

        self.label_all_works.hide()
        self.label_all_works_checked.hide()
        self.label_group.hide()
        self.label_work_stat.hide()
        self.label_works_upload.hide()
        self.label_woks_checked.hide()
        self.label_advice.hide()
        self.label_advices.hide()
        self.label_comment.hide()

        self.line_above_advice.hide()
        self.line_left_work_stat.hide()
        self.line_right_work_stat.hide()

        self.comboBox_work.hide()
        self.comboBox_task.hide()

        self.text_comment.hide()
        self.text_grade.hide()

    def send_off(self):

        self.task_to_send.clear()
        self.task_to_send.hide()

        self.text_to_send.clear()
        self.text_to_send.hide()

        self.label_task_to_send.hide()
        self.label_task_descr_to_send.hide()

        self.button_to_upload.hide()
        self.button_to_send.hide()

        self.button_to_send.setStyleSheet(
            "font: 25 22pt \"Corbel Light\";\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(139, 35, 9);"
        )
        self.button_to_send.setEnabled(False)

        self.file_directory = ''

    def main_lobby_show(self):

        self.label_all_stat.setText("Общая статистика")

        self.auto_off()
        self.window_status = "main"

        self.label_all_works.show()
        self.label_all_works_checked.show()
        self.label_group.show()
        self.label_work_stat.show()
        self.label_works_upload.show()
        self.label_woks_checked.show()
        self.label_advice.show()
        self.label_advices.show()
        self.label_comment.show()

        self.line_above_advice.show()
        self.line_left_work_stat.show()
        self.line_right_work_stat.show()

        self.comboBox_work.show()
        self.comboBox_task.show()

        self.text_comment.show()
        self.text_grade.show()

        self.change_stat_lesson()

    def send_show(self):

        self.label_all_stat.setText("Загрузка работ")

        self.label_task_to_send.show()
        self.task_to_send.show()
        self.label_task_descr_to_send.show()
        self.text_to_send.show()

        self.button_to_upload.show()
        self.button_to_send.show()

# -------------------------------------------

    def print_information(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        task = database.execute(
            "SELECT work_ID FROM tasks WHERE work_name = ?", (self.comboBox_task.currentText(), )
        ).fetchone()

        if task is None:
            self.text_comment.clear()
            self.text_grade.clear()
        else:

            comment = database.execute(
                    "SELECT comment FROM student_tasks WHERE student_ID = ? AND task_ID = ?", (self.user, task[0])
                ).fetchone()

            grade = database.execute(
                "SELECT grade FROM student_tasks WHERE student_ID = ? AND task_ID = ?", (self.user, task[0])
            ).fetchone()

            if comment[0] is None:
                self.text_comment.clear()
            else:

                if len(comment[0].strip()) > 0:
                    self.text_comment.setPlainText(comment[0])

            if grade[0] is None:
                self.text_grade.clear()
            else:
                self.text_grade.setPlainText(str(grade[0]))

    def work_to_sent(self, lesson_ID):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        self.auto_off()
        self.window_status = "send"
        self.auto_on()

        for element in database.execute(
            "SELECT work_name FROM tasks WHERE lessons_key = ?", lesson_ID
        ).fetchall():
            self.task_to_send.addItem(element[0])

        if self.task_to_send.currentText() == '':
            self.button_to_upload.setEnabled(False)

            self.button_to_upload.setStyleSheet(
            "font: 25 22pt \"Corbel Light\";\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(139, 35, 9);"
            )
        else:
            self.button_to_upload.setEnabled(True)

            self.button_to_upload.setStyleSheet(
                "font: 25 22pt \"Corbel Light\";\n"
                "border-color: rgba(255, 255, 255, 0);\n"
                "color: rgb(255, 255, 255);\n"
                "background-color: rgb(231, 63, 17);"
            )

            self.show_descr_of_task()

    def get_directory(self):

        from PyQt5.QtWidgets import QFileDialog

        file_filter = 'Python File (*.py)'
        result = QFileDialog.getOpenFileName(
            caption = 'Выберите файл для загрузки',
            directory = os.getcwd(),
            filter = file_filter,
            initialFilter = 'Python File (*.py)'
        )

        self.file_directory = result[0]

        if os.path.isfile(self.file_directory):

            self.button_to_send.setStyleSheet(
                "font: 25 22pt \"Corbel Light\";\n"
                "border-color: rgba(255, 255, 255, 0);\n"
                "color: rgb(255, 255, 255);\n"
                "background-color: rgb(231, 63, 17);"
            )
            self.button_to_send.setEnabled(True)

    def converter_to_binary(self):

        with open(self.file_directory, 'rb') as file:
            blob_data = file.read()

        return blob_data

    def upload_work(self):

    # ----- ПОДКЛЮЧЕНИЕ БАЗЫ ДАННЫХ -----
        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        data = self.converter_to_binary()

        if os.path.isfile(self.file_directory):
            database.execute(
                "UPDATE student_tasks set file = ? WHERE task_ID = ? AND student_ID = ?",
                (data, database.execute("SELECT work_ID FROM tasks WHERE work_name = ?", (self.task_to_send.currentText(), )).fetchone()[0],
                    self.user)
            )

            file_location.commit()

        self.button_to_send.setStyleSheet(
            "font: 25 22pt \"Corbel Light\";\n"
            "border-color: rgba(255, 255, 255, 0);\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(139, 35, 9);"
        )
        self.button_to_send.setEnabled(False)

        self.file_directory = ''
