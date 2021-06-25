from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt

from MainWindow_ui import Ui_MainWindow


class Widget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self._old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._old_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._old_pos = None

    def mouseMoveEvent(self, event):
        if not self._old_pos:
            return

        delta = event.pos() - self._old_pos
        self.move(self.pos() + delta)
