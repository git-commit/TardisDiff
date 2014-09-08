import sys
from PyQt5 import QtWidgets, QtCore


class TardisDiff(QtWidgets.QMainWindow):
    def __init__(self):
        super(TardisDiff, self).__init__()
        self.initUI()

    def initUI(self):
        #Create and initialize UI elements
        self.centralwidget = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.formLayout = QtWidgets.QFormLayout()
        self.label_time1 = QtWidgets.QLabel(self.centralwidget)
        self.label_time2 = QtWidgets.QLabel(self.centralwidget)
        self.timeEdit1 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.label_timeDiff = QtWidgets.QLabel(self.centralwidget)
        self.label_timeDiffOut = QtWidgets.QLabel(self.centralwidget)

        self.label_time1.setText("Time 1:")
        self.label_time2.setText("Time 2:")
        self.label_timeDiff.setText("Difference")
        self.label_timeDiffOut.setText("")
        self.timeEdit1.setTime(QtCore.QTime(8, 0))
        self.timeEdit2.setTime(QtCore.QTime(17, 0))

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
                                  self.label_timeDiff)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.label_timeDiffOut)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.statusBar()

        #connect slots
        self.timeEdit1.timeChanged.connect(self.inputChanged)
        self.timeEdit2.timeChanged.connect(self.inputChanged)

        self.setWindowTitle('TardisDiff')
        QtCore.QMetaObject.connectSlotsByName(self)

        self.show()

    def inputChanged(self):
        time1 = self.timeEdit1.time()
        time2 = self.timeEdit2.time()
        diff = time1.secsTo(time2)
        self.label_timeDiffOut.setText(str(diff/3600))


def main():
    app = QtWidgets.QApplication(sys.argv)
    ed = TardisDiff()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
