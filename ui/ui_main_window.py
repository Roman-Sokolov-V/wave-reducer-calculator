# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1019, 568)
        MainWindow.setMinimumSize(QSize(100, 100))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.all = QVBoxLayout()
        self.all.setObjectName(u"all")
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.menu_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_15 = QLabel(self.menu_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout.addWidget(self.label_15)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.menu_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.horizontalLayout.addWidget(self.label)

        self.ball_number = QSpinBox(self.menu_frame)
        self.ball_number.setObjectName(u"ball_number")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ball_number.sizePolicy().hasHeightForWidth())
        self.ball_number.setSizePolicy(sizePolicy)
        self.ball_number.setMouseTracking(False)
        self.ball_number.setWrapping(False)
        self.ball_number.setFrame(True)
        self.ball_number.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ball_number.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.ball_number.setProperty(u"showGroupSeparator", False)
        self.ball_number.setMinimum(2)
        self.ball_number.setValue(5)

        self.horizontalLayout.addWidget(self.ball_number)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ball_diameter = QDoubleSpinBox(self.menu_frame)
        self.ball_diameter.setObjectName(u"ball_diameter")
        sizePolicy.setHeightForWidth(self.ball_diameter.sizePolicy().hasHeightForWidth())
        self.ball_diameter.setSizePolicy(sizePolicy)
        self.ball_diameter.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.ball_diameter.setMinimum(3.000000000000000)
        self.ball_diameter.setSingleStep(0.100000000000000)

        self.horizontalLayout_3.addWidget(self.ball_diameter)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.track_outer_radius = QSpinBox(self.menu_frame)
        self.track_outer_radius.setObjectName(u"track_outer_radius")
        sizePolicy.setHeightForWidth(self.track_outer_radius.sizePolicy().hasHeightForWidth())
        self.track_outer_radius.setSizePolicy(sizePolicy)
        self.track_outer_radius.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.track_outer_radius.setMinimum(0)
        self.track_outer_radius.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.track_outer_radius.setValue(0)

        self.horizontalLayout_4.addWidget(self.track_outer_radius)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.reducer_outer_diameter = QSpinBox(self.menu_frame)
        self.reducer_outer_diameter.setObjectName(u"reducer_outer_diameter")
        sizePolicy.setHeightForWidth(self.reducer_outer_diameter.sizePolicy().hasHeightForWidth())
        self.reducer_outer_diameter.setSizePolicy(sizePolicy)
        self.reducer_outer_diameter.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.reducer_outer_diameter.setMinimum(0)
        self.reducer_outer_diameter.setValue(0)

        self.horizontalLayout_5.addWidget(self.reducer_outer_diameter)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.resolution = QSpinBox(self.menu_frame)
        self.resolution.setObjectName(u"resolution")
        sizePolicy.setHeightForWidth(self.resolution.sizePolicy().hasHeightForWidth())
        self.resolution.setSizePolicy(sizePolicy)
        self.resolution.setStyleSheet(u"")
        self.resolution.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)

        self.horizontalLayout_6.addWidget(self.resolution)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.visualize_pushButton = QPushButton(self.menu_frame)
        self.visualize_pushButton.setObjectName(u"visualize_pushButton")
        self.visualize_pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 0, 100), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 170, 0);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.visualize_pushButton)

        self.verticalLayout_2.setStretch(0, 6)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_16 = QLabel(self.menu_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.verticalLayout_3.addWidget(self.label_16)

        self.widget = QWidget(self.menu_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")
        self.horizontalLayout_7 = QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.checkBox_eccentric = QCheckBox(self.widget)
        self.checkBox_eccentric.setObjectName(u"checkBox_eccentric")
        self.checkBox_eccentric.setStyleSheet(u"")
        self.checkBox_eccentric.setChecked(True)
        self.checkBox_eccentric.setTristate(False)

        self.horizontalLayout_7.addWidget(self.checkBox_eccentric)

        self.checkBox_separator = QCheckBox(self.widget)
        self.checkBox_separator.setObjectName(u"checkBox_separator")
        self.checkBox_separator.setAutoFillBackground(False)
        self.checkBox_separator.setStyleSheet(u"")
        self.checkBox_separator.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_separator)

        self.checkBox_balls = QCheckBox(self.widget)
        self.checkBox_balls.setObjectName(u"checkBox_balls")
        self.checkBox_balls.setStyleSheet(u"")
        self.checkBox_balls.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_balls)

        self.checkBox_track = QCheckBox(self.widget)
        self.checkBox_track.setObjectName(u"checkBox_track")
        self.checkBox_track.setChecked(True)

        self.horizontalLayout_7.addWidget(self.checkBox_track)


        self.verticalLayout_3.addWidget(self.widget)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.export_pushButton = QPushButton(self.menu_frame)
        self.export_pushButton.setObjectName(u"export_pushButton")
        self.export_pushButton.setStyleSheet(u"QPushButton {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 170, 0, 100), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 170, 0);\n"
"}")

        self.verticalLayout_4.addWidget(self.export_pushButton)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_11)

        self.plotContainer = QWidget(self.menu_frame)
        self.plotContainer.setObjectName(u"plotContainer")
        self.plotContainer.setMinimumSize(QSize(300, 200))
        self.plotContainer.setAutoFillBackground(False)
        self.plotContainer.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")

        self.horizontalLayout_2.addWidget(self.plotContainer)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 3)

        self.all.addWidget(self.menu_frame)

        self.notifications = QLabel(self.centralwidget)
        self.notifications.setObjectName(u"notifications")
        self.notifications.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 255, 255));")

        self.all.addWidget(self.notifications)

        self.all.setStretch(0, 10)
        self.all.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.all)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wave Reducer Calculator", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Resucer Parameters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ball number", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ball diameter", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"track outer radius", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"reducer outer diameter", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"resolution", None))
        self.visualize_pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate & Visualize", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Export Options", None))
        self.checkBox_eccentric.setText(QCoreApplication.translate("MainWindow", u"eccentric", None))
        self.checkBox_separator.setText(QCoreApplication.translate("MainWindow", u"separator", None))
        self.checkBox_balls.setText(QCoreApplication.translate("MainWindow", u"balls", None))
        self.checkBox_track.setText(QCoreApplication.translate("MainWindow", u"track", None))
        self.export_pushButton.setText(QCoreApplication.translate("MainWindow", u"Export to DXF", None))
        self.notifications.setText(QCoreApplication.translate("MainWindow", u"notifications", None))
    # retranslateUi

