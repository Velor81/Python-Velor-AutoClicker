# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(788, 690)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.help_bt = QPushButton(self.horizontalFrame)
        self.help_bt.setObjectName(u"help_bt")

        self.horizontalLayout_5.addWidget(self.help_bt, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.verticalFrame_6 = QFrame(self.centralwidget)
        self.verticalFrame_6.setObjectName(u"verticalFrame_6")
        self.horizontalLayout = QHBoxLayout(self.verticalFrame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_2 = QFrame(self.verticalFrame_6)
        self.verticalFrame_2.setObjectName(u"verticalFrame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.verticalFrame_2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_2.setSizePolicy(sizePolicy1)
        self.verticalFrame_2.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggle_keys_group = QGroupBox(self.verticalFrame_2)
        self.toggle_keys_group.setObjectName(u"toggle_keys_group")
        self.toggle_keys_group.setMinimumSize(QSize(220, 0))
        self.toggle_keys_group.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.toggle_keys_group)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.save_toggle_keys_bt = QPushButton(self.toggle_keys_group)
        self.save_toggle_keys_bt.setObjectName(u"save_toggle_keys_bt")

        self.verticalLayout_5.addWidget(self.save_toggle_keys_bt)

        self.start_stop_label = QLabel(self.toggle_keys_group)
        self.start_stop_label.setObjectName(u"start_stop_label")

        self.verticalLayout_5.addWidget(self.start_stop_label)

        self.toggle_start_stop_edit = QLineEdit(self.toggle_keys_group)
        self.toggle_start_stop_edit.setObjectName(u"toggle_start_stop_edit")

        self.verticalLayout_5.addWidget(self.toggle_start_stop_edit)


        self.verticalLayout_4.addWidget(self.toggle_keys_group)

        self.delay_group = QGroupBox(self.verticalFrame_2)
        self.delay_group.setObjectName(u"delay_group")
        self.horizontalLayout_3 = QHBoxLayout(self.delay_group)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.delay_edit = QLineEdit(self.delay_group)
        self.delay_edit.setObjectName(u"delay_edit")

        self.horizontalLayout_3.addWidget(self.delay_edit)


        self.verticalLayout_4.addWidget(self.delay_group)

        self.verticalGroupBox_3 = QGroupBox(self.verticalFrame_2)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        self.verticalGroupBox_3.setMinimumSize(QSize(220, 0))
        self.verticalGroupBox_3.setMaximumSize(QSize(220, 16777215))
        self.add_key_group = QVBoxLayout(self.verticalGroupBox_3)
        self.add_key_group.setSpacing(4)
        self.add_key_group.setObjectName(u"add_key_group")
        self.add_key_group.setContentsMargins(9, 9, 9, 9)
        self.verticalFrame_4 = QFrame(self.verticalGroupBox_3)
        self.verticalFrame_4.setObjectName(u"verticalFrame_4")
        self.verticalLayout_6 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.add_key_group.addWidget(self.verticalFrame_4)

        self.add_delay_item_edit = QLineEdit(self.verticalGroupBox_3)
        self.add_delay_item_edit.setObjectName(u"add_delay_item_edit")

        self.add_key_group.addWidget(self.add_delay_item_edit)

        self.add_delay_item_bt = QPushButton(self.verticalGroupBox_3)
        self.add_delay_item_bt.setObjectName(u"add_delay_item_bt")

        self.add_key_group.addWidget(self.add_delay_item_bt)

        self.line = QFrame(self.verticalGroupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.add_key_group.addWidget(self.line)

        self.label_2 = QLabel(self.verticalGroupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.add_key_group.addWidget(self.label_2)

        self.add_key_edit = QLineEdit(self.verticalGroupBox_3)
        self.add_key_edit.setObjectName(u"add_key_edit")
        self.add_key_edit.setClearButtonEnabled(True)

        self.add_key_group.addWidget(self.add_key_edit)

        self.verticalFrame_5 = QFrame(self.verticalGroupBox_3)
        self.verticalFrame_5.setObjectName(u"verticalFrame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalFrame_5.sizePolicy().hasHeightForWidth())
        self.verticalFrame_5.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.verticalFrame_5)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add_key_bt = QPushButton(self.verticalFrame_5)
        self.add_key_bt.setObjectName(u"add_key_bt")

        self.horizontalLayout_2.addWidget(self.add_key_bt)


        self.add_key_group.addWidget(self.verticalFrame_5, 0, Qt.AlignmentFlag.AlignTop)

        self.line_2 = QFrame(self.verticalGroupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.add_key_group.addWidget(self.line_2)

        self.label = QLabel(self.verticalGroupBox_3)
        self.label.setObjectName(u"label")

        self.add_key_group.addWidget(self.label)

        self.horizontalFrame1 = QFrame(self.verticalGroupBox_3)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.verticalLayout_7 = QVBoxLayout(self.horizontalFrame1)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.add_mouse_left_click_bt = QPushButton(self.horizontalFrame1)
        self.add_mouse_left_click_bt.setObjectName(u"add_mouse_left_click_bt")

        self.verticalLayout_7.addWidget(self.add_mouse_left_click_bt)

        self.add_mouse_right_click_bt = QPushButton(self.horizontalFrame1)
        self.add_mouse_right_click_bt.setObjectName(u"add_mouse_right_click_bt")

        self.verticalLayout_7.addWidget(self.add_mouse_right_click_bt)


        self.add_key_group.addWidget(self.horizontalFrame1)

        self.horizontalFrame2 = QFrame(self.verticalGroupBox_3)
        self.horizontalFrame2.setObjectName(u"horizontalFrame2")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.add_left_hold_bt = QPushButton(self.horizontalFrame2)
        self.add_left_hold_bt.setObjectName(u"add_left_hold_bt")

        self.horizontalLayout_4.addWidget(self.add_left_hold_bt)

        self.add_left_hold_lineEdit = QLineEdit(self.horizontalFrame2)
        self.add_left_hold_lineEdit.setObjectName(u"add_left_hold_lineEdit")

        self.horizontalLayout_4.addWidget(self.add_left_hold_lineEdit)


        self.add_key_group.addWidget(self.horizontalFrame2)

        self.horizontalFrame_2 = QFrame(self.verticalGroupBox_3)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.add_right_hold_bt = QPushButton(self.horizontalFrame_2)
        self.add_right_hold_bt.setObjectName(u"add_right_hold_bt")

        self.horizontalLayout_6.addWidget(self.add_right_hold_bt)

        self.add_right_hold_lineEdit = QLineEdit(self.horizontalFrame_2)
        self.add_right_hold_lineEdit.setObjectName(u"add_right_hold_lineEdit")

        self.horizontalLayout_6.addWidget(self.add_right_hold_lineEdit)


        self.add_key_group.addWidget(self.horizontalFrame_2)


        self.verticalLayout_4.addWidget(self.verticalGroupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalFrame = QFrame(self.verticalFrame_2)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.status_running_or_idle_label = QLabel(self.verticalFrame)
        self.status_running_or_idle_label.setObjectName(u"status_running_or_idle_label")
        font = QFont()
        font.setPointSize(18)
        self.status_running_or_idle_label.setFont(font)
        self.status_running_or_idle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.status_running_or_idle_label)


        self.verticalLayout_4.addWidget(self.verticalFrame)

        self.start_stop_bt = QPushButton(self.verticalFrame_2)
        self.start_stop_bt.setObjectName(u"start_stop_bt")
        self.start_stop_bt.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.start_stop_bt)


        self.horizontalLayout.addWidget(self.verticalFrame_2)

        self.keys_listWidget = QListWidget(self.verticalFrame_6)
        self.keys_listWidget.setObjectName(u"keys_listWidget")

        self.horizontalLayout.addWidget(self.keys_listWidget)

        self.move_up_down_group = QFrame(self.verticalFrame_6)
        self.move_up_down_group.setObjectName(u"move_up_down_group")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.move_up_down_group.sizePolicy().hasHeightForWidth())
        self.move_up_down_group.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.move_up_down_group)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.remove_key_bt = QPushButton(self.move_up_down_group)
        self.remove_key_bt.setObjectName(u"remove_key_bt")
        self.remove_key_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.remove_key_bt)

        self.move_up_bt = QPushButton(self.move_up_down_group)
        self.move_up_bt.setObjectName(u"move_up_bt")
        sizePolicy3.setHeightForWidth(self.move_up_bt.sizePolicy().hasHeightForWidth())
        self.move_up_bt.setSizePolicy(sizePolicy3)
        self.move_up_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.move_up_bt)

        self.move_down_bt = QPushButton(self.move_up_down_group)
        self.move_down_bt.setObjectName(u"move_down_bt")
        sizePolicy3.setHeightForWidth(self.move_down_bt.sizePolicy().hasHeightForWidth())
        self.move_down_bt.setSizePolicy(sizePolicy3)
        self.move_down_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.move_down_bt)

        self.clear_key_bt = QPushButton(self.move_up_down_group)
        self.clear_key_bt.setObjectName(u"clear_key_bt")
        self.clear_key_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.clear_key_bt)


        self.horizontalLayout.addWidget(self.move_up_down_group)


        self.verticalLayout_2.addWidget(self.verticalFrame_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.help_bt.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toggle_keys_group.setTitle(QCoreApplication.translate("MainWindow", u"Toggle Keys", None))
        self.save_toggle_keys_bt.setText(QCoreApplication.translate("MainWindow", u"Save Toggle Keys", None))
        self.start_stop_label.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.toggle_start_stop_edit.setText(QCoreApplication.translate("MainWindow", u"f8", None))
        self.toggle_start_stop_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"f8", None))
        self.delay_group.setTitle(QCoreApplication.translate("MainWindow", u"Clicks delay on all keys", None))
        self.delay_edit.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.delay_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.verticalGroupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Add item", None))
        self.add_delay_item_edit.setText(QCoreApplication.translate("MainWindow", u"5.0", None))
        self.add_delay_item_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"5.0", None))
        self.add_delay_item_bt.setText(QCoreApplication.translate("MainWindow", u"Add Delay", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add key click", None))
        self.add_key_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter key", None))
        self.add_key_bt.setText(QCoreApplication.translate("MainWindow", u"Add Key", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add mouse click", None))
        self.add_mouse_left_click_bt.setText(QCoreApplication.translate("MainWindow", u"Left Click", None))
        self.add_mouse_right_click_bt.setText(QCoreApplication.translate("MainWindow", u"Right Click", None))
        self.add_left_hold_bt.setText(QCoreApplication.translate("MainWindow", u"Left Hold", None))
        self.add_left_hold_lineEdit.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.add_left_hold_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.add_right_hold_bt.setText(QCoreApplication.translate("MainWindow", u"Right Hold", None))
        self.add_right_hold_lineEdit.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.add_right_hold_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.status_running_or_idle_label.setText(QCoreApplication.translate("MainWindow", u"Status: Idle", None))
        self.start_stop_bt.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.remove_key_bt.setText("")
        self.move_up_bt.setText("")
        self.move_down_bt.setText("")
        self.clear_key_bt.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

