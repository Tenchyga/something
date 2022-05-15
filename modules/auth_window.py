
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QMainWindow, QLineEdit, QFrame
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QRect

class Auth_Window():
    def __init__(self):
        self.user = ''

        super().__init__()

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
        self.main_window.setFixedSize(502, 635)
        self.main_window.show()


        # Добавление виджета, с помощью которого можно будет легально сделать полоски
        self.centralwidget = QWidget(self.main_window)


        # Добавление надписи "еПроверка"
        self.title = QLabel(self.main_window)

        self.title.setText("еПроверка")
        self.title.setFixedSize(331, 101)
        self.title.move(90, 30)

        self.title.setFont(QFont('Corbel Light', 48))
        self.title.setStyleSheet("color: #E73F11")
        self.title.show()


        # Добавление надписи о некорректности ввода
        self.warning_lavel = QLabel(self.main_window)

        self.warning_lavel.setText("Неправильно указаны данные для входа.")
        self.warning_lavel.setFixedSize(500, 50)
        self.warning_lavel.move(25, 400)

        self.warning_lavel.setFont(QFont('Corbel Light', 20))
        self.warning_lavel.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0);")

        self.warning_lavel_2 = QLabel(self.main_window)

        self.warning_lavel_2.setText("Проверьте ввод и попробуйте снова.")
        self.warning_lavel_2.setFixedSize(500, 50)
        self.warning_lavel_2.move(35, 450)

        self.warning_lavel_2.setFont(QFont('Corbel Light', 20))
        self.warning_lavel_2.setStyleSheet("color: white; background-color: rgba(255, 255, 255, 0);")

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

        self.line_warning = QFrame(self.centralwidget)
        self.line_warning.setGeometry(QRect(0, 320, 635, 260))
        self.line_warning.setStyleSheet("color: #E73F11")
        self.line_warning.setFrameShadow(QFrame.Plain)
        self.line_warning.setLineWidth(200)
        self.line_warning.setMidLineWidth(0)
        self.line_warning.setFrameShape(QFrame.HLine)
        self.line_warning.hide()


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


        self.minimize_button = QPushButton(self.main_window)
        self.minimize_button.setText("-")
        self.minimize_button.setFont(QFont('Corbel', 20))
        self.minimize_button.setStyleSheet("background-color: #E73F11; color: white")

        self.minimize_button.setFixedSize(51, 31)
        self.minimize_button.move(410, 10)
        self.minimize_button.show()

        self.minimize_button.clicked.connect(self.minimize_window)


    def show_warning(self):
        self.line_warning.show()
        self.warning_lavel.show()
        self.warning_lavel_2.show()

    def login_into_account(self):
        import sqlite3, os

        file_location = sqlite3.connect(os.getcwd() + '\database.db')

        if (self.login.text(), ) in file_location.cursor().execute("SELECT login FROM users").fetchall():
            if (self.password.text(), ) in file_location.cursor().execute("SELECT password FROM users WHERE login = ?", (self.login.text(), )).fetchall():
                self.user = file_location.cursor().execute(f"SELECT user_ID FROM users WHERE login = ?", (self.login.text(), )).fetchone()
                self.main_window.close()
        else:
            self.show_warning()

    def minimize_window(self):
        self.main_window.showMinimized()
