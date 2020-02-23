from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.resolutionLabel = QtWidgets.QLabel(self.centralwidget)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.verticalLayout_3.addWidget(self.resolutionLabel)
        self.resolutionList = QtWidgets.QListWidget(self.centralwidget)
        self.resolutionList.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.resolutionList.setObjectName("resolutionList")
        item = QtWidgets.QListWidgetItem()
        self.resolutionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resolutionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resolutionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resolutionList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.resolutionList.addItem(item)
        self.verticalLayout_3.addWidget(self.resolutionList)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.colorLabel = QtWidgets.QLabel(self.centralwidget)
        self.colorLabel.setObjectName("colorLabel")
        self.verticalLayout.addWidget(self.colorLabel)
        self.blackRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.blackRadio.setEnabled(True)
        self.blackRadio.setChecked(True)
        self.blackRadio.setObjectName("blackRadio")
        self.verticalLayout.addWidget(self.blackRadio)
        self.redRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.redRadio.setObjectName("redRadio")
        self.verticalLayout.addWidget(self.redRadio)
        self.greenRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.greenRadio.setObjectName("greenRadio")
        self.verticalLayout.addWidget(self.greenRadio)
        self.blueRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.blueRadio.setObjectName("blueRadio")
        self.verticalLayout.addWidget(self.blueRadio)
        self.speedLabel = QtWidgets.QLabel(self.centralwidget)
        self.speedLabel.setObjectName("speedLabel")
        self.verticalLayout.addWidget(self.speedLabel)
        self.speedSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.speedSpinbox.setProperty("value", 10)
        self.speedSpinbox.setObjectName("speedSpinbox")
        self.verticalLayout.addWidget(self.speedSpinbox)
        self.launchButton = QtWidgets.QPushButton(self.centralwidget)
        self.launchButton.setObjectName("launchButton")
        self.verticalLayout.addWidget(self.launchButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resolutionList.setCurrentRow(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cellton Launcher"))
        self.resolutionLabel.setText(_translate("MainWindow", "Resolution"))
        __sortingEnabled = self.resolutionList.isSortingEnabled()
        self.resolutionList.setSortingEnabled(False)
        item = self.resolutionList.item(0)
        item.setText(_translate("MainWindow", "320x240"))
        item = self.resolutionList.item(1)
        item.setText(_translate("MainWindow", "640x480"))
        item = self.resolutionList.item(2)
        item.setText(_translate("MainWindow", "1280x720"))
        item = self.resolutionList.item(3)
        item.setText(_translate("MainWindow", "1600x900"))
        item = self.resolutionList.item(4)
        item.setText(_translate("MainWindow", "1920x1080"))
        self.resolutionList.setSortingEnabled(__sortingEnabled)
        self.colorLabel.setText(_translate("MainWindow", "Cell color"))
        self.blackRadio.setText(_translate("MainWindow", "Black"))
        self.redRadio.setText(_translate("MainWindow", "Red"))
        self.greenRadio.setText(_translate("MainWindow", "Green"))
        self.blueRadio.setText(_translate("MainWindow", "Blue"))
        self.speedLabel.setText(_translate("MainWindow", "Game speed"))
        self.launchButton.setText(_translate("MainWindow", "Launch"))
