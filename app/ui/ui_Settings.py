# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsUJdrCa.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout)
import images_rc
import images_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(575, 400)
        Settings.setMaximumSize(QSize(800, 400))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        Settings.setFont(font)
        icon = QIcon()
        icon.addFile(u":/res/convert.png", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        Settings.setModal(True)
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(Settings)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMaximumSize(QSize(16777215, 100))
        self.top_frame.setStyleSheet(u"QFrame#top_frame {\n"
"	border-bottom: 1px solid #a0a0a0;\n"
"	background: white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.top_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, -1, 0)
        self.image_frame = QFrame(self.top_frame)
        self.image_frame.setObjectName(u"image_frame")
        self.image_frame.setMaximumSize(QSize(100, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.image_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.image_frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(64, 64))
        self.label.setPixmap(QPixmap(u":/res/gear.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.image_frame)

        self.frame = QFrame(self.top_frame)
        self.frame.setObjectName(u"frame")
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(9)
        self.title_label.setFont(font1)
        self.title_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.title_label)

        self.subtitle_label = QLabel(self.frame)
        self.subtitle_label.setObjectName(u"subtitle_label")
        self.subtitle_label.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(11)
        self.subtitle_label.setFont(font2)
        self.subtitle_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.subtitle_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(Settings)
        self.mid_frame.setObjectName(u"mid_frame")
        self.gridLayout = QGridLayout(self.mid_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.app_group_box = QGroupBox(self.mid_frame)
        self.app_group_box.setObjectName(u"app_group_box")
        self.verticalLayout_2 = QVBoxLayout(self.app_group_box)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_maximized_checkbox = QCheckBox(self.app_group_box)
        self.start_maximized_checkbox.setObjectName(u"start_maximized_checkbox")

        self.verticalLayout_2.addWidget(self.start_maximized_checkbox)

        self.show_output_checkbox = QCheckBox(self.app_group_box)
        self.show_output_checkbox.setObjectName(u"show_output_checkbox")
        self.show_output_checkbox.setChecked(True)

        self.verticalLayout_2.addWidget(self.show_output_checkbox)


        self.gridLayout.addWidget(self.app_group_box, 0, 0, 1, 1)

        self.appereance_group_box = QGroupBox(self.mid_frame)
        self.appereance_group_box.setObjectName(u"appereance_group_box")
        self.verticalLayout_5 = QVBoxLayout(self.appereance_group_box)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.defaulttheme_radiobtn = QRadioButton(self.appereance_group_box)
        self.defaulttheme_radiobtn.setObjectName(u"defaulttheme_radiobtn")
        self.defaulttheme_radiobtn.setChecked(True)

        self.verticalLayout_5.addWidget(self.defaulttheme_radiobtn)

        self.darktheme_radiobtn = QRadioButton(self.appereance_group_box)
        self.darktheme_radiobtn.setObjectName(u"darktheme_radiobtn")

        self.verticalLayout_5.addWidget(self.darktheme_radiobtn)


        self.gridLayout.addWidget(self.appereance_group_box, 0, 1, 1, 1)

        self.language_group_box = QGroupBox(self.mid_frame)
        self.language_group_box.setObjectName(u"language_group_box")
        self.verticalLayout_4 = QVBoxLayout(self.language_group_box)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.es_radiobtn = QRadioButton(self.language_group_box)
        self.es_radiobtn.setObjectName(u"es_radiobtn")
        self.es_radiobtn.setChecked(True)

        self.verticalLayout_4.addWidget(self.es_radiobtn)

        self.ca_radiobtn = QRadioButton(self.language_group_box)
        self.ca_radiobtn.setObjectName(u"ca_radiobtn")

        self.verticalLayout_4.addWidget(self.ca_radiobtn)

        self.en_radiobtn = QRadioButton(self.language_group_box)
        self.en_radiobtn.setObjectName(u"en_radiobtn")

        self.verticalLayout_4.addWidget(self.en_radiobtn)


        self.gridLayout.addWidget(self.language_group_box, 1, 0, 1, 2)


        self.verticalLayout.addWidget(self.mid_frame)

        self.btm_frame = QFrame(Settings)
        self.btm_frame.setObjectName(u"btm_frame")
        self.btm_frame.setMaximumSize(QSize(16777215, 75))
        self.btm_frame.setStyleSheet(u"QFrame#btm_frame {\n"
"	border-top: 1px solid #a0a0a0;\n"
"	background: white;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.btm_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(335, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.accept_button = QPushButton(self.btm_frame)
        self.accept_button.setObjectName(u"accept_button")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        self.accept_button.setFont(font3)
        self.accept_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.accept_button.setStyleSheet(u"QPushButton#accept_button {\n"
"	padding: 7px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.accept_button)

        self.apply_button = QPushButton(self.btm_frame)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setFont(font3)
        self.apply_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_button.setStyleSheet(u"QPushButton#apply_button {\n"
"	padding: 7px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.apply_button)

        self.cancel_button = QPushButton(self.btm_frame)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setFont(font3)
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet(u"QPushButton#cancel_button {\n"
"	padding: 7px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cancel_button)


        self.verticalLayout.addWidget(self.btm_frame)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.title_label.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ff8e00;\">Configuraci\u00f3n</span></p></body></html>", None))
        self.subtitle_label.setText(QCoreApplication.translate("Settings", u"<html><head/><body><p><span style=\" color:#585858;\">Modifica los par\u00e1metros de la aplicaci\u00f3n</span></p></body></html>", None))
        self.app_group_box.setTitle(QCoreApplication.translate("Settings", u"Aplicaci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.start_maximized_checkbox.setToolTip(QCoreApplication.translate("Settings", u"Iniciar aplicaci\u00f3n maximizada", None))
#endif // QT_CONFIG(tooltip)
        self.start_maximized_checkbox.setText(QCoreApplication.translate("Settings", u"Iniciar maximizado", None))
#if QT_CONFIG(tooltip)
        self.show_output_checkbox.setToolTip(QCoreApplication.translate("Settings", u"Mostrar output de operaciones", None))
#endif // QT_CONFIG(tooltip)
        self.show_output_checkbox.setText(QCoreApplication.translate("Settings", u"Mostrar output", None))
        self.appereance_group_box.setTitle(QCoreApplication.translate("Settings", u"Apariencia", None))
#if QT_CONFIG(tooltip)
        self.defaulttheme_radiobtn.setToolTip(QCoreApplication.translate("Settings", u"Tema predeterminado claro", None))
#endif // QT_CONFIG(tooltip)
        self.defaulttheme_radiobtn.setText(QCoreApplication.translate("Settings", u"Tema predeterminado", None))
#if QT_CONFIG(tooltip)
        self.darktheme_radiobtn.setToolTip(QCoreApplication.translate("Settings", u"Tema oscuro", None))
#endif // QT_CONFIG(tooltip)
        self.darktheme_radiobtn.setText(QCoreApplication.translate("Settings", u"Tema oscuro", None))
        self.language_group_box.setTitle(QCoreApplication.translate("Settings", u"Lenguaje", None))
#if QT_CONFIG(tooltip)
        self.es_radiobtn.setToolTip(QCoreApplication.translate("Settings", u"Espa\u00f1ol", None))
#endif // QT_CONFIG(tooltip)
        self.es_radiobtn.setText(QCoreApplication.translate("Settings", u"Espa\u00f1ol", None))
#if QT_CONFIG(tooltip)
        self.ca_radiobtn.setToolTip(QCoreApplication.translate("Settings", u"Catal\u00e1n", None))
#endif // QT_CONFIG(tooltip)
        self.ca_radiobtn.setText(QCoreApplication.translate("Settings", u"Catal\u00e1n", None))
#if QT_CONFIG(tooltip)
        self.en_radiobtn.setToolTip(QCoreApplication.translate("Settings", u"Ingl\u00e9s", None))
#endif // QT_CONFIG(tooltip)
        self.en_radiobtn.setText(QCoreApplication.translate("Settings", u"Ingl\u00e9s", None))
#if QT_CONFIG(tooltip)
        self.accept_button.setToolTip(QCoreApplication.translate("Settings", u"Aceptar y guardar", None))
#endif // QT_CONFIG(tooltip)
        self.accept_button.setText(QCoreApplication.translate("Settings", u"Aceptar", None))
#if QT_CONFIG(tooltip)
        self.apply_button.setToolTip(QCoreApplication.translate("Settings", u"Aplicar cambios", None))
#endif // QT_CONFIG(tooltip)
        self.apply_button.setText(QCoreApplication.translate("Settings", u"Aplicar cambios", None))
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("Settings", u"Cancelar", None))
#endif // QT_CONFIG(tooltip)
        self.cancel_button.setText(QCoreApplication.translate("Settings", u"Cancelar", None))
    # retranslateUi

