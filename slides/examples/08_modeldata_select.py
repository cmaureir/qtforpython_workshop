#############################################################################
##
## Copyright (C) 2018 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################
import os
import sys
import numpy as np

from PySide2.QtCore import QAbstractTableModel, QModelIndex, QRect, Qt, Slot
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import (QApplication, QGridLayout, QHeaderView,
    QTableView, QWidget, QComboBox, QVBoxLayout)
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
            return "Column {}".format(section)
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
            self.input_data[index.row()][index.column()] = float(value)
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

        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)


        self.chart.createDefaultAxes()
        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart_view.setMinimumSize(640, 480)

        self.x_combo_box = QComboBox()
        self.y_combo_box = QComboBox()

        for column in range(self.model.columnCount()):
            self.x_combo_box.addItem(self.model.headerData(column, Qt.Horizontal, Qt.DisplayRole))
            self.y_combo_box.addItem(self.model.headerData(column, Qt.Horizontal, Qt.DisplayRole))

        self.x_combo_box.currentIndexChanged.connect(self.init_data)
        self.y_combo_box.currentIndexChanged.connect(self.init_data)

        self.init_data()

        # create main layout
        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.table_view, 1, 0)

        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.x_combo_box)
        self.right_layout.addWidget(self.y_combo_box)
        self.right_layout.addWidget(self.chart_view)

        self.main_layout.addLayout(self.right_layout, 1, 1)

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


    @Slot()
    def init_data(self):
        self.chart.removeAllSeries()
        x_index = self.x_combo_box.currentIndex()
        y_index = self.y_combo_box.currentIndex()
        self.add_series("Line", [x_index, y_index])

        seriesColorHex = "#000000"
        seriesColorHex = "{}".format(self.series.pen().color().name())
        print(x_index, y_index)
        self.model.add_mapping(seriesColorHex, QRect(x_index, 0, 1, self.model.rowCount()))
        self.model.add_mapping(seriesColorHex, QRect(y_index, 0, 1, self.model.rowCount()))

if __name__ == "__main__":

    # Read data
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        data = np.genfromtxt(sys.argv[1], delimiter=",")

        # Qt Application
        app = QApplication(sys.argv)

        w = TableWidget(data)
        w.show()
        sys.exit(app.exec_())
