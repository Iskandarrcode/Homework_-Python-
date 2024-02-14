from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Tiktac(QMainWindow):
    __count = 0
    __buttons = []
    
    def __init__(self):
        super().__init__()
        self.setMaximumSize(700, 830)
        self.setMinimumSize(700, 830)
        self.setWindowTitle("Tik_Tac")
        self.setStyleSheet("""
            border-radius: 5px;
            background-color: rgb(70, 130, 180)""")
        self.setWindowIcon(QIcon("D:\\NAJOT.KURS\\PYTHON\\Interface\\icon1.ico"))
        
        
    
        self.btn1 = QPushButton("", self)
        self.btn1.resize(200, 200)
        self.btn1.setFont(QFont("Poor Richard", 82))
        self.btn1.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn2 = QPushButton("", self)
        self.btn2.resize(200, 200)
        self.btn2.setFont(QFont("Poor Richard", 82))
        self.btn2.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn3 = QPushButton("", self)
        self.btn3.resize(200, 200)
        self.btn3.setFont(QFont("Poor Richard", 82))
        self.btn3.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn4 = QPushButton("", self)
        self.btn4.resize(200, 200)
        self.btn4.setFont(QFont("Poor Richard", 82))
        self.btn4.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn5 = QPushButton("", self)
        self.btn5.resize(200, 200)
        self.btn5.setFont(QFont("Poor Richard", 82))
        self.btn5.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn6 = QPushButton("", self)
        self.btn6.resize(200, 200)
        self.btn6.setFont(QFont("Poor Richard", 82))
        self.btn6.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn7 = QPushButton("", self)
        self.btn7.resize(200, 200)
        self.btn7.setFont(QFont("Poor Richard", 82))
        self.btn7.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn8 = QPushButton("", self)
        self.btn8.resize(200, 200)
        self.btn8.setFont(QFont("Poor Richard", 82))
        self.btn8.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.btn9 = QPushButton("", self)
        self.btn9.resize(200, 200)
        self.btn9.setFont(QFont("Poor Richard", 82))
        self.btn9.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;""")
        
        self.new_game = QPushButton("New Game", self)
        self.new_game.resize(200, 50)
        self.new_game.setFont(QFont("Times New Roman", 24))
        self.new_game.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: grey;
            border-radius: 12px;
            background-color: rgb(173, 216, 230)""")
        
        self.and_game = QPushButton("And Game", self)
        self.and_game.resize(200, 50)
        self.and_game.setFont(QFont("Times New Roman", 24))
        self.and_game.setStyleSheet("""
            border-style: solid;
            border-width: 2px;
            border-color: grey;
            border-radius: 12px;
            background-color: rgb(173, 216, 230)""")
        
        
        
        self.btn1.move(50, 50)
        self.btn2.move(245, 50)
        self.btn3.move(440, 50)
        self.btn4.move(50, 245)
        self.btn5.move(245, 245)
        self.btn6.move(440, 245)
        self.btn7.move(50, 440)
        self.btn8.move(245, 440)
        self.btn9.move(440, 440)
        self.new_game.move(440, 720)
        self.and_game.move(50, 720)
        
        self.btnn = QLabel(self)
        self.btnn.setGeometry(265, 655, 200, 50)
        self.btnn.setFont(QFont("Times New Roman", 20, weight = 100))
        
        self.btnn2 = QLabel(self)
        self.btnn2.setGeometry(250, 0, 250, 48)
        self.btnn2.setFont(QFont("Times New Roman", 20, weight = 100))
        
        
        
        self.btn1.clicked.connect(lambda: self.games(self.btn1))
        self.btn2.clicked.connect(lambda: self.games(self.btn2))
        self.btn3.clicked.connect(lambda: self.games(self.btn3))
        self.btn4.clicked.connect(lambda: self.games(self.btn4))
        self.btn5.clicked.connect(lambda: self.games(self.btn5))
        self.btn6.clicked.connect(lambda: self.games(self.btn6))
        self.btn7.clicked.connect(lambda: self.games(self.btn7))
        self.btn8.clicked.connect(lambda: self.games(self.btn8))
        self.btn9.clicked.connect(lambda: self.games(self.btn9))
        self.new_game.clicked.connect(lambda: self.new_game_click())
        self.and_game.clicked.connect(lambda: self.and_game_click())
        
        
        self.__buttons =[self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,
                    self.btn7,self.btn8,self.btn9]
    
    def games(self, text):
        Tiktac.__count += 1
        if text.text() == "":
            if Tiktac.__count % 2 == 0:
                text.setText("O")
            else:
                text.setText("X")
            self.winner()
                
    def winner(self):
        if self.btn1.text() == self.btn2.text() and self.btn1.text() == self.btn3.text() and self.btn1.text() != "" and self.btn2.text() != "" and self.btn3.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn1.text()} player won !")
            self.btn1.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn2.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn3.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn1.text() == self.btn4.text() and self.btn1.text() == self.btn7.text() and self.btn1.text() != "" and self.btn4.text() != "" and self.btn7.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn1.text()} player won !")
            self.btn1.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn4.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn7.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn1.text() == self.btn5.text() and self.btn1.text() == self.btn9.text() and self.btn1.text() != "" and self.btn5.text() != "" and self.btn9.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn1.text()} player won !")
            self.btn1.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn5.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn9.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn4.text() == self.btn5.text() and self.btn4.text() == self.btn6.text() and self.btn4.text() != "" and self.btn5.text() != "" and self.btn6.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn4.text()} player won !")
            self.btn4.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn5.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn6.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn7.text() == self.btn8.text() and self.btn7.text() == self.btn9.text() and self.btn7.text() != "" and self.btn8.text() != "" and self.btn9.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn7.text()} player won !")
            self.btnn.show()
            self.btn7.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn8.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn9.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn2.text() == self.btn5.text() and self.btn2.text() == self.btn8.text() and self.btn2.text() != "" and self.btn5.text() != "" and self.btn8.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn2.text()} player won !")
            self.btnn.setGeometry(245, 35, 100, 50)
            self.btn2.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn5.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn8.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn3.text() == self.btn6.text() and self.btn3.text() == self.btn9.text() and self.btn3.text() != "" and self.btn6.text() != "" and self.btn9.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn3.text()} player won !")
            self.btn3.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn6.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn9.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            
        if self.btn3.text() == self.btn5.text() and self.btn3.text() == self.btn7.text() and self.btn3.text() != "" and self.btn5.text() != "" and self.btn7.text() != "":
            self.disabled()
            self.btnn.setText("Game Over !")
            self.btnn2.setText(f"{self.btn3.text()} player won !")
            self.btn3.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn5.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
            self.btn7.setStyleSheet("""
                background-color: rgb(153, 163, 164);""")
        
            

    def new_game_click(self):
        Tiktac.__count = 0
        for i in self.__buttons:
            i.setText("")
            i.setEnabled(True)
            i.setStyleSheet("""
            border-style: solid;
            border-width: 8px;
            border-color: black;
            background-color:  rgb(70, 130, 180)""")
            
        self.btnn.setText("")
        self.btnn2.setText("")
            
    def disabled(self):
        for i in self.__buttons:
            i.setDisabled(True)
            
    def and_game_click(self):
        msg = QMessageBox(self)
        msg.setFont(QFont("Poor Richard",20))
        msg.setWindowTitle("Information ")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox. Yes  |  QMessageBox. No)
        msg.setText("Siz o'yindan chiqmoqchimisiz? ")
        msg.buttonClicked.connect(self.check_quit)
        msg.show()
    
    def check_quit(self,x):
        if x.text() == "&Yes":
            exit()
        else: 
            print(x.text())
        


app = QApplication([])
main = Tiktac()
main.show()
sys.exit(app.exec_())