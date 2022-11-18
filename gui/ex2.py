import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
)
from PyQt5.QtCore import QCoreApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        # Labels
        self.__LabelTemp = QLabel("Degrés Celsuis")
        self.__LabelC = QLabel("°C")
        self.__LabelK = QLabel("°K")
        self.__LabelConversion = QLabel("Degrés Kelvin")

        # LineEdits
        self.__LineEditC = QLineEdit("")
        self.__LineEditK = QLineEdit("")

        # Buttons
        self.__ButtonConvertir = QPushButton("Convertir")
        self.__ButtonAide = QPushButton("?")

        # ComboBox
        self.__ComboChoix = QComboBox()
        self.__ComboChoix.addItems(["°C -> °K", "°K -> °C"])


        ### --- PLACEMENTS --- ###
        # Première Ligne
        grid.addWidget(self.__LabelTemp, 0, 0)
        grid.addWidget(self.__LineEditC, 0, 1)
        grid.addWidget(self.__LabelC, 0, 2)

        # Deuxième Ligne
        grid.addWidget(self.__ButtonConvertir, 1, 1)
        grid.addWidget(self.__ComboChoix, 1, 2)

        # Troisième Ligne
        grid.addWidget(self.__LabelConversion, 2, 0)
        grid.addWidget(self.__LineEditK, 2, 1)
        grid.addWidget(self.__LabelK, 2, 2)

        # Quatrième Ligne
        grid.addWidget(self.__ButtonAide, 3, 2)

        # Ajouter les composants au grid ayout
        self.__ButtonConvertir.clicked.connect(self._actionConversion)
        self.__ButtonAide.clicked.connect(self._actionAide)

        self.__LineEditK.setEnabled(False)
        self.__ComboChoix.currentIndexChanged.connect(self._actionChangement)
        # self.__quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("Conversions")

            
    def InfoBox(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.exec()


    def _actionConversion(self):
        match self.__ComboChoix.currentIndex():
            case 0: # C vers K
                try:
                    tempk = float(self.__LineEditC.text()) + 273.15
                except ValueError:
                    self.InfoBox("Ne pas mettre de texte!")
                else:
                    if tempk <= 0:
                        self.__LineEditK.setText(str(round(tempk, 2)))
                    else:
                        self.InfoBox("Impossible d'être en dessous du zéro absolu!")
            case 1: # K vers C
                try:
                    tempc = float(self.__LineEditK.text()) - 273.15
                except ValueError:
                    self.InfoBox("Ne pas mettre de texte!")
                else:
                    if tempc >= -273.15:
                        self.__LineEditC.setText(str(round(tempc, 2)))
                    else:
                        self.InfoBox("Impossible d'être en dessous du zéro absolu!")
                    

    def _actionChangement(self):
        match self.__ComboChoix.currentIndex():
            case 0:
                self.__LineEditK.setEnabled(False)
                self.__LineEditC.setEnabled(True)
            case 1:
                self.__LineEditK.setEnabled(True)
                self.__LineEditC.setEnabled(False)

    def _actionAide(self):
        self.InfoBox("Permet de convertir un nombre soit de Kelvin vers Celsuis, soit de Celsuis vers Kelvin")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
