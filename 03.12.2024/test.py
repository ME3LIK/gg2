from PyQt5 import QtWidgets
import main


class Mywindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = main.Ui_Form()
        self.ui.setupUi(self)
        self.a = 0
        
        self.ui.pushButton_2.clicked.connect(self.second)
        self.ui.pushButton.clicked.connect(self.tretye)
        self.ui.pushButton_3.clicked.connect(self.chetyree)
        self.ui.pushButton_4.clicked.connect(self.pyatoe)
        self.ui.pushButton_5.clicked.connect(self.shestoye)
        self.ui.pushButton_6.clicked.connect(self.sedmooe)
        self.ui.pushButton_7.clicked.connect(self.end)
        self.ui.pushButton_8.clicked.connect(self.ryuf)
        


        self.ui.stackedWidget.setCurrentIndex(0)


    def second(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        
    def tretye(self):
        self.ui.stackedWidget.setCurrentIndex(2)  
        if self.ui.radioButton_2.isChecked():
            self.a += 1
        
    def chetyree(self):
        self.ui.stackedWidget.setCurrentIndex(3)  
        if self.ui.radioButton_4.isChecked():        
            self.a += 1
        
    def pyatoe(self):
        self.ui.stackedWidget.setCurrentIndex(4)  
        if self.ui.radioButton_7.isChecked():
            self.a += 1
        
    def shestoye(self):
        self.ui.stackedWidget.setCurrentIndex(5)  
        if self.ui.radioButton_10.isChecked() or self.ui.radioButton_11.isChecked() or self.ui.radioButton_12.isChecked():
            self.a += 1
        
    def sedmooe(self):
        self.ui.stackedWidget.setCurrentIndex(6) 
        if self.ui.radioButton_13.isChecked():
            self.a += 1 
         
    def end(self):
        if self.ui.radioButton_16.isChecked():
            self.a += 1   
        
        self.ui.stackedWidget.setCurrentIndex(7)  
    
        
        
            
    def ryuf(self):
        ocenka = {
            0 : 5,
            1 : 2,
            2 : 2,
            3 : 3,
            4 : 4,
            5 : 4, 
            6 : 5
        }
        self.ui.label_8.setText(f"tvoi balli: {self.a}")        
        self.ui.label_9.setText(f"ocenka: {ocenka[self.a]}") 
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Mywindow()
    window.show()
    sys.exit(app.exec_())
