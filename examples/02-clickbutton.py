import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtWidgets import QApplication, QPushButton

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
sys.exit(app.exec_())
