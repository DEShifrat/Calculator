
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 361)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(147, 147, 147);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(211, 211, 211);\n"
"color: rgb(254, 254, 254);")
        self.label.setObjectName("label")
        self.equals = QtWidgets.QPushButton(self.centralwidget)
        self.equals.setGeometry(QtCore.QRect(180, 290, 91, 71))
        self.equals.setObjectName("equals")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 290, 181, 71))
        self.btn_0.setObjectName("btn_0")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(180, 220, 91, 71))
        self.btn_3.setObjectName("btn_3")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(180, 150, 91, 71))
        self.btn_6.setObjectName("btn_6")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(180, 80, 91, 71))
        self.btn_9.setObjectName("btn_9")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(90, 220, 91, 71))
        self.btn_2.setObjectName("btn_2")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(90, 150, 91, 71))
        self.btn_5.setObjectName("btn_5")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(90, 80, 91, 71))
        self.btn_8.setObjectName("btn_8")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 80, 91, 71))
        self.btn_7.setObjectName("btn_7")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 150, 91, 71))
        self.btn_4.setObjectName("btn_4")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 220, 91, 71))
        self.btn_1.setObjectName("btn_1")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(270, 80, 51, 51))
        self.plus.setObjectName("plus")
        self.division = QtWidgets.QPushButton(self.centralwidget)
        self.division.setGeometry(QtCore.QRect(270, 180, 51, 51))
        self.division.setObjectName("division")
        self.multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.multiplication.setGeometry(QtCore.QRect(270, 230, 51, 51))
        self.multiplication.setObjectName("multiplication")
        self.voice = QtWidgets.QPushButton(self.centralwidget)
        self.voice.setGeometry(QtCore.QRect(270, 280, 51, 81))
        self.voice.setObjectName("voice")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(270, 130, 51, 51))
        self.minus.setObjectName("minus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.add_functions()

        self.is_equel = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label.setText(_translate("MainWindow", "0"))
        self.equals.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.division.setText(_translate("MainWindow", "/"))
        self.multiplication.setText(_translate("MainWindow", "*"))
        self.voice.setText(_translate("MainWindow", "voice"))
        self.minus.setText(_translate("MainWindow", "-"))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.plus.clicked.connect(lambda: self.write_number(self.plus.text()))
        self.division.clicked.connect(lambda: self.write_number(self.division.text()))
        self.multiplication.clicked.connect(lambda: self.write_number(self.multiplication.text()))
        self.minus.clicked.connect(lambda: self.write_number(self.minus.text()))


        self.equals.clicked.connect(self.results)

        self.voice.clicked.connect(self.voice_qt)


    def voice_qt(self):
        self.label.setText('В разработке:')
        self.is_equel = True

    def results(self):
        if not self.is_equel:
            res = eval(self.label.text())
            self.label.setText('Результат:' + str(res))
            self.is_equel = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Невозможно выполнить данное действие")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            error.setInformativeText("Ошибка смотрите детальный разбор:")
            error.setDetailedText("Невозможно получить результат без переменных калькулятора")

            error.exec_()







    def write_number(self, number):
        if self.label.text() == '0' or self.is_equel:
            self.label.setText(number)
            self.is_equel = False
        else:
            self.label.setText(self.label.text()+number)







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
