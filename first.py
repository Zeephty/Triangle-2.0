import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from random import randrange
import ui

 
class MyWidget(QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 400, 400)
        self.setMouseTracking(True)

        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.toggle)

        self.b = False
    
    def toggle(self):
        self.b = True
        self.update()

    def paintEvent(self, event):
        if self.b:
            painter = QPainter(self)
            painter.setBrush(QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256)))
            randr = randrange(2, 300)
            painter.drawEllipse(randrange(0, self.width() - randr), randrange(0, self.height() - randr), randr, randr)
            self.b = False

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())