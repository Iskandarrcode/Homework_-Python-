from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Kalkulyator:
    def __init__(self):
        super().__init__()

        self.forma = QWidget()
        self.forma.setWindowTitle("Kalkulyator")
        self.forma.resize(440, 700)
        self.forma.setStyleSheet("""background-color: black;""")

        # Label settings
        self.lbl = QLabel(self.forma)
        self.lbl.setFont(QFont("Calibri", 40))
        self.lbl.setGeometry(30, 40, 450, 50)
        self.lbl.setStyleSheet("""color: white;""")
        self.lbl.setText("0")

        # Battom settings
        self.bt1 = QPushButton(self.forma)
        self.bt1.setGeometry(30, 180, 80, 80)
        self.bt1.setStyleSheet(
            """ background-color: #A5A5A5;
                                             border-radius: 40px;"""
        )
        self.bt1.setFont(QFont("Calibri", 20, weight=100))
        self.bt1.setText("AC")
        self.bt1.clicked.connect(lambda: self.enterAC())

        self.bt2 = QPushButton(self.forma)
        self.bt2.setGeometry(130, 180, 80, 80)
        self.bt2.setStyleSheet(
            """ background-color: #A5A5A5;
                                             border-radius: 40px;"""
        )
        self.bt2.setFont(QFont("Calibri", 20, weight=100))
        self.bt2.setText("+/-")
        self.bt2.clicked.connect(lambda: self.enter_minus())

        self.bt3 = QPushButton(self.forma)
        self.bt3.setGeometry(230, 180, 80, 80)
        self.bt3.setStyleSheet(
            """ background-color: #A5A5A5;
                                             border-radius: 40px;"""
        )
        self.bt3.setFont(QFont("Calibri", 20, weight=100))
        self.bt3.setText("%")
        self.bt3.clicked.connect(lambda: self.enter_boliw())

        self.bt4 = QPushButton(self.forma)
        self.bt4.setGeometry(330, 180, 80, 80)
        self.bt4.setStyleSheet(
            """ background-color: orange;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt4.setFont(QFont("Calibri", 20, weight=100))
        self.bt4.setText("÷")
        self.bt4.clicked.connect(lambda: self.enter_amal("÷"))

        self.bt5 = QPushButton(self.forma)
        self.bt5.setGeometry(30, 280, 80, 80)
        self.bt5.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;
                                             color: white;"""
        )
        self.bt5.setFont(QFont("Calibri", 20, weight=100))
        self.bt5.setText("7")
        self.bt5.clicked.connect(lambda: self.enter_amal("7"))

        self.bt6 = QPushButton(self.forma)
        self.bt6.setGeometry(130, 280, 80, 80)
        self.bt6.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt6.setFont(QFont("Calibri", 20, weight=100))
        self.bt6.setText("8")
        self.bt6.clicked.connect(lambda: self.enter_amal("8"))

        self.bt7 = QPushButton(self.forma)
        self.bt7.setGeometry(230, 280, 80, 80)
        self.bt7.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt7.setFont(QFont("Calibri", 20, weight=100))
        self.bt7.setText("9")
        self.bt7.clicked.connect(lambda: self.enter_amal("9"))

        self.bt8 = QPushButton(self.forma)
        self.bt8.setGeometry(330, 280, 80, 80)
        self.bt8.setStyleSheet(
            """ background-color: orange;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt8.setFont(QFont("Calibri", 20, weight=100))
        self.bt8.setText("×")
        self.bt8.clicked.connect(lambda: self.enter_amal("×"))

        self.bt9 = QPushButton(self.forma)
        self.bt9.setGeometry(30, 380, 80, 80)
        self.bt9.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt9.setFont(QFont("Calibri", 20, weight=100))
        self.bt9.setText("4")
        self.bt9.clicked.connect(lambda: self.enter_amal("4"))

        self.bt10 = QPushButton(self.forma)
        self.bt10.setGeometry(130, 380, 80, 80)
        self.bt10.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt10.setFont(QFont("Calibri", 20, weight=100))
        self.bt10.setText("5")
        self.bt10.clicked.connect(lambda: self.enter_amal("5"))

        self.bt11 = QPushButton(self.forma)
        self.bt11.setGeometry(230, 380, 80, 80)
        self.bt11.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt11.setFont(QFont("Calibri", 20, weight=100))
        self.bt11.setText("6")
        self.bt11.clicked.connect(lambda: self.enter_amal("6"))

        self.bt12 = QPushButton(self.forma)
        self.bt12.setGeometry(330, 380, 80, 80)
        self.bt12.setStyleSheet(
            """ background-color: orange;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt12.setFont(QFont("Calibri", 20, weight=100))
        self.bt12.setText("-")
        self.bt12.clicked.connect(lambda: self.enter_amal("-"))

        self.bt13 = QPushButton(self.forma)
        self.bt13.setGeometry(30, 480, 80, 80)
        self.bt13.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt13.setFont(QFont("Calibri", 20, weight=100))
        self.bt13.setText("1")
        self.bt13.clicked.connect(lambda: self.enter_amal("1"))

        self.bt14 = QPushButton(self.forma)
        self.bt14.setGeometry(130, 480, 80, 80)
        self.bt14.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt14.setFont(QFont("Calibri", 20, weight=100))
        self.bt14.setText("2")
        self.bt14.clicked.connect(lambda: self.enter_amal("2"))

        self.bt15 = QPushButton(self.forma)
        self.bt15.setGeometry(230, 480, 80, 80)
        self.bt15.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt15.setFont(QFont("Calibri", 20, weight=100))
        self.bt15.setText("3")
        self.bt15.clicked.connect(lambda: self.enter_amal("3"))

        self.bt16 = QPushButton(self.forma)
        self.bt16.setGeometry(330, 480, 80, 80)
        self.bt16.setStyleSheet(
            """ background-color: orange;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt16.setFont(QFont("Calibri", 20, weight=100))
        self.bt16.setText("+")
        self.bt16.clicked.connect(lambda: self.enter_amal("+"))

        self.bt17 = QPushButton(self.forma)
        self.bt17.setGeometry(30, 580, 180, 80)
        self.bt17.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt17.setFont(QFont("Calibri", 20, weight=100))
        self.bt17.setText("0")
        self.bt17.clicked.connect(lambda: self.enter_amal("0"))

        self.bt18 = QPushButton(self.forma)
        self.bt18.setGeometry(230, 580, 80, 80)
        self.bt18.setStyleSheet(
            """ background-color: #3D3D3D;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt18.setFont(QFont("Calibri", 20, weight=100))
        self.bt18.setText(".")
        self.bt18.clicked.connect(lambda: self.enter_amal(","))

        self.bt19 = QPushButton(self.forma)
        self.bt19.setGeometry(330, 580, 80, 80)
        self.bt19.setStyleSheet(
            """ background-color: orange;
                                             border-radius: 40px;
                                             color: white;"""
        )
        self.bt19.setFont(QFont("Calibri", 20, weight=100))
        self.bt19.setText("=")
        self.bt19.clicked.connect(lambda: self.xisobla())

        self.forma.show()

    def enterAC(self):
        self.lbl.setText("0")

    def enter_minus(self):
        self.lbl.setText(str(-1 * int(self.lbl.text())))

    def enter_boliw(self):
        self.lbl.setText(str(int(self.lbl.text()) / 100))

    def enter_amal(self, num):
        if self.lbl.text() == "0":
            self.lbl.setText(num)
        else:
            self.lbl.setText(self.lbl.text() + num)

    def xisobla(self):
        res = self.lbl.text()
        res = res.replace("÷", "/")
        res = res.replace("×", "*")
        res = res.replace("-", "-")
        res = res.replace("+", "+")
        self.lbl.setText(str(eval(res)))


app = QApplication([])
res = Kalkulyator()
sys.exit(app.exec_())
