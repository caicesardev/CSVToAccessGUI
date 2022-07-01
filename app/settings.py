import sys

from ui.ui_Settings import Ui_Settings

from PySide6.QtCore import (
    QLibraryInfo,
    QLocale,
    QTranslator,
    QSettings,
)
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
)

__version__ = "1.0.0"


# Settings.
class Settings(QDialog, Ui_Settings):
    def __init__(self, parent=None):
        super(Settings, self).__init__(parent)

        self.parent = parent
        self.init_ui()
        self.get_settings()
        self.set_settings()

    def init_ui(self):
        self.setupUi(self)
        self.show()
        self.accept_button.clicked.connect(self.accept)
        self.apply_button.clicked.connect(self.apply)
        self.cancel_button.clicked.connect(self.cancel)

    def accept(self):
        self.save()
        self.close()
        self.parent.set_settings()

    def apply(self):
        self.save()
        self.parent.set_settings()

    def save(self):
        self.app_settings.setValue(
            "start_maximized",
            self.start_maximized_checkbox.isChecked())
        self.app_settings.setValue(
            "show_output",
            self.show_output_checkbox.isChecked())
        self.app_theme.setValue(
            "light_theme",
            self.defaulttheme_radiobtn.isChecked())
        self.app_theme.setValue(
            "dark_theme",
            self.darktheme_radiobtn.isChecked())
        self.app_language.setValue("es_l", self.es_radiobtn.isChecked())
        self.app_language.setValue("ca_l", self.ca_radiobtn.isChecked())
        self.app_language.setValue("en_l", self.en_radiobtn.isChecked())

    def cancel(self):
        self.close()

    def get_settings(self):
        self.app_settings = QSettings("CSVToAccessGUI", "AppSettings")
        self.app_theme = QSettings("CSVToAccessGUI", "AppTheme")
        self.app_language = QSettings("CSVToAccessGUI", "AppLanguage")

    def set_settings(self):
        # App Settings
        if self.app_settings.value("start_maximized") == "true":
            self.start_maximized_checkbox.setChecked(True)
        else:
            self.start_maximized_checkbox.setChecked(False)
        if self.app_settings.value("show_output") == "true":
            self.show_output_checkbox.setChecked(True)
        else:
            self.show_output_checkbox.setChecked(False)
        # App Theme
        if self.app_theme.value("light_theme") == "true":
            self.defaulttheme_radiobtn.setChecked(True)
        else:
            self.darktheme_radiobtn.setChecked(True)
        # App Lang
        if self.app_language.value("es_l") == "true":
            self.es_radiobtn.setChecked(True)
        elif self.app_language.value("ca_l") == "true":
            self.ca_radiobtn.setChecked(True)
        else:
            self.en_radiobtn.setChecked(True)


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
