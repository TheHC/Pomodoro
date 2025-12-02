# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QMainWindow, QLineEdit,QTextEdit
from PyQt6.QtGui import QIcon
from PyQt6 import uic
from PyQt6.QtCore import QRunnable, QThreadPool, QTimer, pyqtSlot
from PySide6.QtCore import  Signal, QObject
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('Starting program')

variable=0
state_select = "Focus"
class Worker(QRunnable):
    """Worker thread"""
    def __init__(self, time):
        super().__init__()
        self.time = time
        self.signals = WorkerSignals()


    @pyqtSlot()
    def run(self):
        # print("Thread start")
        logger.info('Starting worker thread')
        time.sleep(self.time)
        # print(self.time)
        # print("Thread end")
        logger.info('Ended worker thread')
        self.signals.finished.emit()


class WorkerSignals(QObject):
    finished=Signal()
    progress=Signal(int)



#sublass QMainWindows to customize app main windows
class MyApp(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.step="Focus"
        self.button.clicked.connect(self.state_machine)

        self.threadpool=QThreadPool()

        self.state=1
        self.focus_label.setStyleSheet("background-color: green")
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

    def state_machine(self):

        if self.step=="Focus":
            self.short_label.setStyleSheet("background-color: grey")
            self.focus_label.setStyleSheet("background-color: blue")
            worker=Worker(10)
        elif self.step=="Short":
            self.short_label.setStyleSheet("background-color: blue")
            self.focus_label.setStyleSheet("background-color: grey")
            worker=Worker(2)
        worker.signals.finished.connect(self.actual_state)
        self.threadpool.start(worker)
    def actual_state(self):
        if self.step == "Focus":
            self.step="Short"
            self.short_label.setStyleSheet("background-color: green")
            self.focus_label.setStyleSheet("background-color: grey")
        else :
            self.step="Focus"
            self.short_label.setStyleSheet("background-color: grey")
            self.focus_label.setStyleSheet("background-color: green")

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