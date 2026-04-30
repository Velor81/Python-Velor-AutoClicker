# ---------------------------------------------------------
# Developer: Alaa Hamdy (Velor)
# Github: https://github.com/Velor81/Python-Velor-AutoClicker
# Licensed under the MIT License
# ---------------------------------------------------------

from PySide6.QtWidgets import QMainWindow, QApplication, QMenu, QListWidget
from PySide6.QtCore import  Qt, QPoint
from PySide6.QtGui import QAction,QDoubleValidator
from ui_mainwindow import Ui_MainWindow
from AutoClicker import AutoClicker

class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Velor Auto Clicker")
        float_validator = QDoubleValidator()
        float_validator.setNotation(QDoubleValidator.StandardNotation) 
        self.ui.delay_edit.setValidator(float_validator)
        self.ui.add_delay_item_edit.setValidator(float_validator)
        self.ui.add_left_hold_lineEdit.setValidator(float_validator)
        self.ui.add_right_hold_lineEdit.setValidator(float_validator)

        self.auto_clicker = AutoClicker(self.ui.keys_listWidget, self.ui.add_key_edit, self.ui.add_delay_item_edit,
                                        self.ui.toggle_start_stop_edit,self.ui.delay_edit, self.ui.add_left_hold_lineEdit,
                                        self.ui.add_right_hold_lineEdit, self) #self here only for QMessage
        self.add_context_menu(self.ui.keys_listWidget, ['copy', 'clear', 'remove'])

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
        self.ui.delay_edit.textChanged.connect(lambda: self.auto_clicker.save_click_delay())
        self.ui.help_bt.clicked.connect(lambda: self.auto_clicker.show_help())
        self.ui.keys_listWidget.itemChanged.connect(lambda: self.auto_clicker.save_keys_to_file())
        
    def add_context_menu(self, listwidget: QListWidget, options: list):
        def show_context_menu(pos: QPoint):
            context_menu = QMenu(listwidget)
            # Dynamically add actions based on provided options
            if 'copy' in options:
                copy_action = QAction('Copy', listwidget)
                copy_action.triggered.connect(lambda: copy_selected_items(listwidget))
                context_menu.addAction(copy_action)
            if 'select_all' in options:
                select_all_action = QAction('Select All', listwidget)
                select_all_action.triggered.connect(lambda: listwidget.selectAll())
                context_menu.addAction(select_all_action)
            if 'remove' in options:
                remove_action = QAction('Remove', listwidget)
                remove_action.triggered.connect(lambda: remove_selected_items(listwidget))
                context_menu.addAction(remove_action)
            if 'clear' in options:
                clear_selection_action = QAction('Clear Selection', listwidget)
                clear_selection_action.triggered.connect(lambda: listwidget.clearSelection())
                context_menu.addAction(clear_selection_action)
            # Display the context menu at the cursor position
            context_menu.exec(listwidget.mapToGlobal(pos))
        def copy_selected_items(listwidget: QListWidget):
            selected_items = listwidget.selectedItems()
            if selected_items:
                item_texts = [item.text() for item in selected_items]
                all_text = "\n".join(item_texts)
                clipboard = QApplication.clipboard()
                clipboard.setText(all_text)
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
