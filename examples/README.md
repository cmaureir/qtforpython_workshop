# Examples

## 01. Hello World

```python
import sys
from PySide2.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication([])
    label = QLabel("Hello World!")
    label.resize(400, 400)
    label.show()
    sys.exit(app.exec_())
```
## 02. Click button (without class)

```python
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
```

## 03. Click button (with a class)

```python
import sys
import random
from PySide2.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)
from PySide2.QtCore import Slot, Qt

class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
```

## 04. Line and Bar

Check the file `04-lineandbar.py`.

## 05. Nested donuts

Check the file `05-nesteddonuts.py`.

## 06. Wizard

Check the file `06-wizard.py`.

## More examples

You can find more examples
[in the official repository](http://code.qt.io/cgit/pyside/pyside-setup.git/tree/examples).
