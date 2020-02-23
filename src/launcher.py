import sys
import os
import yaml
from PyQt5 import QtWidgets
import launcher_gui

class LauncherApp(QtWidgets.QMainWindow, launcher_gui.Ui_MainWindow):
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        self.settings = settings
        self.started = False
        self.resolutionList.itemActivated.connect(self.selectionChanged)
        self.launchButton.clicked.connect(self.launch)

    def selectionChanged(self):
        item = self.resolutionList.currentRow()
        width, height = self.resolutionList.item(item).text().split('x')
        self.settings['width'] = int(width)
        self.settings['height'] = int(height)

    def launch(self):
        self.started = True
        self.selectionChanged()
        # other methods
        with open('settings.yml', 'w') as f:
            yaml.safe_dump(self.settings, f)

def main():
    with open('settings.yml', 'r') as f:
        settings = yaml.safe_load(f)
    app = QtWidgets.QApplication(sys.argv)
    window = LauncherApp(settings)
    window.show()
    app.exec_()
    return window.started

if __name__ == '__main__':
    main()
