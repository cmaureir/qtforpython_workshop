import sys
import csv
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QAction, QPainter
from PySide6.QtWidgets import (QWidget, QTableWidget, QLineEdit, QPushButton,
                               QVBoxLayout, QHBoxLayout, QLabel, QHeaderView,
                               QTableWidgetItem, QApplication, QMainWindow,
                               QGridLayout, QMessageBox)
from PySide6.QtCharts import QChartView, QChart, QBarSeries, QBarSet


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.items = 0

        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Quantity"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Chart
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Right
        self.description = QLineEdit()
        self.quantity = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.plot = QPushButton("Plot")

        # Disabling 'Add' button
        self.add.setEnabled(False)

        self.right = QVBoxLayout()
        self.right.setContentsMargins(10, 10, 10, 10)

        self.right_top = QGridLayout()

        self.right_top.addWidget(QLabel("Description"), 0, 0, 1, 1)
        self.right_top.addWidget(self.description, 0, 1, 1, 3)
        self.right_top.addWidget(QLabel("Quantity"), 1, 0, 1, 1)
        self.right_top.addWidget(self.quantity, 1, 1, 1, 1)
        self.right_top.addWidget(self.add, 1, 2, 1, 2)

        self.right.addLayout(self.right_top)
        self.right.addWidget(self.chart_view)

        self.right_bottom = QGridLayout()
        self.right_bottom.addWidget(self.plot, 0, 0, 1, 2)
        self.right_bottom.addWidget(self.clear, 1, 0)
        self.right_bottom.addWidget(self.quit, 1, 1)

        self.right.addLayout(self.right_bottom)

        # QWidget Layout
        self.layout = QHBoxLayout()

        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        # Set the layout to the QWidget
        self.setLayout(self.layout)

        # Signals and Slots
        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.description.textChanged[str].connect(self.check_disable)
        self.quantity.textChanged[str].connect(self.check_disable)

    @Slot()
    def add_element(self):
        des = self.description.text()
        qty = self.quantity.text()

        self.table.insertRow(self.items)
        self.table.setItem(self.items, 0, QTableWidgetItem(des))
        self.table.setItem(self.items, 1, QTableWidgetItem(qty))

        self.description.setText("")
        self.quantity.setText("")

        self.items += 1

    @Slot()
    def check_disable(self, s):
        if not self.description.text() or not self.quantity.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def plot_data(self):
        # Get table information
        series = QBarSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())

            bar_set = QBarSet(text)
            bar_set.append(number)

            series.append(bar_set)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):
        QApplication.quit()

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")
        self.widget = widget

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Load QAction
        load_action = QAction("Load", self)
        load_action.setShortcut("Ctrl+L")
        load_action.triggered.connect(self.load_data)

        # Save QAction
        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.save_data)

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(load_action)
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(exit_action)
        self.setCentralWidget(self.widget)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def save_data(self, checked):
        rows = self.widget.table.rowCount()
        if rows:
            with open('../data.csv', 'w') as f:
                writer = csv.writer(f, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)
                for i in range(rows):
                    des = self.widget.table.item(i, 0).text()
                    qty = self.widget.table.item(i, 1).text()
                    writer.writerow([des, qty])
                reply = QMessageBox.information(self, "Save",
                                                "Saved file successfully")
                # Invoke reply to show it
                reply

    @Slot()
    def load_data(self, checked):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            self.widget.items = 0
            self.widget.table.setRowCount(0)
            for i, row in enumerate(reader):
                des, qty = row
                self.widget.table.insertRow(i)
                self.widget.table.setItem(i, 0, QTableWidgetItem(des))
                self.widget.table.setItem(i, 1, QTableWidgetItem(qty))
                self.widget.items += 1

            reply = QMessageBox.information(self, "Load",
                                            "Load successfully")
            reply


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widget = Widget()
    # QMainWindow using QWidget as central widget
    window = MainWindow(widget)
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec())
