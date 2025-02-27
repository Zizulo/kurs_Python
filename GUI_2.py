import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1")
        label2 = QLabel("#2")
        label3 = QLabel("#3")
        label4 = QLabel("#4")

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")

        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)

        # central_widget.setLayout(vbox)

        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)

        # central_widget.setLayout(hbox)

        grid = QGridLayout()
        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()