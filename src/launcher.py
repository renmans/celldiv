import sys
import yaml
from PyQt5 import QtWidgets
import launcher_gui

class LauncherApp(QtWidgets.QMainWindow, launcher_gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LauncherApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()