import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Click me", self)
        self.label = QLabel("Hello", self)
        self.initUI()
    
    def initUI(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def on_click(self):
        print("Button clicked")
        self.button.setText("Clicked")
        self.button.setDisabled(True)
        self.label.setText("GoodBye")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # window2 = MainWindow()
    # window2.button.setText("Hello")
    # window2.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()