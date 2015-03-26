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
            os.path.join(script_path, 'tardis.ico')))
        self.initUI()

    def initUI(self):
        # Create and initialize UI elements
        self.contentWidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.contentWidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.label_time1 = QtWidgets.QLabel(self.contentWidget)
        self.label_time2 = QtWidgets.QLabel(self.contentWidget)
        self.label_breakTime = QtWidgets.QLabel(self.contentWidget)
        self.timeEdit1 = QtWidgets.QTimeEdit(self.contentWidget)
        self.timeEdit2 = QtWidgets.QTimeEdit(self.contentWidget)
        self.timeEditBreakTime = QtWidgets.QTimeEdit(self.contentWidget)
        self.label_timeDiff = QtWidgets.QLabel(self.contentWidget)
        self.label_timeDiffOut = QtWidgets.QLabel(self.contentWidget)

        self.label_time1.setText("Time 1:")
        self.label_time2.setText("Time 2:")
        self.label_breakTime.setText("Break Time:")
        self.label_timeDiff.setText("Difference")
        self.label_timeDiffOut.setText("")
        self.timeEdit1.setTime(self.getStartTime())
        self.timeEdit2.setTime(QtCore.QTime.currentTime())

        # Set relations
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label_time1)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.timeEdit1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole,
                                  self.label_time2)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole,
                                  self.timeEdit2)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_breakTime)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.timeEditBreakTime)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_timeDiff)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.label_timeDiffOut)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.contentWidget)

        self.statusBar()

        # connect slots
        self.timeEdit1.timeChanged.connect(self.inputChanged)
        self.timeEdit2.timeChanged.connect(self.inputChanged)
        self.timeEditBreakTime.timeChanged.connect(self.inputChanged)

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
