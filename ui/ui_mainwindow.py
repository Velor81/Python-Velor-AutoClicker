# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    
    QFont,
)
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalFrame = QFrame(self.centralwidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.horizontalFrame.sizePolicy().hasHeightForWidth()
        )
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.help_bt = QPushButton(self.horizontalFrame)
        self.help_bt.setObjectName("help_bt")

        self.horizontalLayout_5.addWidget(self.help_bt, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_2.addWidget(self.horizontalFrame)

        self.verticalFrame_6 = QFrame(self.centralwidget)
        self.verticalFrame_6.setObjectName("verticalFrame_6")
        self.horizontalLayout = QHBoxLayout(self.verticalFrame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_2 = QFrame(self.verticalFrame_6)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.verticalFrame_2.sizePolicy().hasHeightForWidth()
        )
        self.verticalFrame_2.setSizePolicy(sizePolicy1)
        self.verticalFrame_2.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.verticalFrame_2)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggle_keys_group = QGroupBox(self.verticalFrame_2)
        self.toggle_keys_group.setObjectName("toggle_keys_group")
        self.toggle_keys_group.setMinimumSize(QSize(220, 0))
        self.toggle_keys_group.setMaximumSize(QSize(220, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.toggle_keys_group)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.horizontalFrame1 = QFrame(self.toggle_keys_group)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 1)
        self.start_stop_label = QLabel(self.horizontalFrame1)
        self.start_stop_label.setObjectName("start_stop_label")

        self.horizontalLayout_8.addWidget(self.start_stop_label)

        self.toggle_start_stop_edit = QLineEdit(self.horizontalFrame1)
        self.toggle_start_stop_edit.setObjectName("toggle_start_stop_edit")

        self.horizontalLayout_8.addWidget(self.toggle_start_stop_edit)

        self.verticalLayout_5.addWidget(self.horizontalFrame1)

        self.save_toggle_keys_bt = QPushButton(self.toggle_keys_group)
        self.save_toggle_keys_bt.setObjectName("save_toggle_keys_bt")

        self.verticalLayout_5.addWidget(self.save_toggle_keys_bt)

        self.verticalLayout_4.addWidget(self.toggle_keys_group)

        self.delay_group = QGroupBox(self.verticalFrame_2)
        self.delay_group.setObjectName("delay_group")
        self.horizontalLayout_3 = QHBoxLayout(self.delay_group)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.global_delay_edit = QLineEdit(self.delay_group)
        self.global_delay_edit.setObjectName("global_delay_edit")

        self.horizontalLayout_3.addWidget(self.global_delay_edit)

        self.verticalLayout_4.addWidget(self.delay_group)

        self.verticalGroupBox_3 = QGroupBox(self.verticalFrame_2)
        self.verticalGroupBox_3.setObjectName("verticalGroupBox_3")
        self.verticalGroupBox_3.setMinimumSize(QSize(220, 0))
        self.verticalGroupBox_3.setMaximumSize(QSize(220, 16777215))
        self.add_key_group = QVBoxLayout(self.verticalGroupBox_3)
        self.add_key_group.setSpacing(4)
        self.add_key_group.setObjectName("add_key_group")
        self.add_key_group.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame_4 = QFrame(self.verticalGroupBox_3)
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.verticalLayout_6 = QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.add_key_group.addWidget(self.verticalFrame_4)

        self.add_delay_item_edit = QLineEdit(self.verticalGroupBox_3)
        self.add_delay_item_edit.setObjectName("add_delay_item_edit")

        self.add_key_group.addWidget(self.add_delay_item_edit)

        self.add_delay_item_bt = QPushButton(self.verticalGroupBox_3)
        self.add_delay_item_bt.setObjectName("add_delay_item_bt")

        self.add_key_group.addWidget(self.add_delay_item_bt)

        self.line = QFrame(self.verticalGroupBox_3)
        self.line.setObjectName("line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.add_key_group.addWidget(self.line)

        self.verticalGroupBox = QGroupBox(self.verticalGroupBox_3)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.gridLayout = QGridLayout(self.verticalGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.add_key_bt = QPushButton(self.verticalGroupBox)
        self.add_key_bt.setObjectName("add_key_bt")

        self.gridLayout.addWidget(self.add_key_bt, 1, 0, 1, 2)

        self.add_key_edit = QLineEdit(self.verticalGroupBox)
        self.add_key_edit.setObjectName("add_key_edit")
        self.add_key_edit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.add_key_edit, 0, 0, 1, 1)

        self.add_key_help_bt = QPushButton(self.verticalGroupBox)
        self.add_key_help_bt.setObjectName("add_key_help_bt")
        self.add_key_help_bt.setMaximumSize(QSize(25, 25))

        self.gridLayout.addWidget(self.add_key_help_bt, 0, 1, 1, 1)

        self.add_key_group.addWidget(self.verticalGroupBox)

        self.verticalFrame_5 = QFrame(self.verticalGroupBox_3)
        self.verticalFrame_5.setObjectName("verticalFrame_5")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.verticalFrame_5.sizePolicy().hasHeightForWidth()
        )
        self.verticalFrame_5.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.verticalFrame_5)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.add_key_group.addWidget(self.verticalFrame_5, 0, Qt.AlignmentFlag.AlignTop)

        self.line_2 = QFrame(self.verticalGroupBox_3)
        self.line_2.setObjectName("line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.add_key_group.addWidget(self.line_2)

        self.horizontalGroupBox = QGroupBox(self.verticalGroupBox_3)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.gridLayout_3 = QGridLayout(self.horizontalGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.add_mouse_right_click_bt = QPushButton(self.horizontalGroupBox)
        self.add_mouse_right_click_bt.setObjectName("add_mouse_right_click_bt")

        self.gridLayout_3.addWidget(self.add_mouse_right_click_bt, 1, 0, 1, 1)

        self.add_mouse_left_click_bt = QPushButton(self.horizontalGroupBox)
        self.add_mouse_left_click_bt.setObjectName("add_mouse_left_click_bt")

        self.gridLayout_3.addWidget(self.add_mouse_left_click_bt, 0, 0, 1, 1)

        self.add_key_group.addWidget(self.horizontalGroupBox)

        self.verticalGroupBox1 = QGroupBox(self.verticalGroupBox_3)
        self.verticalGroupBox1.setObjectName("verticalGroupBox1")
        self.verticalLayout_10 = QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.horizontalFrame_2 = QFrame(self.verticalGroupBox1)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.add_right_hold_bt = QPushButton(self.horizontalFrame_2)
        self.add_right_hold_bt.setObjectName("add_right_hold_bt")

        self.horizontalLayout_6.addWidget(self.add_right_hold_bt)

        self.add_right_hold_lineEdit = QLineEdit(self.horizontalFrame_2)
        self.add_right_hold_lineEdit.setObjectName("add_right_hold_lineEdit")

        self.horizontalLayout_6.addWidget(self.add_right_hold_lineEdit)

        self.verticalLayout_10.addWidget(self.horizontalFrame_2)

        self.horizontalFrame2 = QFrame(self.verticalGroupBox1)
        self.horizontalFrame2.setObjectName("horizontalFrame2")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalFrame2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.add_left_hold_bt = QPushButton(self.horizontalFrame2)
        self.add_left_hold_bt.setObjectName("add_left_hold_bt")

        self.horizontalLayout_4.addWidget(self.add_left_hold_bt)

        self.add_left_hold_lineEdit = QLineEdit(self.horizontalFrame2)
        self.add_left_hold_lineEdit.setObjectName("add_left_hold_lineEdit")

        self.horizontalLayout_4.addWidget(self.add_left_hold_lineEdit)

        self.verticalLayout_10.addWidget(self.horizontalFrame2)

        self.add_key_group.addWidget(self.verticalGroupBox1)

        self.verticalLayout_4.addWidget(self.verticalGroupBox_3)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalFrame = QFrame(self.verticalFrame_2)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.status_running_or_idle_label = QLabel(self.verticalFrame)
        self.status_running_or_idle_label.setObjectName("status_running_or_idle_label")
        font = QFont()
        font.setPointSize(18)
        self.status_running_or_idle_label.setFont(font)
        self.status_running_or_idle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.status_running_or_idle_label)

        self.verticalLayout_4.addWidget(self.verticalFrame)

        self.start_stop_bt = QPushButton(self.verticalFrame_2)
        self.start_stop_bt.setObjectName("start_stop_bt")
        self.start_stop_bt.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.start_stop_bt)

        self.horizontalLayout.addWidget(self.verticalFrame_2)

        self.keys_listWidget = QListWidget(self.verticalFrame_6)
        self.keys_listWidget.setObjectName("keys_listWidget")

        self.horizontalLayout.addWidget(self.keys_listWidget)

        self.move_up_down_group = QFrame(self.verticalFrame_6)
        self.move_up_down_group.setObjectName("move_up_down_group")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(
            self.move_up_down_group.sizePolicy().hasHeightForWidth()
        )
        self.move_up_down_group.setSizePolicy(sizePolicy3)
        self.verticalLayout = QVBoxLayout(self.move_up_down_group)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.remove_key_bt = QPushButton(self.move_up_down_group)
        self.remove_key_bt.setObjectName("remove_key_bt")
        self.remove_key_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.remove_key_bt)

        self.move_up_bt = QPushButton(self.move_up_down_group)
        self.move_up_bt.setObjectName("move_up_bt")
        sizePolicy3.setHeightForWidth(self.move_up_bt.sizePolicy().hasHeightForWidth())
        self.move_up_bt.setSizePolicy(sizePolicy3)
        self.move_up_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.move_up_bt)

        self.move_down_bt = QPushButton(self.move_up_down_group)
        self.move_down_bt.setObjectName("move_down_bt")
        sizePolicy3.setHeightForWidth(
            self.move_down_bt.sizePolicy().hasHeightForWidth()
        )
        self.move_down_bt.setSizePolicy(sizePolicy3)
        self.move_down_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.move_down_bt)

        self.clear_key_bt = QPushButton(self.move_up_down_group)
        self.clear_key_bt.setObjectName("clear_key_bt")
        self.clear_key_bt.setMaximumSize(QSize(25, 16777215))

        self.verticalLayout.addWidget(self.clear_key_bt)

        self.horizontalLayout.addWidget(self.move_up_down_group)

        self.verticalLayout_2.addWidget(self.verticalFrame_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.help_bt.setText(QCoreApplication.translate("MainWindow", "Help", None))
        self.toggle_keys_group.setTitle(
            QCoreApplication.translate("MainWindow", "Toggle Keys", None)
        )
        self.start_stop_label.setText(
            QCoreApplication.translate("MainWindow", "Start/Stop", None)
        )
        self.toggle_start_stop_edit.setText(
            QCoreApplication.translate("MainWindow", "f8", None)
        )
        self.toggle_start_stop_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "f8", None)
        )
        self.save_toggle_keys_bt.setText(
            QCoreApplication.translate("MainWindow", "Save Toggle Keys", None)
        )
        self.delay_group.setTitle(
            QCoreApplication.translate("MainWindow", "Global Delay", None)
        )
        self.global_delay_edit.setText(
            QCoreApplication.translate("MainWindow", "0.5", None)
        )
        self.global_delay_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "0.5", None)
        )
        self.verticalGroupBox_3.setTitle(
            QCoreApplication.translate("MainWindow", "Add Delay", None)
        )
        self.add_delay_item_edit.setText(
            QCoreApplication.translate("MainWindow", "0.5", None)
        )
        self.add_delay_item_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "0.5", None)
        )
        self.add_delay_item_bt.setText(
            QCoreApplication.translate("MainWindow", "Add Delay", None)
        )
        self.verticalGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Add Key Click", None)
        )
        self.add_key_bt.setText(
            QCoreApplication.translate("MainWindow", "Add Key", None)
        )
        self.add_key_edit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Enter key", None)
        )
        self.add_key_help_bt.setText(
            QCoreApplication.translate("MainWindow", "?", None)
        )
        self.horizontalGroupBox.setTitle(
            QCoreApplication.translate("MainWindow", "Add Mouse Click", None)
        )
        self.add_mouse_right_click_bt.setText(
            QCoreApplication.translate("MainWindow", "Right Click", None)
        )
        self.add_mouse_left_click_bt.setText(
            QCoreApplication.translate("MainWindow", "Left Click", None)
        )
        self.verticalGroupBox1.setTitle(
            QCoreApplication.translate("MainWindow", "Add Mouse Hold", None)
        )
        self.add_right_hold_bt.setText(
            QCoreApplication.translate("MainWindow", "Right Hold", None)
        )
        self.add_right_hold_lineEdit.setText(
            QCoreApplication.translate("MainWindow", "1.0", None)
        )
        self.add_right_hold_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "1.0", None)
        )
        self.add_left_hold_bt.setText(
            QCoreApplication.translate("MainWindow", "Left Hold", None)
        )
        self.add_left_hold_lineEdit.setText(
            QCoreApplication.translate("MainWindow", "1.0", None)
        )
        self.add_left_hold_lineEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "0.0", None)
        )
        self.status_running_or_idle_label.setText(
            QCoreApplication.translate("MainWindow", "Status: Idle", None)
        )
        self.start_stop_bt.setText(
            QCoreApplication.translate("MainWindow", "Start/Stop", None)
        )
        self.remove_key_bt.setText("")
        self.move_up_bt.setText("")
        self.move_down_bt.setText("")
        self.clear_key_bt.setText(QCoreApplication.translate("MainWindow", "C", None))

    # retranslateUi
