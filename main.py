import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        
        self.button.clicked.connect(self.paint)
        self.do_paint = False

    def do(self, painter):
        diameter = randint(10, 100)
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)

        painter.setBrush(QColor(255, 255, 0))
        painter.setPen(QColor(255, 255, 0))
        painter.drawEllipse(x, y, diameter, diameter)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.do(qp)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YellowCircles()
    window.show()
    sys.exit(app.exec_())