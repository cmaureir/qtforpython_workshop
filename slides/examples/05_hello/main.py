import sys
import random

from PySide2.QtCore import QObject, Slot
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine


class Bridge(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.colors = ["#ef9a9a", "#a5d6a7", "#90caf9", "white"]

    @Slot(result=str)
    def get_color(self):
        return random.choice(self.colors)

if __name__ == '__main__':
    sys.argv += ['--style', 'material']
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Instance of the Python object
    bridge = Bridge()

    # Expose the Python object to QML
    context = engine.rootContext()
    context.setContextProperty("con", bridge)

    engine.load("view.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
