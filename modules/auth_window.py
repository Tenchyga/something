from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QLineEdit, QMessageBox, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QRect

class Auth_Window():
    def __init__(self):
        self.user = ''

        super().__init__()

        # Создание основого рабочего пространства
        self.main_window = QMainWindow()

        self.main_window.setWindowFlags(
            Qt.CustomizeWindowHint |
            Qt.Window   |
            Qt.WindowStaysOnTopHint
        )

        self.main_window.setStyleSheet("background-color: white;")
        self.main_window.setFixedSize(502, 635)
        self.main_window.show()


        # Добавление виджета, с помощью которого можно будет легально сделать полоски
        self.centralwidget = QWidget(self.main_window)


        # Создание кнопок
        self.exit_button = QPushButton(self.main_window)
        self.exit_button.setText("Выход")
        self.exit_button.setFont(QFont('Corbel Light', 20))
        self.exit_button.setStyleSheet("background-color: #E73F11; color: white")

        self.exit_button.setFixedSize(140, 30)
        self.exit_button.move(180, 560)
        self.exit_button.show()

        self.exit_button.clicked.connect(exit)


        self.sign_in_button = QPushButton(self.main_window)
        self.sign_in_button.setText("Вход")
        self.sign_in_button.setFont(QFont('Corbel Light', 20))
        self.sign_in_button.setStyleSheet("background-color: #E73F11; color: white")

        self.sign_in_button.setFixedSize(140, 30)
        self.sign_in_button.move(180, 310)
        self.sign_in_button.show()

        self.sign_in_button.clicked.connect(self.login_into_account)


        # Добавление надписи "еПроверка"
        self.title = QLabel(self.main_window)

        self.title.setText("еПроверка")
        self.title.setFixedSize(331, 101)
        self.title.move(90, 30)

        self.title.setFont(QFont('Corbel Light', 48))
        self.title.setStyleSheet("color: #E73F11")
        self.title.show()


        # Создание линий по краям "Аккаунт"
        self.line = QFrame(self.centralwidget)
        self.line.setGeometry(QRect(40, 140, 141, 16))
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)

        self.account = QLabel(self.main_window)
        self.account.setGeometry(QRect(190, 120, 121, 51))
        self.account.setText("Аккаунт")

        self.account.setFont(QFont('Corbel Light', 20))
        self.account.setStyleSheet("color: black")
        self.account.setAlignment(Qt.AlignCenter)
        self.account.show()

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QRect(320, 140, 141, 16))
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(190, 120, 121, 51))


        # Добавление полосок
        self.main_window.setCentralWidget(self.centralwidget)


        # Добавление места для написания логина и пароля
        self.login = QLineEdit(self.main_window)
        self.login.setPlaceholderText("Введите логин")
        self.login.setFixedSize(421, 31)
        self.login.move(40, 200)

        self.login.setFont(QFont('Corbel Light', 14))
        self.login.show()

        self.password = QLineEdit(self.main_window)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Введите пароль")
        self.password.setFixedSize(421, 31)
        self.password.move(40, 240)

        self.password.setFont(QFont('Corbel Light', 14))
        self.password.show()

    def login_into_account(self):
        import sqlite3, os

        is_exists = False

        file_location = sqlite3.connect(os.getcwd() + '\database.db')
        database = file_location.cursor()

        for login, password in database.execute("SELECT login, password FROM users"):
            if self.login.text() == login and self.password.text() == password:
                print("Такая запись существует.")
                is_exists = True

                self.user = login
                self.main_window.close()

        if not(is_exists):
            print("Указанной записи не существует.")
