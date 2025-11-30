# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QMainWindow, QLineEdit,QTextEdit


#sublass QMainWindows to customize app main windows
class MMyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro")
        
        self.inputtest=
        button = QPushButton("start")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        layout = QVBoxLayout()
        layout.addWidget(button)

        #Set the central widget of the windows
        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("clicked")
    def the_button_was_toggled(self, checked):
        print("checked?",checked)

# Pass in sys.argv to allow command line arguments
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()

#sys.exit(app.exec_()) to ensure the process is terminated upon closing
# Your application won't reach here until you exit and the event
# loop has stopped.