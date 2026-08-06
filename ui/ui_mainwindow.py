# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(793, 720)
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
        self.about_bt = QPushButton(self.horizontalFrame)
        self.about_bt.setObjectName(u"about_bt")

        self.horizontalLayout_5.addWidget(self.about_bt, 0, Qt.AlignmentFlag.AlignLeft)


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
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalFrame1 = QFrame(self.toggle_keys_group)
        self.horizontalFrame1.setObjectName(u"horizontalFrame1")
        self.horizontalFrame1.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 1)
        self.start_stop_label = QLabel(self.horizontalFrame1)
        self.start_stop_label.setObjectName(u"start_stop_label")

        self.horizontalLayout_8.addWidget(self.start_stop_label)

        self.toggle_start_stop_edit = QLineEdit(self.horizontalFrame1)
        self.toggle_start_stop_edit.setObjectName(u"toggle_start_stop_edit")

        self.horizontalLayout_8.addWidget(self.toggle_start_stop_edit)

        self.save_toggle_keys_bt = QPushButton(self.horizontalFrame1)
        self.save_toggle_keys_bt.setObjectName(u"save_toggle_keys_bt")

        self.horizontalLayout_8.addWidget(self.save_toggle_keys_bt)


        self.verticalLayout_5.addWidget(self.horizontalFrame1)


        self.verticalLayout_4.addWidget(self.toggle_keys_group)

        self.delay_group = QGroupBox(self.verticalFrame_2)
        self.delay_group.setObjectName(u"delay_group")
        self.delay_group.setFlat(False)
        self.horizontalLayout_3 = QHBoxLayout(self.delay_group)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.global_delay_edit = QLineEdit(self.delay_group)
        self.global_delay_edit.setObjectName(u"global_delay_edit")

        self.horizontalLayout_3.addWidget(self.global_delay_edit)


        self.verticalLayout_4.addWidget(self.delay_group)

        self.verticalGroupBox_3 = QGroupBox(self.verticalFrame_2)
        self.verticalGroupBox_3.setObjectName(u"verticalGroupBox_3")
        self.verticalGroupBox_3.setMinimumSize(QSize(220, 0))
        self.verticalGroupBox_3.setMaximumSize(QSize(220, 16777215))
        self.add_key_group = QVBoxLayout(self.verticalGroupBox_3)
        self.add_key_group.setSpacing(4)
        self.add_key_group.setObjectName(u"add_key_group")
        self.add_key_group.setContentsMargins(0, 0, 0, 0)
        self.horizontalGroupBox = QGroupBox(self.verticalGroupBox_3)
        self.horizontalGroupBox.setObjectName(u"horizontalGroupBox")
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.add_delay_item_bt = QPushButton(self.horizontalGroupBox)
        self.add_delay_item_bt.setObjectName(u"add_delay_item_bt")

        self.horizontalLayout_9.addWidget(self.add_delay_item_bt)

        self.add_delay_item_edit = QLineEdit(self.horizontalGroupBox)
        self.add_delay_item_edit.setObjectName(u"add_delay_item_edit")

        self.horizontalLayout_9.addWidget(self.add_delay_item_edit)


        self.add_key_group.addWidget(self.horizontalGroupBox)

        self.line = QFrame(self.verticalGroupBox_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.add_key_group.addWidget(self.line)

        self.verticalGroupBox = QGroupBox(self.verticalGroupBox_3)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.gridLayout = QGridLayout(self.verticalGroupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.add_key_bt = QPushButton(self.verticalGroupBox)
        self.add_key_bt.setObjectName(u"add_key_bt")

        self.gridLayout.addWidget(self.add_key_bt, 1, 0, 1, 2)

        self.add_key_edit = QLineEdit(self.verticalGroupBox)
        self.add_key_edit.setObjectName(u"add_key_edit")
        self.add_key_edit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_key_edit, 0, 0, 1, 1)

        self.add_key_help_bt = QPushButton(self.verticalGroupBox)
        self.add_key_help_bt.setObjectName(u"add_key_help_bt")
        self.add_key_help_bt.setMaximumSize(QSize(25, 25))

        self.gridLayout.addWidget(self.add_key_help_bt, 0, 1, 1, 1)


        self.add_key_group.addWidget(self.verticalGroupBox)

        self.gridGroupBox = QGroupBox(self.verticalGroupBox_3)
        self.gridGroupBox.setObjectName(u"gridGroupBox")
        self.gridLayout_2 = QGridLayout(self.gridGroupBox)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.add_key_hold_help = QPushButton(self.gridGroupBox)
        self.add_key_hold_help.setObjectName(u"add_key_hold_help")
        self.add_key_hold_help.setMaximumSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.add_key_hold_help, 0, 2, 1, 1)

        self.add_key_hold_le = QLineEdit(self.gridGroupBox)
        self.add_key_hold_le.setObjectName(u"add_key_hold_le")

        self.gridLayout_2.addWidget(self.add_key_hold_le, 0, 0, 1, 1)

        self.add_key_hold_duration_le = QLineEdit(self.gridGroupBox)
        self.add_key_hold_duration_le.setObjectName(u"add_key_hold_duration_le")

        self.gridLayout_2.addWidget(self.add_key_hold_duration_le, 0, 1, 1, 1)

        self.add_key_hold_bt = QPushButton(self.gridGroupBox)
        self.add_key_hold_bt.setObjectName(u"add_key_hold_bt")

        self.gridLayout_2.addWidget(self.add_key_hold_bt, 2, 0, 1, 3)


        self.add_key_group.addWidget(self.gridGroupBox)

        self.line_2 = QFrame(self.verticalGroupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.add_key_group.addWidget(self.line_2)

        self.horizontalGroupBox1 = QGroupBox(self.verticalGroupBox_3)
        self.horizontalGroupBox1.setObjectName(u"horizontalGroupBox1")
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalGroupBox1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.add_mouse_left_click_bt = QPushButton(self.horizontalGroupBox1)
        self.add_mouse_left_click_bt.setObjectName(u"add_mouse_left_click_bt")

        self.horizontalLayout_7.addWidget(self.add_mouse_left_click_bt)

        self.add_mouse_right_click_bt = QPushButton(self.horizontalGroupBox1)
        self.add_mouse_right_click_bt.setObjectName(u"add_mouse_right_click_bt")

        self.horizontalLayout_7.addWidget(self.add_mouse_right_click_bt)


        self.add_key_group.addWidget(self.horizontalGroupBox1)

        self.verticalGroupBox1 = QGroupBox(self.verticalGroupBox_3)
        self.verticalGroupBox1.setObjectName(u"verticalGroupBox1")
        self.verticalLayout_10 = QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.horizontalFrame2 = QFrame(self.verticalGroupBox1)
        self.horizontalFrame2.setObjectName(u"horizontalFrame2")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.add_left_hold_bt = QPushButton(self.horizontalFrame2)
        self.add_left_hold_bt.setObjectName(u"add_left_hold_bt")

        self.horizontalLayout_4.addWidget(self.add_left_hold_bt)

        self.add_left_hold_duration_le = QLineEdit(self.horizontalFrame2)
        self.add_left_hold_duration_le.setObjectName(u"add_left_hold_duration_le")

        self.horizontalLayout_4.addWidget(self.add_left_hold_duration_le)


        self.verticalLayout_10.addWidget(self.horizontalFrame2)

        self.horizontalFrame_2 = QFrame(self.verticalGroupBox1)
        self.horizontalFrame_2.setObjectName(u"horizontalFrame_2")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.add_right_hold_bt = QPushButton(self.horizontalFrame_2)
        self.add_right_hold_bt.setObjectName(u"add_right_hold_bt")

        self.horizontalLayout_6.addWidget(self.add_right_hold_bt)

        self.add_right_hold_duration_le = QLineEdit(self.horizontalFrame_2)
        self.add_right_hold_duration_le.setObjectName(u"add_right_hold_duration_le")

        self.horizontalLayout_6.addWidget(self.add_right_hold_duration_le)


        self.verticalLayout_10.addWidget(self.horizontalFrame_2)


        self.add_key_group.addWidget(self.verticalGroupBox1)


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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.move_up_down_group.sizePolicy().hasHeightForWidth())
        self.move_up_down_group.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.move_up_bt.sizePolicy().hasHeightForWidth())
        self.move_up_bt.setSizePolicy(sizePolicy2)
        self.move_up_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.move_up_bt)

        self.move_down_bt = QPushButton(self.move_up_down_group)
        self.move_down_bt.setObjectName(u"move_down_bt")
        sizePolicy2.setHeightForWidth(self.move_down_bt.sizePolicy().hasHeightForWidth())
        self.move_down_bt.setSizePolicy(sizePolicy2)
        self.move_down_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.move_down_bt)

        self.clear_key_bt = QPushButton(self.move_up_down_group)
        self.clear_key_bt.setObjectName(u"clear_key_bt")
        self.clear_key_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.clear_key_bt)


        self.horizontalLayout.addWidget(self.move_up_down_group)


        self.verticalLayout_2.addWidget(self.verticalFrame_6)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.about_bt, self.toggle_start_stop_edit)
        QWidget.setTabOrder(self.toggle_start_stop_edit, self.save_toggle_keys_bt)
        QWidget.setTabOrder(self.save_toggle_keys_bt, self.global_delay_edit)
        QWidget.setTabOrder(self.global_delay_edit, self.add_delay_item_bt)
        QWidget.setTabOrder(self.add_delay_item_bt, self.add_delay_item_edit)
        QWidget.setTabOrder(self.add_delay_item_edit, self.add_key_edit)
        QWidget.setTabOrder(self.add_key_edit, self.add_key_help_bt)
        QWidget.setTabOrder(self.add_key_help_bt, self.add_key_bt)
        QWidget.setTabOrder(self.add_key_bt, self.add_key_hold_le)
        QWidget.setTabOrder(self.add_key_hold_le, self.add_key_hold_duration_le)
        QWidget.setTabOrder(self.add_key_hold_duration_le, self.add_key_hold_help)
        QWidget.setTabOrder(self.add_key_hold_help, self.add_key_hold_bt)
        QWidget.setTabOrder(self.add_key_hold_bt, self.add_mouse_left_click_bt)
        QWidget.setTabOrder(self.add_mouse_left_click_bt, self.add_mouse_right_click_bt)
        QWidget.setTabOrder(self.add_mouse_right_click_bt, self.add_left_hold_bt)
        QWidget.setTabOrder(self.add_left_hold_bt, self.add_left_hold_duration_le)
        QWidget.setTabOrder(self.add_left_hold_duration_le, self.add_right_hold_bt)
        QWidget.setTabOrder(self.add_right_hold_bt, self.add_right_hold_duration_le)
        QWidget.setTabOrder(self.add_right_hold_duration_le, self.start_stop_bt)
        QWidget.setTabOrder(self.start_stop_bt, self.keys_listWidget)
        QWidget.setTabOrder(self.keys_listWidget, self.remove_key_bt)
        QWidget.setTabOrder(self.remove_key_bt, self.move_up_bt)
        QWidget.setTabOrder(self.move_up_bt, self.move_down_bt)
        QWidget.setTabOrder(self.move_down_bt, self.clear_key_bt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.about_bt.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.toggle_keys_group.setTitle(QCoreApplication.translate("MainWindow", u"Toggle Keys", None))
        self.start_stop_label.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.toggle_start_stop_edit.setText(QCoreApplication.translate("MainWindow", u"f8", None))
        self.toggle_start_stop_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"f8", None))
        self.save_toggle_keys_bt.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.delay_group.setTitle(QCoreApplication.translate("MainWindow", u"Global Delay", None))
        self.global_delay_edit.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.global_delay_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.verticalGroupBox_3.setTitle("")
        self.horizontalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Add Delay", None))
        self.add_delay_item_bt.setText(QCoreApplication.translate("MainWindow", u"Add Delay", None))
        self.add_delay_item_edit.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.add_delay_item_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.verticalGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Add Key Click", None))
        self.add_key_bt.setText(QCoreApplication.translate("MainWindow", u"Add Key", None))
        self.add_key_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter key", None))
        self.add_key_help_bt.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.gridGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Add Key Hold", None))
        self.add_key_hold_help.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.add_key_hold_le.setText("")
        self.add_key_hold_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Key Hold", None))
        self.add_key_hold_duration_le.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.add_key_hold_duration_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.add_key_hold_bt.setText(QCoreApplication.translate("MainWindow", u"Add Key Hold", None))
        self.horizontalGroupBox1.setTitle(QCoreApplication.translate("MainWindow", u"Add Mouse Click", None))
        self.add_mouse_left_click_bt.setText(QCoreApplication.translate("MainWindow", u"Left Click", None))
        self.add_mouse_right_click_bt.setText(QCoreApplication.translate("MainWindow", u"Right Click", None))
        self.verticalGroupBox1.setTitle(QCoreApplication.translate("MainWindow", u"Add Mouse Hold", None))
        self.add_left_hold_bt.setText(QCoreApplication.translate("MainWindow", u"Left Hold", None))
        self.add_left_hold_duration_le.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.add_left_hold_duration_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.add_right_hold_bt.setText(QCoreApplication.translate("MainWindow", u"Right Hold", None))
        self.add_right_hold_duration_le.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.add_right_hold_duration_le.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.status_running_or_idle_label.setText(QCoreApplication.translate("MainWindow", u"Status: Idle", None))
        self.start_stop_bt.setText(QCoreApplication.translate("MainWindow", u"Start/Stop", None))
        self.remove_key_bt.setText("")
        self.move_up_bt.setText("")
        self.move_down_bt.setText("")
        self.clear_key_bt.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

