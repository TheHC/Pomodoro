# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QMainWindow, QLineEdit,QTextEdit
from PyQt6.QtGui import QIcon
from PyQt6 import uic

#sublass QMainWindows to customize app main windows
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)

        # self.setWindowTitle("Pomodoro")
        # self.setWindowIcon(QIcon('icon.png'))
        # self.resize(400, 300)
        #
        # layout= QVBoxLayout()
        # self.setLayout(layout)
        #
        # self.inputField = QLineEdit()
        # button = QPushButton('&Say Hello', clicked=self.say_hello)
        # self.output= QTextEdit()
        #
        # layout.addWidget(self.inputField)
        # layout.addWidget(button)
        # layout.addWidget(self.output)

    def say_hello(self):
        inputText=self.inputField.text()
        self.output.setText('Hello {}'.format(inputText))

# Pass in sys.argv to allow command line arguments
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MyApp()
window.show()

# Start the event loop.
app.exec()

#sys.exit(app.exec_()) to ensure the process is terminated upon closing
# Your application won't reach here until you exit and the event
# loop has stopped.