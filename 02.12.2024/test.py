from PyQt5 import QtWidgets
import main

class Mywindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.a = 0
        self.ocenka = 0 
        self.ui.pushButton_2.clicked.connect(self.second)
        self.ui.pushButton.clicked.connect(self.tretye)
        self.ui.pushButton_3.clicked.connect(self.chetyree)
        self.ui.pushButton_4.clicked.connect(self.pyatoe)
        self.ui.pushButton_5.clicked.connect(self.shestoye)
        self.ui.pushButton_6.clicked.connect(self.sedmooe)
        self.ui.pushButton_7.clicked.connect(self.end)
        self.ui.pushButton_8.clicked.connect(self.result)

    
        self.ui.stackedWidget.setCurrentIndex(0)
    def second(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def tretye(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        
    def chetyree(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        
    def pyatoe(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        
    def shestoye(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        
    def sedmooe(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        
    def end(self):
        self.ui.stackedWidget.setCurrentIndex(7)
        


    
    def result(self):
        if self.ui.radioButton_2.isChecked():
            self.a += 1
        if self.ui.radioButton_4.isChecked():
            self.a += 1
        if self.ui.radioButton_7.isChecked():
            self.a += 1
        if self.ui.radioButton_10.isChecked() or self.ui.radioButton_11.isChecked() or self.ui.radioButton_12.isChecked():
            self.a += 1
        if self.ui.radioButton_13.isChecked():
            self.a += 1
        if self.ui.radioButton_16.isChecked():
            self.a += 1
        
        if self.a <=2:
            self.ocenka == 2
        if self.a <=4:
            self.ocenka == 3
        if self.a == 5:
            self.ocenka == 4
        if self. a == 6:
            self.ocenka == 5

        self.ui.label_8.setText(f"tvoi balli: {self.a}")
        
        self.ui.label_9.setText(f"ocenka: {self.ocenka}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())