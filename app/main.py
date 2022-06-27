import sqlalchemy_access.pyodbc  # necessary import
import sys
import os
import subprocess
import pandas as pd
import pyodbc
import urllib

from sqlalchemy import create_engine
from datetime import datetime

from ui.ui_MainWindow import Ui_MainWindow

from PySide6.QtGui import QTextDocument, QTextCursor
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
    QTableWidgetItem,
    QFileDialog,
    QMessageBox,
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
        self.selected_csv_file_label.setMaximumHeight(35)
        self.selected_csv_file_label.setStyleSheet("QLabel {font-size: 13px;}")
        self.selected_csv_file_label.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.csv_title_label)
        self.verticalLayout_3.addWidget(self.selected_csv_file_label)
        self.setCursor(Qt.DragCopyCursor)

    def mousePressEvent(self, event) -> None:
        self.csv_mdb_path, _ = QFileDialog.getOpenFileName(
            self, "Abrir", "", "Archivo CSV (*.csv)")
        if self.csv_mdb_path == '' or not str(self.csv_mdb_path).endswith(".csv"):
            event.ignore()
            return
        else:
            self.selected_csv_file_label.setText(f"""
            <html>
            <head/>
                <body>
                    <p>
                    <span style=" color:#585858;">{self.csv_mdb_path}</span>
                    </p>
                </body>
            </html>
            """)
            self.populate_csv_table(self.csv_mdb_path)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.parent.output.insertPlainText(
                f"{current_time} - Loaded {self.csv_mdb_path} file successfully.\n")
            event.accept()
        return super().mousePressEvent(event)

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
                        <span style=" color:#585858;">{self.csv_file}</span>
                        </p>
                    </body>
                </html>
                """)
                self.populate_csv_table(self.csv_file)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.parent.output.insertPlainText(
                    f"{current_time} - Loaded {self.csv_file} file successfully.\n")
        return super().dropEvent(event)

    def populate_csv_table(self, csv_file):
        csv_data = pd.read_csv(csv_file)
        table = self.parent.csv_table
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
        self.selected_mdb_file_label.setMaximumHeight(35)
        self.selected_mdb_file_label.setStyleSheet("QLabel {font-size: 13px;}")
        self.selected_mdb_file_label.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.mdb_title_label)
        self.verticalLayout_3.addWidget(self.selected_mdb_file_label)
        self.setCursor(Qt.DragCopyCursor)

    def mousePressEvent(self, event) -> None:
        self.mdb_file, _ = QFileDialog.getOpenFileName(
            self, "Abrir", "", "Microsoft Access (*.accdb)")
        if self.mdb_file == '' or not str(self.mdb_file).endswith(".accdb"):
            event.ignore()
            return
        else:
            self.selected_mdb_file_label.setText(f"""
            <html>
            <head/>
                <body>
                    <p>
                    <span style=" color:#585858;">{self.mdb_file}</span>
                    </p>
                </body>
            </html>
            """)
            self.parent.available_tables_combo.setEnabled(True)
            con = pyodbc.connect(
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                f"DBQ={self.mdb_file}"
            )
            cur = con.cursor()
            # Making a list because I want to show user made tables first.
            table_list = []
            for row in cur.tables():
                table_list.append(row.table_name)
            # Reversing items in the list in order to show user made tables first.
            for table in reversed(table_list):
                self.parent.available_tables_combo.addItem(table)
            current_table = self.parent.available_tables_combo.currentText()
            self.populate_mdb_table(current_table)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.parent.output.insertPlainText(
                f"{current_time} - Loaded {self.mdb_file} file successfully.\n")
            event.accept()
        return super().mousePressEvent(event)

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
            # Checks if you are dropping a .accdb file.
            if event.mimeData().urls()[0].toString().endswith(".accdb"):
                event.setDropAction(Qt.CopyAction)
                event.accept()
                self.mdb_file = event.mimeData().urls()[0].toLocalFile()
                self.selected_mdb_file_label.setText(f"""
                <html>
                <head/>
                    <body>
                        <p>
                        <span style=" color:#585858;">{self.mdb_file}</span>
                        </p>
                    </body>
                </html>
                """)
                self.parent.available_tables_combo.setEnabled(True)
                con = pyodbc.connect(
                    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                    f"DBQ={self.mdb_file}"
                )
                cur = con.cursor()
                # Making a list because I want to show user made tables first.
                table_list = []
                for row in cur.tables():
                    table_list.append(row.table_name)
                # Reversing items in the list in order to show user made tables first.
                for table in reversed(table_list):
                    self.parent.available_tables_combo.addItem(table)
                current_table = self.parent.available_tables_combo.currentText()
                self.populate_mdb_table(current_table)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.parent.output.insertPlainText(
                    f"{current_time} - Loaded {self.mdb_file} file successfully.\n")
        return super().dropEvent(event)

    def populate_mdb_table(self, table_name):
        table = self.parent.mdb_table
        con = pyodbc.connect(
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={self.mdb_file}"
        )
        try:
            mdb_data = pd.read_sql(f"SELECT * FROM {table_name}", con)
        except Exception as e:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.parent.output.insertPlainText(
                f"{current_time} - {e}\n")
        table.setRowCount(len(mdb_data))
        table.setColumnCount(len(mdb_data.columns))
        table.setHorizontalHeaderLabels(mdb_data.columns)
        for i in range(len(mdb_data)):
            for j in range(len(mdb_data.columns)):
                table.setItem(i, j, QTableWidgetItem(str(mdb_data.iat[i, j])))


# MainWindow.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init_ui()
        self.show_details = True
        # Get app settings.
        self.get_settings()
        # Set app settings.
        self.set_settings()

        self.output.insertPlainText("--------- INIT APP ---------\n")
        self.output.insertPlainText(
            "--> Select a CSV and MS Access file to start <--\n")

    def init_ui(self):
        self.setupUi(self)

        self.csv_droppable_frame = CSVDroppableFrame(self)
        self.verticalLayout.addWidget(self.csv_droppable_frame)
        self.mdb_droppable_frame = MDBDroppableFrame(self)
        self.verticalLayout_2.addWidget(self.mdb_droppable_frame)

        self.dump_data_button.clicked.connect(self.dump_data)
        self.show_hide_details_button.clicked.connect(self.show_hide_details)
        self.clean_left_button.clicked.connect(
            lambda: self.clean_drop("left"))
        self.clean_right_button.clicked.connect(
            lambda: self.clean_drop("right"))
        self.available_tables_combo.currentIndexChanged.connect(
            lambda: self.mdb_droppable_frame.populate_mdb_table(self.available_tables_combo.currentText()))
        self.output.textChanged.connect(self.auto_scroll)
        self.copy_output_button.clicked.connect(self.copy_output)
        self.export_button.clicked.connect(self.save_output)
        self.clean_output_button.clicked.connect(self.clean_output)

    def dump_data(self):
        try:
            self.csv_file = self.csv_droppable_frame.selected_csv_file_label.text()
            self.mdb_file = self.mdb_droppable_frame.selected_mdb_file_label.text()
            convert_to_plain = QTextDocument()
            convert_to_plain.setHtml(self.csv_file)
            convert_to_plain_2 = QTextDocument()
            convert_to_plain_2.setHtml(self.mdb_file)
            csv_file = convert_to_plain.toPlainText()
            mdb_file = convert_to_plain_2.toPlainText()
            # If the two file exist.
            if csv_file and mdb_file:
                ret = QMessageBox.question(
                    self, "Confirmar acción", f"¿Seguro que quieres realizar esta acción? Esto podría sobreescribir todos los datos de la tabla ('{self.available_tables_combo.currentText()}').")
                if ret == QMessageBox.Yes:
                    df = pd.read_csv(csv_file)
                    table = self.available_tables_combo.currentText()
                    cnn_str = (
                        r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                        f"DBQ={mdb_file}"
                    )
                    cnn_url = f"access+pyodbc:///?odbc_connect={urllib.parse.quote_plus(cnn_str)}"
                    acc_engine = create_engine(cnn_url)
                    df.to_sql(f"{table}", acc_engine,
                              if_exists='replace', index=False)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    self.output.insertPlainText(
                        f"--------- WRITE COMPLETED ---------\n")
                    # Refresh table with new data.
                    self.mdb_droppable_frame.populate_mdb_table(table)
        except Exception as e:
            self.output.insertPlainText(f"--------- ERROR ---------\n{e}")

    def clean_output(self):
        self.output.clear()

    def copy_output(self):
        self.output.selectAll()
        self.output.copy()

    def auto_scroll(self):
        if self.auto_scroll_checkbox.isChecked():
            self.output.moveCursor(QTextCursor.End)

    def save_output(self):
        self.path, _ = QFileDialog.getSaveFileName(
            self, "Guardar como", "output.txt", "Documentos de texto (*.txt)",)
        if self.path == '':
            return
        text = self.output.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
        except Exception as e:
            print(e)
            QMessageBox.critical(
                self, "Error de guardado", f"No se ha podido guardar el archivo en {self.path}")

    def clean_drop(self, frame):
        if frame == "left":
            self.csv_droppable_frame.selected_csv_file_label.setText("")
            self.csv_table.setRowCount(0)
            self.csv_table.setColumnCount(0)
            self.csv_table.resizeColumnsToContents()
            self.csv_table.clear()
        else:
            self.mdb_droppable_frame.selected_mdb_file_label.setText("")
            self.available_tables_combo.setEnabled(False)
            self.available_tables_combo.clear()
            self.mdb_table.setRowCount(0)
            self.mdb_table.setColumnCount(0)
            self.mdb_table.resizeColumnsToContents()
            self.mdb_table.clear()

    def show_hide_details(self):
        # If currently showing details.
        if self.show_details:
            self.details_frame.hide()
            self.show_details = False
        else:
            self.details_frame.show()
            self.show_details = True

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
