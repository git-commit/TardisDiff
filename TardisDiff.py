import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import ctypes
from uptime import boottime


class TardisDiff(QtWidgets.QMainWindow):

    def __init__(self):
        super(TardisDiff, self).__init__()
        self.diff = 0
        self.clipboard = QtWidgets.QApplication.clipboard()
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+C"), self,
                            self.setClipboard)
        # Google for a fancy tardis icon until I've made one
        self.setWindowIcon(QtGui.QIcon('tardis.ico'))
        self.initUI()

    def initUI(self):
        #Create and initialize UI elements
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
        self.timeEdit1.setTime(self.getBootTimeAsQTime())
        self.timeEdit2.setTime(QtCore.QTime.currentTime())

        #Set relations
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

        #connect slots
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
        self.diff = (time1.secsTo(time2) + breakTime) / 3600
        self.diff = round(self.diff, 2)
        self.label_timeDiffOut.setText(str(self.diff))

    def setClipboard(self):
        """Sets the current diff text to clipboard"""
        self.clipboard.setText(str(self.diff))
        self.statusBar().showMessage("Copied to clipboard.")

    def getBootTimeAsQTime(self):
        return QtCore.QDateTime(boottime()).time()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ed = TardisDiff()
    sys.exit(app.exec_())


if __name__ == '__main__':
    myappid = 'net.xerael.tardisdiff'
    if sys.platform == "win32":
        """
        This is for collapsing on the task bar on windows 7/8 and using
        the application icon on the task bar instead of the python icon
        if running using a python executable.

        See:
        http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7
        """
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    main()
