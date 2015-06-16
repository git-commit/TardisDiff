import sys
import os
import inspect
from PyQt5 import QtWidgets, QtCore, QtGui
import plugnplay
from uptime import boottime
from TardisUtil import TardisOptions, TimeSubmitter


class TardisDiff(QtWidgets.QMainWindow):

    def __init__(self):
        super(TardisDiff, self).__init__()
        self.difference = 0
        self.clipboard = QtWidgets.QApplication.clipboard()

        # Set hot keys
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+C"), self,
                            self.setClipboard)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+T"), self,
                            self.notify_time_submitters)
        self.options = TardisOptions()

        # Get plugins
        plugnplay.plugin_dirs = ['./plugins', ]
        plugnplay.load_plugins()

        # Get directory path
        # From: http://stackoverflow.com/a/22881871/1963958
        if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
            script_path = os.path.abspath(sys.executable)
        else:
            script_path = inspect.getabsfile(TardisDiff)
        script_path = os.path.realpath(script_path)
        script_path = os.path.dirname(script_path)

        # Google for a fancy tardis icon until I've made one
        self.setWindowIcon(QtGui.QIcon(
            os.path.join(script_path, 'icon', 'tardis-by-camilla-isabell-kasbo.ico')))
        self.initUI()

    def initUI(self):
        # Create and initialize UI elements
        self.contentWidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.contentWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.timeEdit1 = QtWidgets.QTimeEdit(self.contentWidget)
        self.timeEdit2 = QtWidgets.QTimeEdit(self.contentWidget)
        self.timeEditBreakTime = QtWidgets.QTimeEdit(self.contentWidget)
        self.timeEditBreakTime.setDisplayFormat("h:mm")
        self.timeEditBreakTime.setCurrentSection(
            QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEditBreakTime.setTime(QtCore.QTime(0, 30))
        self.label_timeDiffOut = QtWidgets.QLabel(self.contentWidget)
        self.button_time1_now = QtWidgets.QPushButton(
            "Now", self.contentWidget)
        self.button_time2_now = QtWidgets.QPushButton(
            "Now", self.contentWidget)

        self.label_timeDiffOut.setText("")
        self.timeEdit1.setTime(self.getStartTime())
        self.timeEdit2.setTime(QtCore.QTime.currentTime())

        # Add UI elements
        row1 = QtWidgets.QHBoxLayout()
        row1.addWidget(self.timeEdit1)
        row1.addWidget(self.button_time1_now)

        row2 = QtWidgets.QHBoxLayout()
        row2.addWidget(self.timeEdit2)
        row2.addWidget(self.button_time2_now)

        self.formLayout.addRow("Time 1:", row1)
        self.formLayout.addRow("Time 2:", row2)
        self.formLayout.addRow("Break Time:", self.timeEditBreakTime)
        self.formLayout.addRow("Difference:", self.label_timeDiffOut)

        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.contentWidget)

        self.statusBar()

        # connect slots
        self.timeEdit1.timeChanged.connect(self.inputChanged)
        self.timeEdit2.timeChanged.connect(self.inputChanged)
        self.timeEditBreakTime.timeChanged.connect(self.inputChanged)
        self.button_time1_now.pressed.connect(self.reset_time1)
        self.button_time2_now.pressed.connect(self.reset_time2)

        self.setWindowTitle('TardisDiff')
        self.inputChanged()
        self.show()

    def inputChanged(self):
        """
        Checks both time inputs and the break time
        input to determine the difference.
        Then calls the method to update the ui.
        """
        time1 = self.timeEdit1.time()
        time2 = self.timeEdit2.time()
        breakTime = self.timeEditBreakTime.time().secsTo(QtCore.QTime(0, 0))
        self.difference = (time1.secsTo(time2) + breakTime) / 3600
        self.difference = round(self.difference, 2)
        self.label_timeDiffOut.setText(str(self.difference))

    def reset_time1(self):
        self.timeEdit1.setTime(QtCore.QTime.currentTime())

    def reset_time2(self):
        self.timeEdit2.setTime(QtCore.QTime.currentTime())

    def setClipboard(self):
        """Sets the current diff text to clipboard"""
        self.clipboard.setText(str(self.difference))
        self.statusBar().showMessage("Copied to clipboard.")

    def getStartTime(self):
        return TardisDiff.getBootTimeAsQTime()\
            if self.options.isStartTimeAuto()\
            else QtCore.QTime.fromString(self.options.getStartTime())

    def notify_time_submitters(self):
        TimeSubmitter.submit_time(self.difference)

    @staticmethod
    def getBootTimeAsQTime():
        return QtCore.QDateTime(boottime()).time()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ed = TardisDiff()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
