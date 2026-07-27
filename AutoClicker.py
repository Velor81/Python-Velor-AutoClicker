from PySide6.QtWidgets import QMessageBox, QListWidgetItem
from PySide6.QtGui import QIcon
import time
import os
import threading
import pyautogui
from pynput import keyboard
import json
from ui.ui_mainwindow import Ui_MainWindow

class AutoClicker():
    def __init__(self, parent, ui:Ui_MainWindow):
        self.ui = ui
        self.parent = parent # for Qmessage
        pyautogui.PAUSE = 0.0 #delay between key presses (default is 0.1, 0=no delay)
        self.click_delay = 0.5
        self.hold_start_time = None  
        self.default_stop_start_toggle_key = 'f8'
        self.toggle_start_stop_key = self.get_key_from_text(self.default_stop_start_toggle_key)  # Handle printable and non-printable keys
        self.autoclicker_is_running = False #to break thread
        self.valid_keys = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u','v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'space', 'cmd', 'enter', 'tab', 'shift', 'ctrl', 'alt', 'esc', 'backspace', 'delete', 
            'home', 'end', 'left', 'right', 'up', 'down', 'enter', 'esc', 'pageup', 'pagedown', 'altgr', 
            'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'
        ]

        self.load_keys_from_file() # Load keys from file if available
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()
    def get_key_from_text(self, key_text):
        # Dictionary to map string representations to keyboard keys
        key_map = {
            'shift': keyboard.Key.shift,
            'ctrl': keyboard.Key.ctrl,
            'alt': keyboard.Key.alt,
            'altgr': keyboard.Key.alt_gr,
            'cmd': keyboard.Key.cmd,
            'enter': keyboard.Key.enter,
            'esc': keyboard.Key.esc,
            'tab': keyboard.Key.tab,
            'space': keyboard.Key.space,
            'backspace': keyboard.Key.backspace,
            'delete': keyboard.Key.delete,
            'up': keyboard.Key.up,
            'down': keyboard.Key.down,
            'left': keyboard.Key.left,
            'right': keyboard.Key.right,
            'pageup': keyboard.Key.page_up,
            'pagedown': keyboard.Key.page_down,
            'home': keyboard.Key.home,
            'end': keyboard.Key.end,
            'f1': keyboard.Key.f1,
            'f2': keyboard.Key.f2,
            'f3': keyboard.Key.f3,
            'f4': keyboard.Key.f4,
            'f5': keyboard.Key.f5,
            'f6': keyboard.Key.f6,
            'f7': keyboard.Key.f7,
            'f8': keyboard.Key.f8,
            'f9': keyboard.Key.f9,
            'f10': keyboard.Key.f10,
            'f11': keyboard.Key.f11,
            'f12': keyboard.Key.f12,
        }
        return key_map.get(key_text.lower(), key_text.lower())  # Return key object or lowercase char for printable keys
    def add_mouse_left_right_click_item(self, is_it_left_click:bool):
        if is_it_left_click:
            action = "Left-click"
        else:
            action = "Right-click"
        icon = QIcon("icons/mouse.png")
        self.add_list_item(icon, action)
        self.ui.add_key_edit.clear()  
        self.save_keys_to_file()  

    def add_mouse_left_right_hold_item(self, is_it_left_click:bool):
        if is_it_left_click:
            delay = self.ui.add_left_hold_lineEdit.text()
            action = f"Left-hold: {delay}"
        else:
            delay = self.ui.add_left_hold_lineEdit.text()
            action = f"Right-hold: {delay}"
        icon = QIcon("icons/mouse.png")
        self.add_list_item(icon, action)
        self.ui.add_key_edit.clear()
        self.save_keys_to_file()  
                
    def add_delay_item(self):
        delay_amount = self.ui.add_delay_item_edit.text().strip().lower()
        if delay_amount:
            action = f"delay: {delay_amount}"
            icon = QIcon("icons/delay.png")
            self.add_list_item(icon, action)
            self.ui.add_key_edit.clear() 
            self.save_keys_to_file() 

    def add_key(self):
        key = self.ui.add_key_edit.text().strip().lower()
        if key in self.valid_keys:
            action = f"Key press: {key}"
            icon = QIcon("icons/key.png")
            self.add_list_item(icon, action)
            self.ui.add_key_edit.clear() 
            self.save_keys_to_file() 
            
    def clear_keys(self):
        self.ui.keys_listWidget.clear()
        self.save_keys_to_file()

    def remove_key(self):
        selected_item = self.ui.keys_listWidget.currentItem()
        if selected_item:
            self.ui.keys_listWidget.takeItem(self.ui.keys_listWidget.row(selected_item))
            self.save_keys_to_file()

    def move_key_up(self):
        current_row = self.ui.keys_listWidget.currentRow()
        if current_row > 0:
            item = self.ui.keys_listWidget.takeItem(current_row)
            self.ui.keys_listWidget.insertItem(current_row - 1, item)
            self.ui.keys_listWidget.setCurrentRow(current_row - 1)
            self.save_keys_to_file() 

    def move_key_down(self):
        current_row = self.ui.keys_listWidget.currentRow()
        if current_row < self.ui.keys_listWidget.count() - 1:
            item = self.ui.keys_listWidget.takeItem(current_row)
            self.ui.keys_listWidget.insertItem(current_row + 1, item)
            self.ui.keys_listWidget.setCurrentRow(current_row + 1)
            self.save_keys_to_file()  # Save the updated list to file

    def save_toggle_keys(self):
        start_stop_new_key = self.ui.toggle_start_stop_edit.text().strip()
        if start_stop_new_key:
            self.toggle_start_stop_key = self.get_key_from_text(start_stop_new_key)
        else:
            self.toggle_start_stop_key = self.get_key_from_text(self.default_stop_start_toggle_key)

    def save_click_delay(self):
        try:
            self.click_delay = float(self.ui.delay_edit.text().strip())
            # self.ui.delay_edit.clear() 
            print(f"Click delay set to: {self.click_delay} seconds")
        except ValueError:
            QMessageBox.information(self.parent, "err", "Invalid delay value entered")
            print("Invalid delay value entered")

    def show_help(self):
        help_text = (
        "Developer: Alaa Hamdy (Velor)\n"
        "Github: https://github.com/Velor81\n"
        "Licensed under the MIT License\n\n"
        "------------------------------\n"
            "Instructions:\n"
            "1. Enter a key in the input box and click 'Add Key' to add it to the list.\n"
            "2. Use 'Remove Key' to delete the selected key from the list.\n"
            "3. Use 'Move Up' and 'Move Down' to rearrange the keys in the list.\n"
            "4. Set a toggle key to start/stop the auto clicker from the keyboard.\n"
            "5. Adjust the delay between clicks using the 'Click Delay' input.\n"
        "-------------------------------\n\n"
        "Warning: Setting delay to 0 may cause system lag or freeze. Use with caution."
        )
        QMessageBox.information(self.parent, "Help", help_text)
    def add_key_help(self):
        help_text = ("""
                    <b>Supported Keys</b><br><br>

                    <b>Letters</b><br>
                    A B C D E F G H I J K L M<br>
                    N O P Q R S T U V W X Y Z<br><br>

                    <b>Numbers</b><br>
                    0 1 2 3 4 5 6 7 8 9<br><br>

                    <b>Modifiers</b><br>
                    Shift, Ctrl, Alt, AltGr, Cmd<br><br>

                    <b>Special Keys</b><br>
                    Space, Enter, Tab, Esc, Backspace, Delete<br>
                    Home, End, PageUp, PageDown<br>
                    Left, Right, Up, Down<br><br>

                    <b>Function Keys</b><br>
                    F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12
                    """
        )
        QMessageBox.information(self.parent, "Keys Help", help_text)

    def toggle_autoclicker(self):
        if self.autoclicker_is_running:
            self.autoclicker_is_running = False
            self.ui.status_running_or_idle_label.setText("Status: Idle")
            print("Automation stopped")
        else:
            self.autoclicker_is_running = True
            click_thread = threading.Thread(target=self.start_autoclicker)
            click_thread.start()
            self.ui.status_running_or_idle_label.setText("Status: Running")
            print("Automation started")
    def start_autoclicker(self):
        while self.autoclicker_is_running:
            for i in range(self.ui.keys_listWidget.count()):
                if not self.autoclicker_is_running:
                    break
                item = self.ui.keys_listWidget.item(i).text()
                item_splited = item.split(':')                
                if item_splited[0] == 'Key press':
                    pyautogui.press(item_splited[1].strip())
                elif item_splited[0] == 'Left-click' or item_splited[0] == 'Right-click':
                    pyautogui.click(button='left' if item_splited[0] == 'Left-click' else 'right')
                elif item_splited[0] == 'Left-hold' or item_splited[0] == 'Right-hold':
                    if item_splited[0] == 'Left-hold':
                        m_hold_delay = self.ui.add_left_hold_lineEdit.text()
                    else:
                        m_hold_delay = self.ui.add_right_hold_lineEdit.text()
                    pyautogui.mouseDown(button='left' if 'Left-hold' in item_splited[0] else 'right')
                    time.sleep(float(m_hold_delay.strip()))
                    pyautogui.mouseUp(button='left' if 'Left-hold' in item_splited[0] else 'right')

                elif item_splited[0] == 'delay':
                    delay_time = float(item_splited[1])
                    time.sleep(delay_time) 

                time.sleep(self.click_delay)

    def save_keys_to_file(self):
        keys = [self.ui.keys_listWidget.item(i).text() for i in range(self.ui.keys_listWidget.count())]
        with open("keys.txt", "w") as f:
            for key in keys:
                f.write(f"{key}\n")
    def load_keys_from_file(self):
        if os.path.exists("keys.txt"):
            with open("keys.txt", "r") as f:
                keys = f.readlines()
                for key in keys:
                    key = key.strip()
                    if key:
                        if 'Left-click' in key or "Right-click" in key or 'Left-hold' in key or 'Right-hold':
                            icon = QIcon("icons/mouse.png")
                        elif 'Key press' in key:
                            icon = QIcon('icons/key.png')
                        elif 'delay' in key:
                            icon = QIcon('icons/delay.png')
                        item = QListWidgetItem(icon, key)
                        # self.ui.keys_listWidget.addItem(key.strip())
                        self.ui.keys_listWidget.addItem(item)
                        
    def on_key_press(self, key):
        try:
            if hasattr(key, 'char') and key.char == self.toggle_start_stop_key:
                self.toggle_autoclicker()
            # Handle non-printable keys like F8, Shift, Ctrl
            elif key == self.toggle_start_stop_key:
                self.toggle_autoclicker()
        except AttributeError:
            pass


    def add_list_item(self, icon, action_text):
        list_item = QListWidgetItem(icon, action_text)
        self.ui.keys_listWidget.addItem(list_item)
