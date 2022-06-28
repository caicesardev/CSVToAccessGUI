import sys

from ui.ui_About import Ui_About

from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
)

__version__ = "1.0.0"


# Settings.
class About(QWidget, Ui_About):
    def __init__(self):
        super(About, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
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
