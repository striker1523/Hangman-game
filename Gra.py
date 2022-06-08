from functools import partial
from PyQt5 import QtCore
import PyQt5.QtWidgets as pq
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QRegExp
import random

#Metody
#Start gry
def _gra(self)->"Tworzy okienko gry":
    """
    Główne okno gry
    Pokazuje aktualny stan wisielca
    Tworzy i pokazuje przyciski do zgadywania liter
    Odpowiednio każde kliknięcie przycisku przekazuje dane do metody warunkowej
    """
    self.window.hide()
    #Inicjalizacja okna
    self.game=pq.QApplication([])
    self.okno=pq.QWidget()
    self.okno.setFixedSize(800,500)
    self.okno.setWindowTitle("Grasz w wisielca")
    self.okno.setStyleSheet("background: #afcae3;")
    self.okno.setWindowIcon(QIcon("pngs/ikonka.png"))
                                                        #print(_gra.__doc__)
                                                        #help(_gra)
    #Haslo
    haslo(self)

    #Wisielec
    wisielec(self)

    #Widgety
    widgets(self)

    #Widgety - style
    widgetsstyle(self)
        
    #Layout
    lay(self)

    #Wykonanie
        #Wykonanie - Wykonanie przycisków
    wyk_lit = 97
    for i in range (26):
        self.przyciski[i].clicked.connect(partial(self.Checker, chr(wyk_lit), i))
        wyk_lit+=1
        #Wykonanie - Wykonanie wyjscia
    self.wyjdz2.clicked.connect(self.wyjscie)
    #Exec
    self.okno.show()



def haslo(self):
    """
    Ładuje hasło podane przez użytkownika, lub losuje je z puli
    """
    self.has = ["zut", "python", "uczelnia",\
                "uniwersytet", "program", "profesor",\
                "algorytm", "szczecin", "komputer"]
    if (self.slowo.text() == ''):
        self.haslo = random.choice(self.has)
    else:
        self.haslo = str(self.slowo.text())
    self.literki = []
    self.literki[:] = self.haslo
    self.dlugosc = len(self.literki)



def wisielec(self):
    """
    Ładuje obrazki i rysuje wisielca w głównym oknie gry
    """
        #Wisielec - Ładowanie obrazków
    self.wisielec = []
    for i in range (7):
        self.stage = QPixmap("pngs/wisiak" + str(i) + ".png")
        self.wisielec.append(self.stage)
        #Wisielec - GŁOWNY WISIELEC
    self.wisiak = pq.QLabel()
    self.wisiak.setPixmap(QPixmap(self.wisielec[self.update]))
    self.wisiak.setAlignment(QtCore.Qt.AlignCenter)
    self.wisiak.setStyleSheet("margin-bottom: 1px;")



def widgets(self):
    """
    Tworzy widgety w oknie gry (przyciski, labele)
    """
        #Widgety - widgety przycisków
    self.przyciski = []
    for i in range (97,123):
        self.przyciski.append(pq.QPushButton(chr(i)))
    self.wyjdz2 = pq.QPushButton('Wyjdź')
        #Shortcuty - przyciskow
    self.shrtct = 0
    for i in range (97,123):
        self.przyciski[self.shrtct].setShortcut(chr(i))
        self.shrtct+=1
        #Widgety - widgety labeli(hasła)
    self.labelki = []
    for i in range (self.dlugosc):
        self.labelki.append(pq.QLabel('_ '))



def widgetsstyle(self):
    """
    Nadaje style widgetom stworzonym w metodzie widgets
    """
        #Widgety - Style
    self.PrzyciskStyl=(
    "border: 2px solid '#80c1ff';" + 
	"background-color: '#cfd9e3';" +
	"font-size: 25px;" +
	"padding-left: 1px;" +
    "border-radius: 15px;" +
	"color: 'grey';"
    )
    for i in range (0,26):
        self.przyciski[i].setStyleSheet(self.PrzyciskStyl)

    self.wyjdz2.setStyleSheet(self.Styl)

    self.labelkiStyl=("font-size:25px;")
    for i in range (self.dlugosc):
        self.labelki[i].setStyleSheet(self.labelkiStyl)



def lay(self):
    """
    Tworzy layout z widgetów w metodzie widgets
    """
    self.grid2 = pq.QGridLayout() 
    self.grid2.addWidget(self.wisiak,0,0,1,13)
        #Layout - Layout przycisków
    a=0
    for i in range (3,5):
        for j in range (0,13):
            self.grid2.addWidget(self.przyciski[a],i,j)
            a+=1
        #Layout - Layout Labelek (hasła)
    a=0
    for i in range (1, self.dlugosc+1):
        self.grid2.addWidget(self.labelki[a],2,i)
        a+=1

    self.grid2.addWidget(self.wyjdz2,5,5,1,3)
    self.okno.setLayout(self.grid2)