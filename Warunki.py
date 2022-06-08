from functools import partial
from PyQt5.QtGui import QPixmap

from Komunikat import Dialog

#Metoda warunkowa
def _Checker(self, litera:"litera", miejsce:"Miejsce litery")->"Warunki wciśnięcia przycisków":
    """
    Pierwszy if sprawdza czy litera znajduje się w tablicy liter słowa odgadywanego
    Drugi if sprawdza czy litera nie znajduje się w tablicy liter słowa odgadywanego
    Trzeci if sprawdza czy gracz wcisnął 6 błędnych liter i wywołuje okno dialogowe końca gry
    elif sprawdza czy gracz odgadł całe słowo i wywołuje okno dialogowe końca gry
    """
    updater=0
    if litera not in self.guessed:
        for i in range (self.dlugosc):
            if self.literki[i] == litera:
                updater=1                  #Obejście drugiego ifa
                self.guessed.append(litera)#Dodanie litery do listy zgadniętych
                self.przyciski[miejsce].setStyleSheet(
                "border: 2px solid '#80c1ff';" + 
	            "background-color: '#c6ff91';" +
	            "font-size: 25px;" +
	            "padding-left: 1px;" +
                "border-radius: 15px;" +
	            "color: 'grey';"
                )
                self.labelki[i].setText(litera)#Pokazanie liter w słowie zgadywanym
    if (updater == 0) and (litera not in self.literki):
        if litera not in self.checked:
            self.checked.append(litera)#Dodanie litery do listy błędnych
            self.update += 1           #Aktualizacja stanu wisielca
            self.przyciski[miejsce].setStyleSheet(
            "border: 2px solid '#80c1ff';" + 
	        "background-color: '#fa7883';" +
	        "font-size: 25px;" +
	        "padding-left: 1px;" +
            "border-radius: 15px;" +
	        "color: 'grey';"
            )
        self.wisiak.setPixmap(QPixmap(self.wisielec[self.update]))
        #PRZEGRANA
    if self.update >= 6:
        dial = Dialog()
        dial.exec_() #Odpalanie 2 okienka
        if dial.result()==1:
            plik=str(dial.plikname.text())
            if plik == "":
                plik = "wyniki" 
            with open(plik + '.txt', 'a') as file:
                file.write(
                    "Przegrana w wisielca. \n" +
                    "Słowo : " + self.haslo + "\n" +
                    "Następnym razem pójdzie Ci lepiej! \n"
                    )
            self.app.quit()
        else:
            self.app.quit()
        #WYGRANA
    elif len(self.guessed) == len(self.literki):
        self.wisiak.setPixmap(QPixmap("pngs/wisiakwygrana.png"))
        dial = Dialog()
        dial.exec_() #Odpalanie 2 okienka
        if dial.result()==1:
            plik=str(dial.plikname.text())
            if plik == "":
                plik = "wyniki" 
            with open(plik + '.txt', 'a') as file:
                file.write(
                    "Wygrana w wisielca. \n" +
                    "Słowo : " + str(self.haslo) + "\n" +
                    "Liczba nie trafionych liter: " + 
                    str(len(self.checked)) + "\n"
                    )
            self.app.quit()
        else:
            self.app.quit()
    #print(self.update)

