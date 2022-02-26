
from os import path
import sys

from PyQt5.QtWidgets import QApplication
from modules.auth_window import Auth_Window

def main():

    mainApp = QApplication(sys.argv)
    application = Auth_Window()
    sys.exit(mainApp.exec_())

if __name__ == '__main__':
    main()
