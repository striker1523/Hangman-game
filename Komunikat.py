import PyQt5.QtWidgets as pq
from PyQt5.QtGui import QIcon

class Dialog(pq.QDialog):
    """
    Dialog końca gry, umożliwia zapis wyniku do pliku tekstowego z nazwą podaną przez gracza
    """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Koniec gry")
        self.setStyleSheet("background: #afcae3;")
        self.setWindowIcon(QIcon("pngs/ikonka.png"))

        self.label=pq.QLabel('Zapisz swój wynik!')
        self.label2=pq.QLabel('Nazwa pliku: ')
        self.plikname=pq.QLineEdit()
        self.button=pq.QPushButton('Zapisz')
        self.button2=pq.QPushButton('Wyjdź')

        self.Dialogstyl=(
        "border: 2px solid '#80c1ff';" + 
	    "background-color: '#cfd9e3';" +
	    "font-size: 25px;" +
	    "padding-left: 1px;" +
        "border-radius: 15px;" +
	    "color: 'grey';"
        )
        self.label.setStyleSheet("font-size: 25px; color: 'grey';")
        self.label2.setStyleSheet(self.Dialogstyl)
        self.plikname.setStyleSheet(self.Dialogstyl + "background-color: '#e1f8fc';")
        self.button.setStyleSheet(self.Dialogstyl)
        self.button2.setStyleSheet(self.Dialogstyl)

        self.button.clicked.connect(self.accept)
        self.button2.clicked.connect(self.reject)
        
        self.diallay = pq.QGridLayout() 
        self.diallay.addWidget(self.label, 0, 1, 1, 3)
        self.diallay.addWidget(self.label2,1,0,1,2)
        self.diallay.addWidget(self.plikname,1,2,1,3)
        self.diallay.addWidget(self.button,2,0)
        self.diallay.addWidget(self.button2,2,4)
        self.setLayout(self.diallay)