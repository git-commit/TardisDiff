import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class TardisDiff(QtWidgets.QMainWindow):
    def __init__(self):
        super(TardisDiff, self).__init__()
        self.diff = 0

        self.clipboard = QtWidgets.QApplication.clipboard()
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Shift+C"), self, self.setClipboard)
        self.initUI()

    def initUI(self):
        #Create and initialize UI elements
        self.centralwidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.label_time1 = QtWidgets.QLabel(self.centralwidget)
        self.label_time2 = QtWidgets.QLabel(self.centralwidget)
        self.label_time3 = QtWidgets.QLabel(self.centralwidget)
        self.timeEdit1 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit3 = QtWidgets.QTimeEdit(self.centralwidget)
        self.label_timeDiff = QtWidgets.QLabel(self.centralwidget)
        self.label_timeDiffOut = QtWidgets.QLabel(self.centralwidget)

        self.label_time1.setText("Time 1:")
        self.label_time2.setText("Time 2:")
        self.label_time3.setText("Break Time:")
        self.label_timeDiff.setText("Difference")
        self.label_timeDiffOut.setText("")
        self.timeEdit1.setTime(QtCore.QTime(8, 0))
        currentTime = QtCore.QTime.currentTime()
        currentTime.setHMS(currentTime.hour(), currentTime.minute(), 0)
        self.timeEdit2.setTime(currentTime)

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
                                  self.label_time3)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.timeEdit3)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_timeDiff)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.label_timeDiffOut)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.statusBar()

        #connect slots
        self.timeEdit1.timeChanged.connect(self.inputChanged)
        self.timeEdit2.timeChanged.connect(self.inputChanged)
        self.timeEdit3.timeChanged.connect(self.inputChanged)

        self.setWindowTitle('TardisDiff')
        QtCore.QMetaObject.connectSlotsByName(self)
        self.inputChanged()
        self.show()

    def inputChanged(self):
        """
        Checks both time inputs and the break time input to determine the difference.
        Then calls the method to update the ui.
        """
        time1 = self.timeEdit1.time()
        time2 = self.timeEdit2.time()
        breakTime = self.timeEdit3.time().secsTo(QtCore.QTime(0, 0))
        self.diff = (time1.secsTo(time2) + breakTime) / 3600
        self.diff = round(self.diff, 2)
        self.label_timeDiffOut.setText(str(self.diff))

    def setClipboard(self):
        """Sets the current diff text to clipboard"""
        self.clipboard.setText(str(self.diff))
        self.statusBar().showMessage("Copied to clipboard.")




def main():
    app = QtWidgets.QApplication(sys.argv)
    ed = TardisDiff()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
