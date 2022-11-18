import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.__grid = QGridLayout()
        widget.setLayout(self.__grid)

        self.__lab = QLabel("Saisir votre nom")
        self.__text = QLineEdit("")
        self.__ok = QPushButton("Ok")
        self.__name = QLabel("")
        self.__quit = QPushButton("Quitter")

        #  TODO: mettre un widget dans le grid
        self.__grid.addWidget(self.__lab, 0, 0)
        self.__grid.addWidget(self.__text, 1, 0)
        self.__grid.addWidget(self.__ok, 2, 0)
        self.__grid.addWidget(self.__name, 3, 0)
        self.__grid.addWidget(self.__quit, 4, 0)


        # Ajouter les composants au grid ayout
        self.__ok.clicked.connect(self._actionOk)
        self.__quit.clicked.connect(self._actionQuitter)
        self.setWindowTitle("Une première fenêtre")

    def _actionOk(self):
        self.__name.setText(f"Bonjour {self.__text.text()}!")
        print(self.__text.text())


    def _actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()