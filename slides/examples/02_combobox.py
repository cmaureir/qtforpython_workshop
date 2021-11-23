import sys
import numpy as np

from PySide2.QtWidgets import (QApplication, QWidget, QComboBox)


if __name__ == "__main__":
    app = QApplication([])

    combo_box = QComboBox()
    with open("02_hello.txt") as f:
        for line in f.readlines():
            line = line.split(",")
            language = line[0].strip()
            message = line[1].strip()

            combo_box.addItem(language)

    combo_box.setMinimumSize(800,200)
    combo_box.show()


    sys.exit(app.exec_())
