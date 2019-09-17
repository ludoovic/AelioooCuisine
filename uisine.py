import requests
import sys
import json
from PySide2.QtWidgets import (
    QLabel, QApplication, QMainWindow, QTableWidget, QSizePolicy)
from PySide2.QtCore import QTimer, Qt, QTime
from ui_cuisinexavier import Ui_MainWindow

json = "aeliooo.s3db"


class Repertoire(QMainWindow):

    def __init__(self, parent=None):
        super(Repertoire, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(5000)
        # connect timeout vers fonction Refresh
        self.timer.timeout.connect(self.refreshData)
        self.timer.start()

        # self.lwListeNoms.itemClicked.connect(self.userSelected)
        # self.pbAjouter.clicked.connect(self.addUser)
        # self.pbModifier.clicked.connect(self.modifyUser)
        # self.updateTabletWidget()

    def refreshData(self):
        req = requests.get('http://localhost:5000/cuisine')
        retour = json.loads(req.text)
        print(retour)

    def updatetablewidget(self):  # Nouvelles commandes (emplacement)
        self.lwListeNomsAdresse.clear()
        for fiche in self.json["repertoire"]:
            self.lwListeNomsAdresse.addItem(fiche["nom", "adresse"])
            retour = QTableWidget(self, "Ajout Client", "Nom:", "Adresse")
            if retour[0] == "":
                return

    def updatetablewidget2(self):  # commandes en cours
        self.lwListeNomsAdresse.clear()
        for fiche in self.json["repertoire"]:
            self.lwListeNomsAdresse.addItem(fiche["nom", "adresse"])
            retour = QTableWidget(self, "Ajout Client", "Nom:", "Adresse")
        if retour[0] == "":
            return

        # A completer

        # def modifyUser(self):

        # def userSelected(self):

    def lireJSON(self, fileName):
        with open(fileName) as json_file:
            json = json.load(json_file)
            return json
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rep = Repertoire()
    rep.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
