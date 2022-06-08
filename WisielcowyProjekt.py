from Gra import _gra
from Warunki import _Checker
from init import _init
import win32gui, win32con

class Start:
    """
    Główna klasa gry
    Wywołuje konstruktor w którym znajduje się pierwsze okienko z wyborem słowa
    """
    def __init__(self):
        super().__init__()
        _init(self)#Konstruktor

    #Start gry
    def gra(self)->"Tworzy okienko gry":
        _gra(self)
    #Wyjście
    def wyjscie(self)->"Wychodzi z programu":
        self.app.quit()
    #Metoda z warunkami
    def Checker(self, litera:"Label z literą", miejsce:"Miejsce litery")-> "Warunki wciśnięcia przycisku":
        _Checker(self, litera, miejsce)

win=Start()
