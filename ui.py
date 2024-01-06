from PyQt5.QtWidgets import QMainWindow, QPushButton


class CirclesUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.resize(500, 500)

    def initUi(self):
        self.button = QPushButton('Добавить окружность', self)
        self.button.resize(150, 25)