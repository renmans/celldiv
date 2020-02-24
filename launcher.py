import sys
import yaml
from PyQt5 import QtWidgets
import launcher_gui


class LauncherApp(QtWidgets.QMainWindow, launcher_gui.Ui_MainWindow):
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        self.settings = settings
        self.started = False
        # Radio Buttons
        self.blackRadio.toggled.connect(self.colorChanged)
        self.redRadio.toggled.connect(self.colorChanged)
        self.greenRadio.toggled.connect(self.colorChanged)
        self.blueRadio.toggled.connect(self.colorChanged)
        # Resolutions List
        self.resolutionList.itemActivated.connect(self.resolutionChanged)
        self.launchButton.clicked.connect(self.launch)

    def colorChanged(self):
        rbuttons = (self.blackRadio, self.blueRadio,
                    self.greenRadio, self.redRadio)
        for rbutton in rbuttons:
            if rbutton.isChecked():
                self.settings['cell_color'] = rbutton.text().lower()

    def sizeChanged(self):
        self.settings['cell_size'] = self.sizeSpinbox.value()

    def speedChanged(self):
        self.settings['speed'] = self.speedSpinbox.value()

    def resolutionChanged(self):
        item = self.resolutionList.currentRow()
        width, height = self.resolutionList.item(item).text().split('x')
        self.settings['width'] = int(width)
        self.settings['height'] = int(height)

    def launch(self):
        self.started = True
        self.colorChanged()
        self.sizeChanged()
        self.speedChanged()
        self.resolutionChanged()
        with open('settings.yml', 'w') as f:
            yaml.safe_dump(self.settings, f)
        self.close()


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
