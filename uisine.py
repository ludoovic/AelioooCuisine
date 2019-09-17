import requests
import sys
import json
from PySide2.QtWidgets import (
    QLabel, QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QSizePolicy)
from PySide2.QtCore import QTimer, Qt, QTime
from ui_cuisinexavier import Ui_MainWindow


class cuisine(QMainWindow):

    def __init__(self, parent=None):
        super(cuisine, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer = QTimer()
        self.timer.setInterval(5000)

        # connect timeout vers fonction Refresh
        self.timer.timeout.connect(self.refreshData)
        self.timer.start()

        # cellClicked.connect permet de changer d'Etat 1 à 2
        self.ui.tableWidget.cellClicked.connect(self.itemNouveauClicked)

    def itemNouveauClicked(self, rowClicked, colClicked):
        print('click', rowClicked, colClicked)

    def refreshData(self):
        req = requests.get('http://localhost:5000/cuisine')
        retour = req.json()
        self.updateTabletWidget(retour)
        self.updateTabletWidget2(retour)

    def updateTabletWidget(self, dataJson):  # Nouvelles commandes (emplacement)
        self.ui.tableWidget.clear()

        header = ["id Commandes", "Noms Clients"]
        self.ui.tableWidget.setColumnCount(len(header))
        self.ui.tableWidget.setHorizontalHeaderLabels(header)

        cpt = 0
        for fiche in dataJson["commandes"]:
            if fiche["etat"] == 1:
                self.ui.tableWidget.setRowCount(cpt+1)
                self.ui.tableWidget.setItem(cpt, 0, itemID)
                self.ui.tableWidget.setItem(cpt, 1, itemNom)
                itemID = QTableWidgetItem(str(fiche["id"]))
                itemNom = QTableWidgetItem(fiche["nom"])

                cpt = cpt+1

    def updateTabletWidget2(self):  # commandes en cours
        self.ui.tableWidget2.clear()
        self.ui.tableWidget2.setRowCount(0)
        self.ui.tableWidget2.setColumnCount(2)

        cpt = 0
        for fiche in dataJson["commandes"]:
            if fiche["etat"] == 2:
                self.ui.tableWidget2.setRowCount(cpt+1)
                itemID = QTableWidget2Item(str(fiche["id"]))
                itemNom = QTableWidget2Item(fiche["nom"])
                self.ui.tableWidget2.setItem(cpt, 0, itemID)
                self.ui.tableWidget2.setItem(cpt, 1, itemNom)
                cpt = cpt+1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rep = cuisine()
    rep.show()
    sys.exit(app.exec_())
