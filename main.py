import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui import CirclesUI


class Circles(CirclesUI):
    def __init__(self):
        super().__init__()

        self.button.clicked.connect(self.paint)
        self.do_paint = False

    def do(self, painter):
        diameter = randint(10, 100)
        x = randint(0, self.width() - diameter)
        y = randint(0, self.height() - diameter)

        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        painter.setBrush(color)
        painter.setPen(color)
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
    window = Circles()
    window.show()
    sys.exit(app.exec_())