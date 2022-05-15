
import sys, sqlite3

from PyQt5.QtWidgets import QApplication

from modules.auth_window import Auth_Window
from modules.student_window import StudentWindow
from modules.teacher_window import Teacher_Window
from database_creator import create_dabase

from os import getcwd, path

def main():

    if not path.isfile('database.db'):
        create_dabase()

    loginApp = QApplication(sys.argv)
    auth_app = Auth_Window()
    loginApp.exec_()

    file_location = sqlite3.connect(getcwd() + '\database.db')
    database = file_location.cursor()

    user_ID = auth_app.user[0]
    user_role = database.execute(f"SELECT role FROM users WHERE user_ID = ?", (user_ID, )).fetchone()[0]

    if user_role == 'student':
        mainApp = QApplication(sys.argv)
        application = StudentWindow(user_ID)
        sys.exit(mainApp.exec_())
    elif user_role == 'teacher':
        mainApp = QApplication(sys.argv)
        application = Teacher_Window(user_ID)
        sys.exit(mainApp.exec_())

if __name__ == '__main__':
    main()
