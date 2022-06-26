# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowNwXLaE.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 703)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {\n"
"	background: white;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_frame = QFrame(self.centralwidget)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 100))
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.title_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.title_label = QLabel(self.title_frame)
        self.title_label.setObjectName(u"title_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        self.title_label.setFont(font1)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.title_label)

        self.subtitle_label = QLabel(self.title_frame)
        self.subtitle_label.setObjectName(u"subtitle_label")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.subtitle_label.setFont(font2)
        self.subtitle_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.subtitle_label)


        self.verticalLayout_5.addWidget(self.title_frame)

        self.container_frame = QFrame(self.centralwidget)
        self.container_frame.setObjectName(u"container_frame")
        self.container_frame.setMinimumSize(QSize(0, 300))
        self.container_frame.setFrameShape(QFrame.StyledPanel)
        self.container_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.container_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.container_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addWidget(self.left_frame)

        self.image_label = QLabel(self.container_frame)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMaximumSize(QSize(64, 64))
        self.image_label.setPixmap(QPixmap(u":/res/right-arrow.png"))
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.image_label)

        self.right_frame = QFrame(self.container_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.combo_box_frame = QFrame(self.right_frame)
        self.combo_box_frame.setObjectName(u"combo_box_frame")
        self.combo_box_frame.setMaximumSize(QSize(16777215, 25))
        self.combo_box_frame.setFrameShape(QFrame.StyledPanel)
        self.combo_box_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.combo_box_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.selected_table_label = QLabel(self.combo_box_frame)
        self.selected_table_label.setObjectName(u"selected_table_label")
        self.selected_table_label.setMaximumSize(QSize(120, 16777215))
        self.selected_table_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.selected_table_label)

        self.available_tables_combo = QComboBox(self.combo_box_frame)
        self.available_tables_combo.setObjectName(u"available_tables_combo")
        self.available_tables_combo.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.available_tables_combo)


        self.verticalLayout_2.addWidget(self.combo_box_frame)


        self.horizontalLayout.addWidget(self.right_frame)


        self.verticalLayout_5.addWidget(self.container_frame)

        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(16777215, 60))
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line = QFrame(self.buttons_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.dump_data_button = QPushButton(self.buttons_frame)
        self.dump_data_button.setObjectName(u"dump_data_button")
        self.dump_data_button.setMinimumSize(QSize(0, 35))
        self.dump_data_button.setMaximumSize(QSize(300, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        self.dump_data_button.setFont(font3)
        self.dump_data_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/res/conversion-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dump_data_button.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.dump_data_button)

        self.show_hide_details_button = QPushButton(self.buttons_frame)
        self.show_hide_details_button.setObjectName(u"show_hide_details_button")
        self.show_hide_details_button.setMinimumSize(QSize(0, 35))
        self.show_hide_details_button.setMaximumSize(QSize(300, 16777215))
        self.show_hide_details_button.setFont(font3)
        self.show_hide_details_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/res/down.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/res/up.png", QSize(), QIcon.Normal, QIcon.On)
        self.show_hide_details_button.setIcon(icon1)
        self.show_hide_details_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.show_hide_details_button)

        self.line_2 = QFrame(self.buttons_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)


        self.verticalLayout_5.addWidget(self.buttons_frame)

        self.details_frame = QFrame(self.centralwidget)
        self.details_frame.setObjectName(u"details_frame")
        self.details_frame.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.details_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.table_widgets_container = QFrame(self.details_frame)
        self.table_widgets_container.setObjectName(u"table_widgets_container")
        self.table_widgets_container.setFrameShape(QFrame.StyledPanel)
        self.table_widgets_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.table_widgets_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table_left = QFrame(self.table_widgets_container)
        self.table_left.setObjectName(u"table_left")
        self.table_left.setFrameShape(QFrame.StyledPanel)
        self.table_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.table_left)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.csv_table_label = QLabel(self.table_left)
        self.csv_table_label.setObjectName(u"csv_table_label")

        self.verticalLayout_9.addWidget(self.csv_table_label)

        self.csv_table = QTableWidget(self.table_left)
        if (self.csv_table.columnCount() < 3):
            self.csv_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.csv_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.csv_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.csv_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.csv_table.rowCount() < 3):
            self.csv_table.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.csv_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.csv_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.csv_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.csv_table.setItem(0, 0, __qtablewidgetitem6)
        self.csv_table.setObjectName(u"csv_table")
        self.csv_table.setGridStyle(Qt.DashLine)

        self.verticalLayout_9.addWidget(self.csv_table)


        self.horizontalLayout_4.addWidget(self.table_left)

        self.table_right = QFrame(self.table_widgets_container)
        self.table_right.setObjectName(u"table_right")
        self.table_right.setFrameShape(QFrame.StyledPanel)
        self.table_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.table_right)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.mdb_table_label = QLabel(self.table_right)
        self.mdb_table_label.setObjectName(u"mdb_table_label")

        self.verticalLayout_8.addWidget(self.mdb_table_label)

        self.mdb_table = QTableWidget(self.table_right)
        if (self.mdb_table.columnCount() < 3):
            self.mdb_table.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.mdb_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.mdb_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.mdb_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        if (self.mdb_table.rowCount() < 3):
            self.mdb_table.setRowCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.mdb_table.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.mdb_table.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.mdb_table.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.mdb_table.setItem(0, 0, __qtablewidgetitem13)
        self.mdb_table.setObjectName(u"mdb_table")
        self.mdb_table.setGridStyle(Qt.DashLine)

        self.verticalLayout_8.addWidget(self.mdb_table)


        self.horizontalLayout_4.addWidget(self.table_right)


        self.verticalLayout_7.addWidget(self.table_widgets_container)

        self.output_label = QLabel(self.details_frame)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setFont(font)

        self.verticalLayout_7.addWidget(self.output_label)

        self.plainTextEdit = QPlainTextEdit(self.details_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 50))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.plainTextEdit)


        self.verticalLayout_5.addWidget(self.details_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CSVToAccessGUI", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ff8e00;\">CSVToAccessGUI</span></p></body></html>", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#585858;\">Vuelca los datos de tus archivos CSV a una base de datos MS Access f\u00e1cilmente</span></p></body></html>", None))
        self.selected_table_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#585858;\">Tabla seleccionada:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.available_tables_combo.setToolTip(QCoreApplication.translate("MainWindow", u"Selecciona una tabla del archivo mdb", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dump_data_button.setToolTip(QCoreApplication.translate("MainWindow", u"Vuelca los datos del archivo csv", None))
#endif // QT_CONFIG(tooltip)
        self.dump_data_button.setText(QCoreApplication.translate("MainWindow", u" Volcar datos", None))
#if QT_CONFIG(tooltip)
        self.show_hide_details_button.setToolTip(QCoreApplication.translate("MainWindow", u"Muestra u oculta detalles", None))
#endif // QT_CONFIG(tooltip)
        self.show_hide_details_button.setText(QCoreApplication.translate("MainWindow", u" Mostrar/Ocultar detalles", None))
        self.csv_table_label.setText(QCoreApplication.translate("MainWindow", u"Columnas del archivo CSV:", None))
        ___qtablewidgetitem = self.csv_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Columna 1", None));
        ___qtablewidgetitem1 = self.csv_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Columna 2", None));
        ___qtablewidgetitem2 = self.csv_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Columna 3", None));
        ___qtablewidgetitem3 = self.csv_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Fila 1", None));
        ___qtablewidgetitem4 = self.csv_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Fila 2", None));
        ___qtablewidgetitem5 = self.csv_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Fila 3", None));

        __sortingEnabled = self.csv_table.isSortingEnabled()
        self.csv_table.setSortingEnabled(False)
        self.csv_table.setSortingEnabled(__sortingEnabled)

        self.mdb_table_label.setText(QCoreApplication.translate("MainWindow", u"Columnas del archivo MDB:", None))
        ___qtablewidgetitem6 = self.mdb_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Columna 1", None));
        ___qtablewidgetitem7 = self.mdb_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Columna 2", None));
        ___qtablewidgetitem8 = self.mdb_table.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Columna 3", None));
        ___qtablewidgetitem9 = self.mdb_table.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fila 1", None));
        ___qtablewidgetitem10 = self.mdb_table.verticalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Fila 2", None));
        ___qtablewidgetitem11 = self.mdb_table.verticalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Fila 3", None));

        __sortingEnabled1 = self.mdb_table.isSortingEnabled()
        self.mdb_table.setSortingEnabled(False)
        self.mdb_table.setSortingEnabled(__sortingEnabled1)

        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
    # retranslateUi

