# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutPooXwO.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout)
import images_rc
import images_rc

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(800, 540)
        About.setMinimumSize(QSize(800, 540))
        About.setMaximumSize(QSize(800, 540))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        About.setFont(font)
        About.setModal(True)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(About)
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
        self.label.setPixmap(QPixmap(u":/res/question.png"))
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

        self.mid_frame = QFrame(About)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setMaximumSize(QSize(800, 400))
        self.gridLayout = QGridLayout(self.mid_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.frame_3 = QFrame(self.mid_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setOpenExternalLinks(True)

        self.verticalLayout_7.addWidget(self.label_4)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)


        self.verticalLayout_6.addWidget(self.groupBox_2)


        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.mid_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 9, -1, 0)
        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setOpenExternalLinks(True)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.mid_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.groupBox_3 = QGroupBox(self.frame_5)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_5)


        self.verticalLayout_8.addWidget(self.groupBox_3)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 2)

        self.frame_4 = QFrame(self.mid_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.subtitle_label_2 = QLabel(self.frame_4)
        self.subtitle_label_2.setObjectName(u"subtitle_label_2")
        self.subtitle_label_2.setMaximumSize(QSize(16777215, 20))
        self.subtitle_label_2.setFont(font2)
        self.subtitle_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.subtitle_label_2)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 2)

        self.frame_6 = QFrame(self.mid_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 6)
        self.groupBox_4 = QGroupBox(self.frame_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.about_qt_button = QPushButton(self.groupBox_4)
        self.about_qt_button.setObjectName(u"about_qt_button")
        self.about_qt_button.setMinimumSize(QSize(400, 0))
        self.about_qt_button.setFont(font)
        self.about_qt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.about_qt_button.setStyleSheet(u"QPushButton#about_qt_button {\n"
"	padding: 7px;\n"
"}")
        self.about_qt_button.setFlat(False)

        self.horizontalLayout_4.addWidget(self.about_qt_button)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addWidget(self.groupBox_4)


        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 2)


        self.verticalLayout.addWidget(self.mid_frame)

        self.btm_frame = QFrame(About)
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


        self.verticalLayout.addWidget(self.btm_frame)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"About", None))
        self.title_label.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:20pt; color:#ff8e00;\">Acerca de / Ayuda</span></p></body></html>", None))
        self.subtitle_label.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" color:#585858;\">Acerca de la aplicaci\u00f3n y ayuda</span></p></body></html>", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("About", u"Ayuda", None))
        self.label_4.setText(QCoreApplication.translate("About", u"Repositorio: <a href=\"https://github.com/caicesardev/CSVToAccessGUI\">https://github/caicesardev/CSVToAccessGUI<a>", None))
        self.label_6.setText(QCoreApplication.translate("About", u"Manual: <a href=\"https://github.com/caicesardev/CSVToAccessGUI\">https://github/caicesardev/CSVToAccessGUI/<a>", None))
        self.groupBox.setTitle(QCoreApplication.translate("About", u"Desarrolladores", None))
        self.label_3.setText(QCoreApplication.translate("About", u"caicesardev - <a href=\"mailto:caicesardev@gmail.com\"> caicesardev@gmail.com </a>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("About", u"Licencia", None))
        self.label_5.setText(QCoreApplication.translate("About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#585858;\">MIT License Copyright (c) 2022 Caio Gomes Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notic"
                        "e and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. </span></p></body></html>", None))
        self.subtitle_label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" font-size:16pt; color:#585858;\">CSVToAccessGUI</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><p><span style=\" color:#585858;\">Compilaci\u00f3n 28062022 v1.0.0</span></p></body></html>", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("About", u"Qt", None))
        self.about_qt_button.setText(QCoreApplication.translate("About", u"Acerca de Qt", None))
#if QT_CONFIG(tooltip)
        self.accept_button.setToolTip(QCoreApplication.translate("About", u"Aceptar y guardar", None))
#endif // QT_CONFIG(tooltip)
        self.accept_button.setText(QCoreApplication.translate("About", u"Aceptar", None))
    # retranslateUi

