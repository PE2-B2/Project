from PyQt5.QtWidgets import QApplication
import sys
from src import view, gui
from src import model
import time


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gui.MainWindow()
    window.show()
    app.exec_()
