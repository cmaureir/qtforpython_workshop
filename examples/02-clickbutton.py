import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QPushButton


@Slot()
def something():
    print("something!")


# Qt Application
app = QApplication([])

# Qt Widget
button = QPushButton("Push me!")
button.clicked.connect(something)
button.show()

# Executing app
sys.exit(app.exec())
