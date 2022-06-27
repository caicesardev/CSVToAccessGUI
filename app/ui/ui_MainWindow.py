# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowFJxGdL.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 734)
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
        self.title_frame.setMaximumSize(QSize(16777215, 135))
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

        self.frame = QFrame(self.title_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(865, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.help_button = QPushButton(self.frame)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/res/question.png", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon)
        self.help_button.setIconSize(QSize(20, 20))
        self.help_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.help_button)

        self.settings_button = QPushButton(self.frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/res/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setIconSize(QSize(20, 20))
        self.settings_button.setFlat(True)

        self.horizontalLayout_8.addWidget(self.settings_button)


        self.verticalLayout_6.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.title_frame)

        self.container_frame = QFrame(self.centralwidget)
        self.container_frame.setObjectName(u"container_frame")
        self.container_frame.setMinimumSize(QSize(0, 240))
        self.horizontalLayout = QHBoxLayout(self.container_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.container_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.clean_frame = QFrame(self.left_frame)
        self.clean_frame.setObjectName(u"clean_frame")
        self.clean_frame.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_5 = QHBoxLayout(self.clean_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(364, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.clean_left_button = QPushButton(self.clean_frame)
        self.clean_left_button.setObjectName(u"clean_left_button")
        self.clean_left_button.setMinimumSize(QSize(0, 30))
        self.clean_left_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/res/cleaning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clean_left_button.setIcon(icon2)
        self.clean_left_button.setIconSize(QSize(32, 32))
        self.clean_left_button.setFlat(True)

        self.horizontalLayout_5.addWidget(self.clean_left_button)


        self.verticalLayout.addWidget(self.clean_frame)


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
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.clean_frame_2 = QFrame(self.right_frame)
        self.clean_frame_2.setObjectName(u"clean_frame_2")
        self.clean_frame_2.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_6 = QHBoxLayout(self.clean_frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_2 = QSpacerItem(364, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.clean_right_button = QPushButton(self.clean_frame_2)
        self.clean_right_button.setObjectName(u"clean_right_button")
        self.clean_right_button.setMinimumSize(QSize(0, 30))
        self.clean_right_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.clean_right_button.setIcon(icon2)
        self.clean_right_button.setIconSize(QSize(32, 32))
        self.clean_right_button.setFlat(True)

        self.horizontalLayout_6.addWidget(self.clean_right_button)


        self.verticalLayout_2.addWidget(self.clean_frame_2)

        self.combo_box_frame = QFrame(self.right_frame)
        self.combo_box_frame.setObjectName(u"combo_box_frame")
        self.combo_box_frame.setMaximumSize(QSize(16777215, 25))
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
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(9)
        self.available_tables_combo.setFont(font3)

        self.horizontalLayout_3.addWidget(self.available_tables_combo)


        self.verticalLayout_2.addWidget(self.combo_box_frame)


        self.horizontalLayout.addWidget(self.right_frame)

        self.image_label.raise_()
        self.left_frame.raise_()
        self.right_frame.raise_()

        self.verticalLayout_5.addWidget(self.container_frame)

        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(16777215, 60))
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
        font4 = QFont()
        font4.setPointSize(10)
        self.dump_data_button.setFont(font4)
        self.dump_data_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/res/conversion-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dump_data_button.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.dump_data_button)

        self.show_hide_details_button = QPushButton(self.buttons_frame)
        self.show_hide_details_button.setObjectName(u"show_hide_details_button")
        self.show_hide_details_button.setMinimumSize(QSize(0, 35))
        self.show_hide_details_button.setMaximumSize(QSize(300, 16777215))
        self.show_hide_details_button.setFont(font4)
        self.show_hide_details_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/res/down.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/res/up.png", QSize(), QIcon.Normal, QIcon.On)
        self.show_hide_details_button.setIcon(icon4)
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
        self.horizontalLayout_4 = QHBoxLayout(self.table_widgets_container)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.table_left = QFrame(self.table_widgets_container)
        self.table_left.setObjectName(u"table_left")
        self.verticalLayout_9 = QVBoxLayout(self.table_left)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.csv_table_label = QLabel(self.table_left)
        self.csv_table_label.setObjectName(u"csv_table_label")

        self.verticalLayout_9.addWidget(self.csv_table_label)

        self.csv_table = QTableWidget(self.table_left)
        self.csv_table.setObjectName(u"csv_table")
        self.csv_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.csv_table.setAlternatingRowColors(True)
        self.csv_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.csv_table.verticalHeader().setVisible(False)

        self.verticalLayout_9.addWidget(self.csv_table)


        self.horizontalLayout_4.addWidget(self.table_left)

        self.table_right = QFrame(self.table_widgets_container)
        self.table_right.setObjectName(u"table_right")
        self.verticalLayout_8 = QVBoxLayout(self.table_right)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.mdb_table_label = QLabel(self.table_right)
        self.mdb_table_label.setObjectName(u"mdb_table_label")

        self.verticalLayout_8.addWidget(self.mdb_table_label)

        self.mdb_table = QTableWidget(self.table_right)
        self.mdb_table.setObjectName(u"mdb_table")
        self.mdb_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.mdb_table.setAlternatingRowColors(True)
        self.mdb_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.mdb_table.setGridStyle(Qt.DashLine)
        self.mdb_table.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.mdb_table)


        self.horizontalLayout_4.addWidget(self.table_right)


        self.verticalLayout_7.addWidget(self.table_widgets_container)

        self.output_label = QLabel(self.details_frame)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setFont(font)

        self.verticalLayout_7.addWidget(self.output_label)

        self.output = QPlainTextEdit(self.details_frame)
        self.output.setObjectName(u"output")
        self.output.setMaximumSize(QSize(16777215, 200))
        self.output.setFont(font)
        self.output.setUndoRedoEnabled(False)
        self.output.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.output)

        self.output_buttons_frame = QFrame(self.details_frame)
        self.output_buttons_frame.setObjectName(u"output_buttons_frame")
        self.horizontalLayout_7 = QHBoxLayout(self.output_buttons_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.auto_scroll_checkbox = QCheckBox(self.output_buttons_frame)
        self.auto_scroll_checkbox.setObjectName(u"auto_scroll_checkbox")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        self.auto_scroll_checkbox.setFont(font5)
        self.auto_scroll_checkbox.setChecked(True)

        self.horizontalLayout_7.addWidget(self.auto_scroll_checkbox)

        self.clean_output_button = QPushButton(self.output_buttons_frame)
        self.clean_output_button.setObjectName(u"clean_output_button")
        self.clean_output_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.clean_output_button.setIcon(icon2)
        self.clean_output_button.setIconSize(QSize(18, 18))
        self.clean_output_button.setFlat(True)

        self.horizontalLayout_7.addWidget(self.clean_output_button)

        self.copy_output_button = QPushButton(self.output_buttons_frame)
        self.copy_output_button.setObjectName(u"copy_output_button")
        self.copy_output_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/res/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_output_button.setIcon(icon5)
        self.copy_output_button.setIconSize(QSize(18, 18))
        self.copy_output_button.setFlat(True)

        self.horizontalLayout_7.addWidget(self.copy_output_button)

        self.export_button = QPushButton(self.output_buttons_frame)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setMinimumSize(QSize(0, 0))
        self.export_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.export_button.setStyleSheet(u"QPushButton#export_button {\n"
"	padding: 5px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/res/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_button.setIcon(icon6)
        self.export_button.setIconSize(QSize(18, 18))
        self.export_button.setFlat(True)

        self.horizontalLayout_7.addWidget(self.export_button)


        self.verticalLayout_7.addWidget(self.output_buttons_frame)


        self.verticalLayout_5.addWidget(self.details_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CSVToAccessGUI", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ff8e00;\">CSVToAccessGUI</span></p></body></html>", None))
        self.subtitle_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#585858;\">Vuelca los datos de tus archivos CSV a una base de datos MS Access f\u00e1cilmente</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.help_button.setToolTip(QCoreApplication.translate("MainWindow", u"Acerca de/Ayuda", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.settings_button.setToolTip(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.clean_left_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar input", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.clean_right_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar input", None))
#endif // QT_CONFIG(tooltip)
        self.clean_right_button.setText("")
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
        self.mdb_table_label.setText(QCoreApplication.translate("MainWindow", u"Columnas del archivo MDB:", None))
        self.output_label.setText(QCoreApplication.translate("MainWindow", u"Output:", None))
#if QT_CONFIG(tooltip)
        self.auto_scroll_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Activar scroll autom\u00e1tico", None))
#endif // QT_CONFIG(tooltip)
        self.auto_scroll_checkbox.setText(QCoreApplication.translate("MainWindow", u"Scroll autom\u00e1tico", None))
#if QT_CONFIG(tooltip)
        self.clean_output_button.setToolTip(QCoreApplication.translate("MainWindow", u"Limpiar output", None))
#endif // QT_CONFIG(tooltip)
        self.clean_output_button.setText("")
#if QT_CONFIG(tooltip)
        self.copy_output_button.setToolTip(QCoreApplication.translate("MainWindow", u"Copiar output", None))
#endif // QT_CONFIG(tooltip)
        self.copy_output_button.setText("")
#if QT_CONFIG(tooltip)
        self.export_button.setToolTip(QCoreApplication.translate("MainWindow", u"Guardar output", None))
#endif // QT_CONFIG(tooltip)
        self.export_button.setText("")
    # retranslateUi

