import sys
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([])
    label = QLabel("Hello World!")
    label.resize(400, 400)
    label.show()
    sys.exit(app.exec())
