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
        self.figureList.itemActivated.connect(self.setup)
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

    def setup(self):
        item = self.figureList.currentRow()
        figure = self.figureList.item(item).text().lower()
        figures = {'random': [],
                   'glider': [(11, 12), (12, 10), (12, 12), (13, 11),
                              (13, 12)],
                   'gun':    [(15, 11), (16, 11), (15, 12), (16, 12),
                              (15, 21), (16, 21), (17, 21), (14, 22),
                              (18, 22), (13, 23), (19, 23), (13, 24),
                              (19, 24), (16, 25), (14, 26), (18, 26),
                              (15, 27), (16, 27), (17, 27), (16, 28),
                              (13, 31), (14, 31), (15, 31), (13, 32),
                              (14, 32), (15, 32), (12, 33), (16, 33),
                              (11, 35), (12, 35), (16, 35), (17, 35),
                              (13, 45), (14, 45), (13, 46), (14, 46)]}
        self.settings['figure'] = figures[figure]

    def launch(self):
        self.started = True
        self.colorChanged()
        self.sizeChanged()
        self.speedChanged()
        self.resolutionChanged()
        self.setup()
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
