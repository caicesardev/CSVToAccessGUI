import sys

from ui.ui_About import Ui_About

from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

__version__ = "1.0.0"


# Settings.
class About(QDialog, Ui_About):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.init_ui()
        self.parent = parent

    def init_ui(self):
        self.setupUi(self)
        self.show()
        self.about_qt_button.clicked.connect(QApplication.aboutQt)
        self.accept_button.clicked.connect(self.close)


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    gui = About()
    gui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
