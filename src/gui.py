import time

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

from src import view


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Program")
        self.setGeometry(100, 100, 550, 350)

        self.setStyleSheet("background-color:white;")

        self.titleLabel = QLabel("Software Name : ", self)
        self.titleLabel.setFont(QFont('Arial bold', 15))
        self.titleLabel.move(50, 30)
        self.titleLabel.resize(180, 20)

        self.waferLabel = QLabel("Wafer : ", self)
        self.waferLabel.setFont(QFont('Arial', 10))
        self.waferLabel.move(50, 100)
        self.waferLabel.resize(150, 20)

        self.coordinateLabel = QLabel("Coordinates : ", self)
        self.coordinateLabel.setFont(QFont('Arial', 10))
        self.coordinateLabel.move(50, 150)
        self.coordinateLabel.resize(150, 20)

        self.deviceLabel = QLabel("Device ID : ", self)
        self.deviceLabel.setFont(QFont('Arial', 10))
        self.deviceLabel.move(50, 200)
        self.deviceLabel.resize(150, 20)

        self.waferEdit = QLineEdit('', self)
        self.waferEdit.setStyleSheet("border-radius:5px;border: 1px solid black;text-align: center")
        self.waferEdit.move(170, 100)
        self.waferEdit.resize(80, 20)

        self.coordinateEdit = QLineEdit('', self)
        self.coordinateEdit.setStyleSheet("border-radius:5px;border: 1px solid black;text-align: center")
        self.coordinateEdit.move(170, 150)
        self.coordinateEdit.resize(80, 20)

        self.deviceEdit = QLineEdit('', self)
        self.deviceEdit.setStyleSheet("border-radius:5px;border: 1px solid black;text-align: center")
        self.deviceEdit.move(170, 200)
        self.deviceEdit.resize(80, 20)

        self.showEdit = QCheckBox("Show Output", self)
        self.showEdit.move(350, 190)
        self.showEdit.toggle()

        self.saveEdit = QCheckBox("Save Output", self)
        self.saveEdit.move(350, 140)
        self.saveEdit.toggle()

        self.label3 = QLabel('', self)
        self.label3.move(50, 170)

        string = "background-color: grey;border: none;color: white;text-align: " \
                 "center;text-decoration: none;display: inline-block;font-size: 10px;margin: 4px 2px;cursor: pointer; "

        self.btnSave = QPushButton("OK", self)
        self.btnSave.setStyleSheet(string)
        self.btnSave.resize(130, 30)
        self.btnSave.move(380, 290)
        self.btnSave.clicked.connect(self.btn_click)

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn_click(self):
        wafer = self.waferEdit.text()
        coordinates = self.coordinateEdit.text()
        device = self.deviceEdit.text()

        start = time.time()
        view.initMainView(wafer, coordinates, device, self.saveEdit.isChecked(), self.showEdit.isChecked())
        print("time :", time.time() - start)
