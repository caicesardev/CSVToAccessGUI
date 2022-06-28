import sys

from ui.ui_Settings import Ui_Settings

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
class Settings(QWidget, Ui_Settings):
    def __init__(self):
        super(Settings, self).__init__()

        self.init_ui()
        self.get_settings()
        self.set_settings()

    def init_ui(self):
        self.setupUi(self)
        self.accept_button.clicked.connect(self.accept)
        self.apply_button.clicked.connect(self.apply)
        self.cancel_button.clicked.connect(self.cancel)

    def save(self):
        pass

    def accept(self):
        self.save()
        self.close()

    def apply(self):
        self.save()

    def cancel(self):
        self.close()

    def get_settings(self):
        pass

    def set_settings(self):
        pass


def main():
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load("qtbase_" + QLocale.system().name(),
                    QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)
    gui = Settings()
    gui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
