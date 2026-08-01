# ---------------------------------------------------------
# Developer: Alaa Hamdy (Velor)
# Github: https://github.com/Velor81
# Licensed under the MIT License
# ---------------------------------------------------------

from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QListWidget
from PySide6.QtCore import  Qt, QPoint
from PySide6.QtGui import QAction,QDoubleValidator
from ui.ui_mainwindow import Ui_MainWindow
from AutoClicker import AutoClicker
from PySide6.QtGui import QIcon
import sys
class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Velor Auto Clicker")
        self.setWindowIcon(QIcon("icons/V app icon.ico"))
        float_validator = QDoubleValidator()
        float_validator.setNotation(QDoubleValidator.StandardNotation) 
        self.ui.global_delay_edit.setValidator(float_validator)
        self.ui.add_delay_item_edit.setValidator(float_validator)
        self.ui.add_left_hold_duration_le.setValidator(float_validator)
        self.ui.add_right_hold_duration_le.setValidator(float_validator)
        self.ui.add_key_hold_duration_le.setValidator(float_validator)
        self.add_bt_icons()
        self.auto_clicker = AutoClicker( self, self.ui)

        self.add_context_menu(self.ui.keys_listWidget, ['remove'])

        self.ui.add_key_bt.clicked.connect(lambda: self.auto_clicker.add_key())
        self.ui.add_key_edit.returnPressed.connect(lambda: self.auto_clicker.add_key())
        self.ui.add_delay_item_bt.clicked.connect(lambda: self.auto_clicker.add_delay_item())
        self.ui.add_delay_item_edit.returnPressed.connect(lambda: self.auto_clicker.add_delay_item())
        self.ui.add_mouse_left_click_bt.clicked.connect(lambda: self.auto_clicker.add_mouse_left_right_click_item(True))
        self.ui.add_mouse_right_click_bt.clicked.connect(lambda: self.auto_clicker.add_mouse_left_right_click_item(False))
        self.ui.add_left_hold_bt.clicked.connect(lambda: self.auto_clicker.add_mouse_left_right_hold_item(True))
        self.ui.add_right_hold_bt.clicked.connect(lambda: self.auto_clicker.add_mouse_left_right_hold_item(False))
        self.ui.start_stop_bt.clicked.connect(lambda: self.auto_clicker.toggle_autoclicker())
        self.ui.save_toggle_keys_bt.clicked.connect(lambda: self.auto_clicker.save_toggle_keys())
        self.ui.move_up_bt.clicked.connect(lambda: self.auto_clicker.move_key_up())
        self.ui.move_down_bt.clicked.connect(lambda: self.auto_clicker.move_key_down())
        self.ui.remove_key_bt.clicked.connect(lambda: self.auto_clicker.remove_key())
        self.ui.global_delay_edit.textChanged.connect(lambda: self.auto_clicker.save_click_delay())
        self.ui.help_bt.clicked.connect(lambda: self.auto_clicker.show_help())
        self.ui.keys_listWidget.itemChanged.connect(lambda: self.auto_clicker.save_keys_to_file())
        self.ui.add_key_help_bt.clicked.connect(lambda:self.auto_clicker.add_key_help())
        self.ui.clear_key_bt.clicked.connect(lambda: self.auto_clicker.clear_keys())
        self.ui.add_key_hold_bt.clicked.connect(lambda: self.auto_clicker.add_key_hold())
        self.ui.add_key_hold_help.clicked.connect(lambda:self.auto_clicker.add_key_hold_help())

    def add_bt_icons(self):
        icon = QIcon("icons/arrow-up-icon Blue.png")
        self.ui.move_up_bt.setIcon(icon)
        icon = QIcon("icons/arrow-down-icon Blue.png")
        self.ui.move_down_bt.setIcon(icon)
        icon = QIcon("icons/play-icon Red.png")
        self.ui.start_stop_bt.setIcon(icon)
        icon = QIcon("icons/x-icon red.png")
        self.ui.remove_key_bt.setIcon(icon)
    
    def add_context_menu(self, listwidget: QListWidget, options: list):
        def show_context_menu(pos: QPoint):
            context_menu = QMenu(listwidget)
            # Dynamically add actions based on provided options
            if 'remove' in options:
                remove_action = QAction('Remove', listwidget)
                remove_action.triggered.connect(lambda: remove_selected_items(listwidget))
                context_menu.addAction(remove_action)
            context_menu.exec(listwidget.mapToGlobal(pos))
            
        def remove_selected_items(listwidget: QListWidget):
            selected_items = listwidget.selectedItems()
            self.auto_clicker.remove_key() ##
            if selected_items:
                for item in selected_items:
                    row = listwidget.row(item)
                    listwidget.takeItem(row)
        listwidget.setContextMenuPolicy(Qt.CustomContextMenu)
        listwidget.customContextMenuRequested.connect(show_context_menu)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(550,  500)
    window.show()
    sys.exit(app.exec())
