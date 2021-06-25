import sys
import matplotlib
matplotlib.use('Qt5Agg')
import apimoex
import requests
import pandas as pd
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.dates


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Share_plot(QtWidgets.QWidget):

    def __init__(self, ticket, firm_name, start_time, end_time):
        super(Share_plot, self).__init__()
        with requests.Session() as session:
            share_json = apimoex.get_board_candles(session, ticket, interval=24, start=start_time, end=end_time)
            share_df = pd.DataFrame(share_json)
        dates = []
        for index, row in share_df.iterrows():
            dates.append(row["begin"].split(' ')[0])
        date_float = matplotlib.dates.date2num(dates)
        sc = MplCanvas(self, width=12, height=5, dpi=100)
        sc.axes.plot(date_float, share_df['open'])
        sc.axes.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m-%d"))
        sc.axes.set_title(f"Цена акций {firm_name} с {start_time} по {end_time}")
        sc.axes.set_ylabel("Цена акций в рублях")

        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.

        self.setLayout(layout)

        self.show()

