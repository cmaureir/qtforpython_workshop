import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication([])

label = QLabel("Hello Qt for Python")

label.setFixedWidth(800)
label.setFixedHeight(800)

label.show()

sys.exit(app.exec_())
