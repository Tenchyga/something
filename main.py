
import sys, sqlite3

from PyQt5.QtWidgets import QApplication

from modules.auth_window import Auth_Window
from modules.student_window import StudentWindow
from modules.teacher_window import Teacher_Window
from database_creator import create_dabase

from os import getcwd, path
import json

def main():

    if not path.isfile('database.db'):
        create_dabase()

    loginApp = QApplication(sys.argv)
    auth_app = Auth_Window()
    loginApp.exec_()

    file_location = sqlite3.connect(getcwd() + '\database.db')
    database = file_location.cursor().execute(f"SELECT * FROM users WHERE login = ?", (auth_app.user, )).fetchone()

    if database[-1] == 'student':
        mainApp = QApplication(sys.argv)
        application = StudentWindow(auth_app.user)
        sys.exit(mainApp.exec_())
    elif database[-1] == 'teacher':
        mainApp = QApplication(sys.argv)
        application = Teacher_Window(auth_app.user)
        sys.exit(mainApp.exec_())

if __name__ == '__main__':
    main()
