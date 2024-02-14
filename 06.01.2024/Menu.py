from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu")
        self.setMinimumSize(1920, 1080)
        self.setMaximumSize(1920, 1080)
        self.setStyleSheet("""background-color:  #9696FF""")

        oyna = QWidget(self)
        oyna.setWindowTitle("Menu")
        oyna.setGeometry(20, 25, 500, 440)
        oyna.setStyleSheet(
            """background-color: #3C3CC7;
                                         border-radius: 22px"""
        )

        vb = QVBoxLayout()
        btn = QPushButton(self)
        btn.setGeometry(120, 25, 300, 30)
        btn.setFont(QFont("Calibri", 15, weight=100))
        btn.setText("OVQATLAR !")
        btn.setStyleSheet(
            """background-color: #3C3CC7;
                                        border-radius: 22px"""
        )

        check1 = QCheckBox(
            "1_Osh:                                        (25.000 so'm)"
        )
        check1.setFont(QFont("Calibri", 15, weight=60))
        check1.stateChanged.connect(lambda: self.backand(1))
        check2 = QCheckBox("2_Manti:                                     (35.000 so'm)")
        check2.setFont(QFont("Calibri", 15, weight=60))
        check2.stateChanged.connect(lambda: self.backand(2))
        check3 = QCheckBox("3_Somsa                                     (10.000 so'm)")
        check3.setFont(QFont("Calibri", 15, weight=60))
        check3.stateChanged.connect(lambda: self.backand(3))
        check4 = QCheckBox("4_Barak                                      (20.000 so'm)")
        check4.setFont(QFont("Calibri", 15, weight=60))
        check4.stateChanged.connect(lambda: self.backand(4))
        check5 = QCheckBox("5_Norin                                      (17.000 so'm)")
        check5.setFont(QFont("Calibri", 15, weight=60))
        check5.stateChanged.connect(lambda: self.backand(5))
        check6 = QCheckBox("6_Kabob                                     (70.000 so'm)")
        check6.setFont(QFont("Calibri", 15, weight=60))
        check6.stateChanged.connect(lambda: self.backand(6))

        vb.addWidget(check1)
        vb.addWidget(check2)
        vb.addWidget(check3)
        vb.addWidget(check4)
        vb.addWidget(check5)
        vb.addWidget(check6)
        oyna.setLayout(vb)

        oyna2 = QWidget(self)
        oyna2.setWindowTitle("Menu")
        oyna2.setGeometry(595, 25, 580, 440)
        oyna2.setStyleSheet(
            """background-color: #3C3CC7;
                                         border-radius: 22px"""
        )

        vb2 = QVBoxLayout()
        btn2 = QPushButton(self)
        btn2.setGeometry(730, 25, 300, 30)
        btn2.setFont(QFont("Calibri", 15, weight=100))
        btn2.setStyleSheet(
            """background-color: #3C3CC7;
                                         border-radius: 22px"""
        )
        btn2.setText("ICHIMLIKLAR !")

        check7 = QCheckBox(
            "1_Choy(ko'k):                                          (10.000 so'm)"
        )
        check7.setFont(QFont("Calibri", 15, weight=60))
        check7.stateChanged.connect(lambda: self.backand(7))
        check8 = QCheckBox(
            "2_CocaCola:                                            (15.000 so'm)"
        )
        check8.setFont(QFont("Calibri", 15, weight=60))
        check8.stateChanged.connect(lambda: self.backand(8))
        check9 = QCheckBox(
            "3_Fanta:                                                   (10.000 so'm)"
        )
        check9.setFont(QFont("Calibri", 15, weight=60))
        check9.stateChanged.connect(lambda: self.backand(9))
        check10 = QCheckBox(
            "4_Pepsi:                                                   (13.000 so'm)"
        )
        check10.setFont(QFont("Calibri", 15, weight=60))
        check10.stateChanged.connect(lambda: self.backand(10))
        check11 = QCheckBox(
            "5_Sharbat:                                               (20.000 so'm)"
        )
        check11.setFont(QFont("Calibri", 15, weight=60))
        check11.stateChanged.connect(lambda: self.backand(11))
        check12 = QCheckBox(
            "6_Suv:                                                      (5.000 so'm)"
        )
        check12.setFont(QFont("Calibri", 15, weight=60))
        check12.stateChanged.connect(lambda: self.backand(12))

        vb2.addWidget(check7)
        vb2.addWidget(check8)
        vb2.addWidget(check9)
        vb2.addWidget(check10)
        vb2.addWidget(check11)
        vb2.addWidget(check12)
        oyna2.setLayout(vb2)

        oyna3 = QWidget(self)
        btn3 = QPushButton(self)
        btn3.setGeometry(1380, 25, 300, 30)
        btn3.setFont(QFont("Calibri", 15, weight=100))
        btn3.setStyleSheet(
            """background-color: #3C3CC7;
                                         border-radius: 22px"""
        )
        btn3.setText("SHIRINLIKLAR !")

        oyna3.setWindowTitle("Menu")
        oyna3.setGeometry(1250, 25, 580, 440)
        oyna3.setStyleSheet(
            """background-color: #3C3CC7;
                                         border-radius: 22px"""
        )

        vb3 = QVBoxLayout()
        check13 = QCheckBox(
            "1_To'rt(choco):                                       (30.000 so'm)"
        )
        check13.setFont(QFont("Calibri", 15, weight=60))
        check13.stateChanged.connect(lambda: self.backand(13))
        check14 = QCheckBox(
            "2_Chocolad:                                            (25.000 so'm)"
        )
        check14.setFont(QFont("Calibri", 15, weight=60))
        check14.stateChanged.connect(lambda: self.backand(14))
        check15 = QCheckBox(
            "3_To'rt(Qaymoqli):                                 (40.000 so'm)"
        )
        check15.setFont(QFont("Calibri", 15, weight=60))
        check15.stateChanged.connect(lambda: self.backand(15))
        check16 = QCheckBox(
            "4_AlpenGold:                                           (8.000 so'm)"
        )
        check16.setFont(QFont("Calibri", 15, weight=60))
        check16.stateChanged.connect(lambda: self.backand(16))
        check17 = QCheckBox(
            "5_Dark Choco:                                         (15.000 so'm)"
        )
        check17.setFont(QFont("Calibri", 15, weight=60))
        check17.stateChanged.connect(lambda: self.backand(17))
        check18 = QCheckBox(
            "6_Pirok:                                                    (50.000 so'm)"
        )
        check18.setFont(QFont("Calibri", 15, weight=60))
        check18.stateChanged.connect(lambda: self.backand(18))

        vb3.addWidget(check13)
        vb3.addWidget(check14)
        vb3.addWidget(check15)
        vb3.addWidget(check16)
        vb3.addWidget(check17)
        vb3.addWidget(check18)
        oyna3.setLayout(vb3)

        self.bt = QPushButton(self)
        self.bt.setGeometry(550, 600, 700, 40)
        self.bt.setFont(QFont("Calibri", 20, weight=100))
        self.bt.setText("<< TASHRIF UCHUN TASHAKKUR !!! >>")
        self.bt.setStyleSheet(
            """background-color: #9696FF;
                                     border-radius: 10px;"""
        )
        self.bt.clicked.connect(lambda: self.thenku())

        # CHEK SECTION  !

        self.chek_oyna = QLabel(self)
        self.chek_oyna.setFont(QFont("Calibri", 17, weight=80))
        self.chek_oyna.setGeometry(1400, 650, 500, 440)
        self.chek_oyna.setStyleSheet(
            """background-color: # 8263DC;
                                                        border-radius: 22px;"""
        )

        self.show()

        self.sum = 0

    def backand(self, text):
        if text == 1:
            self.sum += 25000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 2:
            self.sum += 35000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 3:
            self.sum += 10000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 4:
            self.sum += 20000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 5:
            self.sum += 17000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 6:
            self.sum += 70000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 7:
            self.sum += 10000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 8:
            self.sum += 15000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 9:
            self.sum += 10000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 10:
            self.sum += 13000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 11:
            self.sum += 20000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 12:
            self.sum += 5000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 13:
            self.sum += 30000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 14:
            self.sum += 25000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 15:
            self.sum += 40000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 16:
            self.sum += 8000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 17:
            self.sum += 15000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

        elif text == 18:
            self.sum += 50000
            self.chek_oyna.setText(f"UMUMIY XISOB_: {str(self.sum)} so'm")

    def thenku(self):
        btn4 = QPushButton(self)
        btn4.setGeometry(10, 10, 110, 200)
        btn4.setFont(QFont("Calibri", 10, weight=100))
        btn4.setStyleSheet("""background-color: #580000""")
        btn4.setText("HARIDINGIZ UCHUN TASHAKKUR !")


app = QApplication([])
res = Menu()
sys.exit(app.exec_())
