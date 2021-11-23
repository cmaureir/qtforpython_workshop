import os
import sys
import numpy as np

from PySide2.QtCore import QAbstractTableModel, QModelIndex, QRect, Qt
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import (QApplication, QGridLayout, QHeaderView,
    QTableView, QWidget)
from PySide2.QtCharts import QtCharts

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self.input_data = []
        self.mapping = {}
        self.column_count = len(data[0])
        self.row_count = len(data)

        self.input_data = [list(map(int, data_row)) for data_row in data]

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section % 2 == 0:
                return "x"
            else:
                return "y"
        else:
            return "{}".format(section + 1)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.input_data[index.row()][index.column()]
        elif role == Qt.EditRole:
            return self.input_data[index.row()][index.column()]
        elif role == Qt.BackgroundRole:
            for color, rect in self.mapping.items():
                if rect.contains(index.column(), index.row()):
                    return QColor(color)
            # cell not mapped return white color
            return QColor(Qt.white);
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.input_data[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def add_mapping(self, color, area):
        self.mapping[color] = area

    def clear_mapping(self):
        self.mapping = {}



class TableWidget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)

        self.model = CustomTableModel(data)

        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_view.setMinimumSize(400, 600)

        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.init_data()

        self.chart.createDefaultAxes()
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setMinimumSize(800, 600)

        # create main layout
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.table_view, 1, 0)
        self.main_layout.addWidget(self.chart_view, 1, 1)
        self.main_layout.setColumnStretch(1, 2)
        self.main_layout.setColumnStretch(0, 1)
        self.setLayout(self.main_layout)

    def add_series(self, name, columns):
        self.series = QtCharts.QLineSeries()
        self.series.setName(name)
        self.mapper = QtCharts.QVXYModelMapper(self)
        self.mapper.setXColumn(columns[0])
        self.mapper.setYColumn(columns[1])
        self.mapper.setSeries(self.series)
        self.mapper.setModel(self.model)
        self.chart.addSeries(self.series)

        # for storing color hex from the series
        seriesColorHex = "#000000"

        # get the color of the series and use it for showing the mapped area
        seriesColorHex = "{}".format(self.series.pen().color().name())
        self.model.add_mapping(seriesColorHex,
            QRect(columns[0], 0, 2, self.model.rowCount()))

    def init_data(self):
        for i in range(int(self.model.columnCount()/2)):
            self.add_series("Line {}".format(i+1), [i*2, (i*2)+1])

if __name__ == "__main__":

    # Read data
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        data = np.genfromtxt(sys.argv[1], delimiter=",")

        # Qt Application
        app = QApplication(sys.argv)

        w = TableWidget(data)
        w.show()
        sys.exit(app.exec_())
