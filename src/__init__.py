# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QMainWindow


#sublass QMainWindows to customize app main windows
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro")
        button = QPushButton("start")

        #Set the central widget of the windows
        self.setCentralWidget(button)


# Pass in sys.argv to allow command line arguments
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()

# Start the event loop.
app.exec()

# Your application won't reach here until you exit and the event
# loop has stopped.