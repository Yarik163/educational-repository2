from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen
import random
import sys


class windowInstaller(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Кнопка")
        self.pushButton.setGeometry(200, 230, 100, 40)

    

class RandomFlag(windowInstaller):
    def __init__(self):
        super().__init__()
        self.pushButton.clicked.connect(self.click)

    def click(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("Yellow")))
        painter.setBrush(QColor("Yellow"))
        count = random.randint(1, 10)
        for i in range(count):
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            diameter = random.randint(10, 100)
            painter.drawEllipse(x, y, diameter, diameter)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RandomFlag()
    window.show()
    sys.exit(app.exec())