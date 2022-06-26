import sys
import os
import subprocess

from ui.ui_MainWindow import Ui_MainWindow

from PySide6.QtCore import (
    QSettings,
    QSize,
    QPoint,
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

__version__ = "1.0.0"


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()
        # Get app settings.
        self.get_settings()
        # Set app settings.
        self.set_settings()

    def init_ui(self):
        self.setupUi(self)

    def get_settings(self):
        self.w_attrib = QSettings("CSVToAccessGUI", "WindowAttributes")

    def set_settings(self):
        # Initial window size/pos last saved. Use default values for first time.
        self.resize(self.w_attrib.value("size", QSize(270, 225)))
        self.move(self.w_attrib.value("pos", QPoint(50, 50)))

    def on_restart(self):
        self.close()
        subprocess.Popen([sys.executable, "./main.py"])
        os.system('cls' if os.name == 'nt' else 'clear')

    # Event that is called when trying to exit the program.
    def closeEvent(self, event) -> None:
        # Remember window postion and size on exit.
        self.w_attrib.setValue("size", self.size())
        self.w_attrib.setValue("pos", self.pos())


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    gui = MainWindow()
    gui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
