import sys
import numpy as np

from PySide2.QtCore import Slot, Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import (QApplication, QWidget, QVBoxLayout,
    QComboBox, QPushButton, QLabel)


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # Placeholder for the data
        self.data = {}


        # Widgets for the interface
        self.combo_box = QComboBox()
        self.button = QPushButton("Change")
        self.label = QLabel("<Empty>")

        # Properties of the QLabel
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Titillium", 30))

        # Layout of the widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.combo_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        # Set main layout
        self.setLayout(self.layout)

        # Initialiazing the data
        self.init_combo_box()

        # Connecting the button clicked signal
        self.button.clicked.connect(self.update_label)


    # Initialization of the data
    def init_combo_box(self):

        with open("02_hello.txt") as f:
            for line in f.readlines():
                line = line.split(",")
                language = line[0].strip()
                message = line[1].strip()

                self.data[language] = message
                self.combo_box.addItem(language)

    # Slot associated to the clicked
    @Slot()
    def update_label(self):
        self.label.setText(self.data[self.combo_box.currentText()])


if __name__ == "__main__":
    app = QApplication([])

    w = MyWidget()
    w.setMinimumSize(800, 400)
    w.show()

    sys.exit(app.exec_())
