# Only needed for access to command line arguments
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QPushButton, QMainWindow, QLineEdit,QTextEdit
from PyQt6.QtGui import QIcon, QCloseEvent
from PyQt6 import uic
from PyQt6.QtCore import QRunnable, QThreadPool, QTimer, pyqtSlot, QObject, pyqtSignal
# from PySide6.QtCore import  Signal, QObject
import time
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info('Starting program')



class Worker(QRunnable):
    """Worker thread"""
    def __init__(self, time_value):
        super().__init__()
        self.time_value = time_value
        self.signals = WorkerSignals()
        self.is_running = True


    @pyqtSlot()
    def run(self):
        # print("Thread start")
        logger.info('Starting worker thread')
        bar_progress_buff=0
        self.signals.progress.emit(0)
        for i in range(self.time_value):
                if self.is_running:
                    time.sleep(1)
                    # self.signals.progress.emit(int(bar_progress_buff / self.time_value))
                    self.signals.progress.emit(i+1)
                    bar_progress_buff=bar_progress_buff+1
                else :
                    break

        # print(self.time)
        # print("Thread end")
        logger.info('Ended worker thread')
        self.signals.finished.emit()

    def stop(self):
        logger.info('is_running to False')



class WorkerSignals(QObject):
    finished=pyqtSignal()
    progress=pyqtSignal(int)
    window_closed=pyqtSignal()
class CloseSignals(QObject):
    close=pyqtSignal()


#sublass QMainWindows to customize app main windows
class MyApp(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        uic.loadUi('gui.ui', self)
        self.step="Focus"
        self.button.clicked.connect(self.state_machine)
        self.worker=Worker(0)
        self.threadpool=QThreadPool()

        self.Bar.setMinimum(0)
        self.Bar.setValue(0)

        self.state=1
        self.focus_label.setStyleSheet("background-color: green")
        self.window_closed=CloseSignals()
        self.window_closed.close.connect(self.worker.stop)

        self.Stop.clicked.connect(self.stop_handler)
    def state_machine(self):
        logger.info("starting state machine")
        sleep_time=0
        if self.step=="Focus":
            self.short_label.setStyleSheet("background-color: grey")
            self.focus_label.setStyleSheet("background-color: blue")
            sleep_time=25*60
        elif self.step=="Short":
            self.short_label.setStyleSheet("background-color: blue")
            self.focus_label.setStyleSheet("background-color: grey")
            sleep_time=5*60
        self.worker=Worker(sleep_time)
        self.worker.signals.finished.connect(self.actual_state)
        self.worker.signals.progress.connect(self.progress_bar)
        self.Bar.setMaximum(sleep_time)
        self.threadpool.start(self.worker)
    def actual_state(self):
        logger.info("starting actual state")
        if self.step == "Focus":
            self.step="Short"
            self.short_label.setStyleSheet("background-color: green")
            self.focus_label.setStyleSheet("background-color: grey")
        else :
            self.step="Focus"
            self.short_label.setStyleSheet("background-color: grey")
            self.focus_label.setStyleSheet("background-color: green")
    def progress_bar(self, value):
        self.Bar.setValue(value)
    def stop_handler(self):
        if self.step=="Focus":
            self.short_label.setStyleSheet("background-color: grey")
            self.focus_label.setStyleSheet("background-color: green")
        else :
            self.short_label.setStyleSheet("background-color: green")
            self.focus_label.setStyleSheet("background-color: grey")
        self.worker.is_running = False
    def closeEvent(self, event: QCloseEvent):
        logging.info("closing window")
        # self.window_closed.close.emit()
        self.worker.is_running = False

# Pass in sys.argv to allow command line arguments
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MyApp()
window.show()

# Start the event loop.
#app.exec()

# to ensure the process is terminated upon closing
sys.exit(app.exec())
# Your application won't reach here until you exit and the event
# loop has stopped.