import sys
import os
import subprocess
import pandas as pd

from ui.ui_MainWindow import Ui_MainWindow

from PySide6.QtCore import (
    Qt,
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
    QFrame,
    QLabel,
    QVBoxLayout,
    QTableWidgetItem
)

__version__ = "1.0.0"


# CSVDroppableFrame
class CSVDroppableFrame(QFrame):
    def __init__(self, parent):
        super(CSVDroppableFrame, self).__init__(parent)

        self.parent = parent
        self.setAcceptDrops(True)
        self.init_ui()

    def init_ui(self):
        self.verticalLayout_3 = QVBoxLayout()
        self.setObjectName("csv_droppable_frame")
        self.setStyleSheet(
            """
        QFrame#csv_droppable_frame {
        	border: 2px dotted grey;
	        padding: 20px;
        }
        """)
        self.setLayout(self.verticalLayout_3)
        self.csv_title_label = QLabel()
        self.csv_title_label.setText(
            """
        <html>
        <head/>
            <body>
                <p>
                    <span style=" color:#55557f;">Arrastra o selecciona archivo CSV</span>
                </p>
            </body>
        </html>
        """)
        self.csv_title_label.setStyleSheet(
            "QLabel {font-size: 17px; font-weight: bold;}")
        self.csv_title_label.setAlignment(Qt.AlignCenter)
        self.selected_csv_file_label = QLabel()
        self.selected_csv_file_label.setText(
            """
        <html>
        <head/>
            <body>
                <p>
                    <span style=" color:#585858;">Archivo CSV seleccionado:</span>
                    </p>
            </body>
        </html>
        """)
        self.selected_csv_file_label.setMaximumHeight(35)
        self.selected_csv_file_label.setStyleSheet("QLabel {font-size: 13px;}")
        self.selected_csv_file_label.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.csv_title_label)
        self.verticalLayout_3.addWidget(self.selected_csv_file_label)

    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
        return super().dragEnterEvent(event)

    def dragMoveEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
        return super().dragMoveEvent(event)

    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            # Checks if you are dropping a .csv file.
            if event.mimeData().urls()[0].toLocalFile().endswith(".csv"):
                event.setDropAction(Qt.CopyAction)
                event.accept()
                self.csv_file = event.mimeData().urls()[0].toLocalFile()
                self.selected_csv_file_label.setText(f"""
                <html>
                <head/>
                    <body>
                        <p>
                        <span style=" color:#585858;">Archivo CSV seleccionado: {self.csv_file}</span>
                        </p>
                    </body>
                </html>
                """)
                self.populate_csv_table(self.csv_file)
        return super().dropEvent(event)

    def populate_csv_table(self, csv_file):
        csv_data = pd.read_csv(csv_file)
        table = self.parent.csv_table
        # table.resizeColumnsToContents()
        # table.resizeRowsToContents()
        table.setRowCount(len(csv_data))
        table.setColumnCount(len(csv_data.columns))
        table.setHorizontalHeaderLabels(csv_data.columns)
        for i in range(len(csv_data)):
            for j in range(len(csv_data.columns)):
                table.setItem(i, j, QTableWidgetItem(
                    str(csv_data.iat[i, j])))


# MDBDroppableFrame
class MDBDroppableFrame(QFrame):
    def __init__(self, parent):
        super(MDBDroppableFrame, self).__init__(parent)

        self.parent = parent
        self.setAcceptDrops(True)
        self.init_ui()

    def init_ui(self):
        self.verticalLayout_3 = QVBoxLayout()
        self.setObjectName("mdb_droppable_frame")
        self.setStyleSheet(
            """
        QFrame#mdb_droppable_frame {
        	border: 2px dotted grey;
	        padding: 20px;
        }
        """)
        self.setLayout(self.verticalLayout_3)
        self.mdb_title_label = QLabel()
        self.mdb_title_label.setText(
            """
        <html>
        <head/>
            <body>
                <p>
                    <span style=" color:#55557f;">Arrastra o selecciona archivo MDB</span>
                </p>
            </body>
        </html>
        """)
        self.mdb_title_label.setStyleSheet(
            "QLabel {font-size: 17px; font-weight: bold;}")
        self.mdb_title_label.setAlignment(Qt.AlignCenter)
        self.selected_mdb_file_label = QLabel()
        self.selected_mdb_file_label.setText(
            """
        <html>
        <head/>
            <body>
                <p>
                    <span style=" color:#585858;">Archivo MDB seleccionado:</span>
                    </p>
            </body>
        </html>
        """)
        self.selected_mdb_file_label.setMaximumHeight(35)
        self.selected_mdb_file_label.setStyleSheet("QLabel {font-size: 13px;}")
        self.selected_mdb_file_label.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.mdb_title_label)
        self.verticalLayout_3.addWidget(self.selected_mdb_file_label)

    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
        return super().dragEnterEvent(event)

    def dragMoveEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
        return super().dragMoveEvent(event)

    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            if event.mimeData().urls()[0].toString().endswith(".accdb"):
                event.setDropAction(Qt.CopyAction)
                event.accept()
                self.mdb_file = event.mimeData().urls()[0].toLocalFile()
                self.selected_mdb_file_label.setText(f"""
                <html>
                <head/>
                    <body>
                        <p>
                        <span style=" color:#585858;">Archivo MDB seleccionado: {self.mdb_file}</span>
                        </p>
                    </body>
                </html>
                """)
                self.parent.available_tables_combo.setEnabled(True)
        return super().dropEvent(event)


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

        self.csv_droppable_frame = CSVDroppableFrame(self)
        self.verticalLayout.addWidget(self.csv_droppable_frame)
        self.mdb_droppable_frame = MDBDroppableFrame(self)
        self.verticalLayout_2.addWidget(self.mdb_droppable_frame)

        self.clean_left_button.clicked.connect(
            lambda: self.clean_drop("left"))
        self.clean_right_button.clicked.connect(
            lambda: self.clean_drop("right"))

    def clean_drop(self, frame):
        if frame == "left":
            self.csv_droppable_frame.selected_csv_file_label.setText(
                """
            <html>
            <head/>
                <body>
                    <p>
                    <span style=" color:#585858;">Archivo MDB seleccionado:</span>
                    </p>
                </body>
            </html>
            """)
            self.csv_table.setRowCount(0)
            self.csv_table.setColumnCount(0)
            self.csv_table.resizeColumnsToContents()
            self.csv_table.clear()
        else:
            self.mdb_droppable_frame.selected_mdb_file_label.setText(
                """
            <html>
            <head/>
                <body>
                    <p>
                    <span style=" color:#585858;">Archivo MDB seleccionado:</span>
                    </p>
                </body>
            </html>
            """)
            self.mdb_table.setRowCount(0)

    def get_settings(self):
        self.w_attrib = QSettings("CSVToAccessGUI", "WindowAttributes")

    def set_settings(self):
        # Initial window size/pos last saved. Use default values for first time.
        self.resize(self.w_attrib.value("size", QSize(1000, 600)))
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
        event.accept()


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
