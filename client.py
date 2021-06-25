import sys  # sys нужен для передачи argv в QApplication
import requests.exceptions
from PyQt5 import QtWidgets, QtCore, QtGui
from UI_MainWindow import Ui_MainWindow
import pandas as pd
import apimoex


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.active_share = None
        self.shares = []
        self.add_share()
        self.pushButton.clicked.connect(self.find_shares)

    def find_shares(self):
        share_name = self.lineEdit.text()

        if share_name != '':
            for i in reversed(range(self.scrollLayout_shares.count())):
                widgetToRemove = self.scrollLayout_shares.itemAt(i).widget()
                self.scrollLayout_shares.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)

            for i in range(len(self.shares)):
                if share_name in self.shares[i].firm_name:
                    self.scrollLayout_shares.addRow(self.shares[i])
        else:
            for i in reversed(range(self.scrollLayout_shares.count())):
                widgetToRemove = self.scrollLayout_shares.itemAt(i).widget()
                self.scrollLayout_shares.removeWidget(widgetToRemove)
                widgetToRemove.setParent(None)

            for i in range(len(self.shares)):
                self.scrollLayout_shares.addRow(self.shares[i])

    def add_share(self):
        with requests.Session() as session:
            data = apimoex.get_board_securities(session, columns=("SECID", "SECNAME", "SHORTNAME"))
            data = pd.DataFrame(data)
            data.sort_values("SECNAME")
        for index, row in data.iterrows():
            s = Share(row["SECID"], row["SHORTNAME"])
            s.clicked.connect(s.open_shares)
            self.shares.append(s)
            self.scrollLayout_shares.addRow(s)


class ClickableWidget(QtWidgets.QWidget):  # класс для виджетов, на которые можно нажимать
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QtWidgets.QWidget.mousePressEvent(self, QMouseEvent)


class Share (ClickableWidget):
    def __init__(self, ticket, name):
        super(Share, self).__init__()
        self.ticket = ticket
        self.url = f"https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities/{self.ticket}.json"
        self.data = []
        self.plot_data = []
        self.plot_time = []
        self.firm_name = name
        self.name = QtWidgets.QLabel(self.firm_name)
        self.container = QtWidgets.QWidget(self)
        self.container.setGeometry(0, 0, 160, 50)
        self.layout = QtWidgets.QVBoxLayout(self.container)
        self.layout.addWidget(self.name)
        self.container.setStyleSheet("background-color:white;")
        self.setLayout(self.layout)

    def update(self):
        r = requests.get(self.url).json()
        self.data = []
        self.plot_data.append(r['marketdata']['data'][0][4])
        self.plot_time.append(r['marketdata']['data'][0][32])
        self.data.append(r['securities']['data'][0][9])
        self.data.append(str(r['marketdata']['data'][0][12]))
        self.data.append(str(r['marketdata']['data'][0][25]))
        self.data.append(str(r['marketdata']['data'][0][4]))
        self.data.append(str(r['marketdata']['data'][0][2]))
        self.data.append(str(r['marketdata']['data'][0][11]))
        self.data.append(str(r['marketdata']['data'][0][10]))


    def open_shares(self):
        if main_window.active_share != self:
            if main_window.active_share != None:
                main_window.active_share.container.setStyleSheet("background-color:white;")
            main_window.active_share = self
            self.update()

            self.container.setStyleSheet("background-color:rgb(183, 242, 255);")
            main_window.lineEdit.setText("")
            main_window.find_shares()

            main_window.label_firm_name.setText(self.data[0])
            main_window.label_8.setText(self.ticket)
            main_window.label_cost.setText(self.data[1])

            if self.data[2][0] == "-":
                main_window.label_dif_precent.setStyleSheet("color:red;")
                main_window.label_dif_precent.setText(f"{self.data[2]}%")
            else:
                main_window.label_dif_precent.setText(f"+{self.data[2]}%")
                main_window.label_dif_precent.setStyleSheet("color:green;")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()