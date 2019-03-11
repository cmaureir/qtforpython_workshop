import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCharts import QtCharts


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Tutorial")

if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    # Execute application
    sys.exit(app.exec_())
