import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPoint


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.button.clicked.connect(self.draw_circle)

        self.circle_exists = False
        self.circle_radius = 0
        self.circle_center = QPoint()

    def draw_circle(self):
        self.circle_exists = True
        self.circle_radius = random.randint(10, 200)
        self.circle_center = QPoint(random.randint(self.circle_radius, self.width() - self.circle_radius),
                                    random.randint(self.circle_radius, self.height() - self.circle_radius))
        self.update()

    def paintEvent(self, event):
        if self.circle_exists:
            painter = QPainter(self)
            painter.setPen(QColor(255, 255, 0))  # Желтый цвет
            painter.setBrush(QColor(255, 255, 0))  # Заливка желтым цветом
            painter.drawEllipse(self.circle_center, self.circle_radius, self.circle_radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec_())
