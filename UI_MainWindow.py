
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1452, 879)
        MainWindow.setMinimumSize(QtCore.QSize(1452, 879))
        MainWindow.setMaximumSize(QtCore.QSize(1452, 879))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 171, 861))
        self.layoutWidget.setObjectName("layoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(130, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.scrollLayout_shares = QtWidgets.QFormLayout()

        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setLayout(self.scrollLayout_shares)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 167, 819))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(350, 410, 110, 22))
        self.dateEdit.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit.setDate(QtCore.QDate(2000, 1, 1))
        self.dateEdit.setObjectName("dateEdit")

        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(490, 410, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 410, 161, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 410, 31, 16))
        self.label_2.setObjectName("label_2")

        self.widget_layout_all = QtWidgets.QFormLayout()
        self.widget_plot_all = QtWidgets.QWidget(self.centralwidget)
        self.widget_plot_all.setLayout(self.widget_layout_all)
        self.widget_plot_all.setGeometry(QtCore.QRect(190, 440, 1241, 421))
        self.widget_plot_all.setObjectName("widget_plot_all")

        self.pushButton_create_plot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_plot.setGeometry(QtCore.QRect(610, 410, 131, 23))
        self.pushButton_create_plot.setObjectName("pushButton_create_plot")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 10, 101, 16))
        self.label_3.setObjectName("label_3")

        self.label_firm_name = QtWidgets.QLabel(self.centralwidget)
        self.label_firm_name.setGeometry(QtCore.QRect(300, 10, 251, 16))
        self.label_firm_name.setText("")
        self.label_firm_name.setObjectName("label_firm_name")

        self.label_cost = QtWidgets.QLabel(self.centralwidget)
        self.label_cost.setGeometry(QtCore.QRect(210, 60, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_cost.setFont(font)
        self.label_cost.setObjectName("label_cost")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 98, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_dif_precent = QtWidgets.QLabel(self.centralwidget)
        self.label_dif_precent.setGeometry(QtCore.QRect(300, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_dif_precent.setFont(font)
        self.label_dif_precent.setObjectName("label_dif_precent")

        self.label_text_bid = QtWidgets.QLabel(self.centralwidget)
        self.label_text_bid.setGeometry(QtCore.QRect(460, 75, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_text_bid.setFont(font)
        self.label_text_bid.setObjectName("label_text_bid")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 110, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_bid = QtWidgets.QLabel(self.centralwidget)
        self.label_bid.setGeometry(QtCore.QRect(550, 80, 47, 13))
        self.label_bid.setObjectName("label_bid")

        self.label_offer = QtWidgets.QLabel(self.centralwidget)
        self.label_offer.setGeometry(QtCore.QRect(510, 110, 47, 16))
        self.label_offer.setObjectName("label_offer")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(640, 110, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(640, 75, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_max_cost = QtWidgets.QLabel(self.centralwidget)
        self.label_max_cost.setGeometry(QtCore.QRect(710, 80, 47, 13))
        self.label_max_cost.setObjectName("label_max_cost")

        self.label_min_cost = QtWidgets.QLabel(self.centralwidget)
        self.label_min_cost.setGeometry(QtCore.QRect(710, 110, 47, 16))
        self.label_min_cost.setObjectName("label_min_cost")

        self.widget_layout_now = QtWidgets.QFormLayout()
        self.widget_plot_now = QtWidgets.QWidget(self.centralwidget)
        self.widget_plot_now.setLayout(self.widget_layout_now)
        self.widget_plot_now.setGeometry(QtCore.QRect(190, 190, 1241, 211))
        self.widget_plot_now.setObjectName("widget_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 170, 201, 16))
        self.label_5.setObjectName("label_5")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 10, 47, 13))
        self.label_7.setObjectName("label_7")

        self.label_ticket = QtWidgets.QLabel(self.centralwidget)
        self.label_ticket.setGeometry(QtCore.QRect(630, 10, 71, 16))
        self.label_ticket.setText("")
        self.label_ticket.setObjectName("label_ticket")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(790, 75, 101, 16))
        self.label_8.setObjectName("label_8")

        self.label_update_time = QtWidgets.QLabel(self.centralwidget)
        self.label_update_time.setGeometry(QtCore.QRect(910, 75, 191, 16))
        self.label_update_time.setObjectName("label_update_time")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(790, 110, 131, 16))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(940, 110, 151, 16))
        self.label_12.setObjectName("label_12")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Показать изменения акций с "))
        self.label_2.setText(_translate("MainWindow", "по"))
        self.pushButton_create_plot.setText(_translate("MainWindow", "Вывести график"))
        self.label_3.setText(_translate("MainWindow", "Название фирмы"))
        self.label_cost.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "RUB"))
        self.label_dif_precent.setText(_translate("MainWindow", "0"))
        self.label_text_bid.setText(_translate("MainWindow", "Предложение:"))
        self.label_6.setText(_translate("MainWindow", "Спрос:"))
        self.label_bid.setText(_translate("MainWindow", "0"))
        self.label_offer.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Минимум:"))
        self.label_10.setText(_translate("MainWindow", "Максимум:"))
        self.label_max_cost.setText(_translate("MainWindow", "0"))
        self.label_min_cost.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Изменение цены акций"))
        self.label_7.setText(_translate("MainWindow", "Тикет:"))
        self.label_8.setText(_translate("MainWindow", "Время обновления:"))
        self.label_update_time.setText(_translate("MainWindow", "00:00:00"))
        self.label_11.setText(_translate("MainWindow", "Рекомендация по акциям:"))
        self.label_12.setText(_translate("MainWindow", "Пока что-то ничего не знаю"))
