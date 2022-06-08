from PyQt5 import QtCore
import PyQt5.QtWidgets as pq
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator
from PyQt5.QtCore import QRegExp

def _init(self)->"Konstruktor":
    """
    Tworzy okienko startowe, w którym użytkownik wpisuje słowo do gry
    Posiada przyciski odpowiadające za wywołanie metody gra, oraz wyjścia z gry
    """
    self.app=pq.QApplication([])
    self.window=pq.QWidget()
    self.window.setFixedSize(500,350)
    self.window.setWindowTitle("ZUT Wisielec")
    self.window.setStyleSheet("background: #afcae3;")
    self.window.setWindowIcon(QIcon("pngs/ikonka.png"))

#Logo
    self.image = QPixmap("pngs/wisiakstart.png")
    self.logo = pq.QLabel()
    self.logo.setPixmap(self.image)
    self.logo.setAlignment(QtCore.Qt.AlignCenter)
    self.logo.setStyleSheet("margin-bottom: 1px;")
#Zmienne
    self.update = 0     #Zmiana stanu wisielca (obrazu)
    self.checked = []   #Nieodgadnięte literki
    self.guessed = []   #Odgadnięte literki

#Funkcje
    #Funkcje - Walidator
    valid=QRegExpValidator(QRegExp(r'[a-z]{0,12}$'))

    #Funkcje - Widgety
    self.graj = pq.QPushButton('Graj!')
    self.wyjdz = pq.QPushButton('Wyjdź')
    self.label = pq.QLabel('Podaj słówko')
    self.slowo = pq.QLineEdit()
    self.slowo.setPlaceholderText("Jeśli puste, słowo zostanie wylosowane")
    self.slowo.setValidator(valid)

    #Funkcje - Style
    self.Styl=(
    "border: 2px solid '#80c1ff';" + 
	"background-color: '#cfd9e3';" +
	"font-size: 25px;" +
	"padding-left: 1px;" +
    "border-radius: 15px;" +
	"color: 'grey';"
    )
    self.graj.setStyleSheet(self.Styl)
    self.graj.setShortcut("Return")
    self.wyjdz.setStyleSheet(self.Styl)
    self.wyjdz.setShortcut("Escape")
    self.label.setStyleSheet(self.Styl)
    self.slowo.setStyleSheet(self.Styl + "background-color: '#e1f8fc';")

    #Funkcje - Wykonanie
    self.graj.clicked.connect(self.gra)
    self.wyjdz.clicked.connect(self.wyjscie)

#Layout
    self.grid = pq.QGridLayout() 
    self.grid.addWidget(self.logo,0,0,1,3)
    self.grid.addWidget(self.label,1,1,1,1)
    self.grid.addWidget(self.slowo,2,0,1,3)
    self.grid.addWidget(self.graj,3,0)
    self.grid.addWidget(self.wyjdz,3,2)
    self.window.setLayout(self.grid)

#exec
    self.window.show()
    self.app.exec_()

