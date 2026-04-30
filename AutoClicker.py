from PySide6.QtWidgets import QMessageBox, QListWidgetItem
from PySide6.QtGui import QIcon
import time
import os
import threading
import pyautogui
from pynput import keyboard
import sys

class AutoClicker():
    def __init__(self, list_widget, line_add_edit, add_delay_edit, toggle_start_stop_edit, delay_edit, 
                 left_hold_lineEdit,  right_hold_lineEdit, main_self):
        self.toggle_start_stop_edit = toggle_start_stop_edit
        self.list_widget = list_widget
        self.line_add_edit = line_add_edit
        self.add_delay_edit = add_delay_edit
        self.delay_edit = delay_edit
        self.add_left_hold_lineEdit = left_hold_lineEdit
        self.add_right_hold_lineEdit = right_hold_lineEdit
        self.main_self = main_self # for Qmessage
        pyautogui.PAUSE = 0.0 #delay between key presses (default is 0.1, 0=no delay)
        self.click_delay = 0.5
        self.hold_start_time = None  
        self.click_threshold = 0.2 
        self.hold_x, self.hold_y = 0, 0  
        self.default_stop_start_toggle_key = 'f8'
        self.toggle_start_stop_key = self.get_key_from_text(self.default_stop_start_toggle_key)  # Handle printable and non-printable keys

        self.autoclicker_is_running = False #to break thread
        self.valid_keys = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'space', 'enter', 'tab', 'shift', 'ctrl', 'alt', 'esc', 'backspace', 'delete', 'home', 'end', 
            'left', 'right', 'up', 'down', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'
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
            # Add more special keys as needed
        }
        return key_map.get(key_text.lower(), key_text.lower())  # Return key object or lowercase char for printable keys
    def add_mouse_left_right_click_item(self, is_it_left_click:bool):
        if is_it_left_click:
            action = "Left-click"
        else:
            action = "right-click"
        icon = QIcon(self.resource_path("icons/mouse.png"))
        self.add_list_item(icon, action)
        self.line_add_edit.clear()  
        self.save_keys_to_file()  

    def add_mouse_left_right_hold_item(self, is_it_left_click:bool):
        if is_it_left_click:
            delay = self.add_left_hold_lineEdit.text()
            action = f"Left-hold: {delay}"
        else:
            delay = self.add_left_hold_lineEdit.text()
            action = f"right-hold: {delay}"
        icon = QIcon(self.resource_path("icons/mouse.png"))
        self.add_list_item(icon, action)
        self.line_add_edit.clear()
        self.save_keys_to_file()  
                
    def add_delay_item(self):
        delay_amount = self.add_delay_edit.text().strip().lower()
        if delay_amount:
            action = f"delay: {delay_amount}"
            icon = QIcon(self.resource_path("icons/delay.png"))
            self.add_list_item(icon, action)
            self.line_add_edit.clear() 
            self.save_keys_to_file() 

    def add_key(self):
        key = self.line_add_edit.text().strip().lower()
        if key in self.valid_keys:
            action = f"Key press: {key}"
            icon = QIcon(self.resource_path("icons/key.png"))
            self.add_list_item(icon, action)
            self.line_add_edit.clear() 
            self.save_keys_to_file() 
    def remove_key(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))
            self.save_keys_to_file()

    def move_key_up(self):
        current_row = self.list_widget.currentRow()
        if current_row > 0:
            item = self.list_widget.takeItem(current_row)
            self.list_widget.insertItem(current_row - 1, item)
            self.list_widget.setCurrentRow(current_row - 1)
            self.save_keys_to_file() 

    def move_key_down(self):
        current_row = self.list_widget.currentRow()
        if current_row < self.list_widget.count() - 1:
            item = self.list_widget.takeItem(current_row)
            self.list_widget.insertItem(current_row + 1, item)
            self.list_widget.setCurrentRow(current_row + 1)
            self.save_keys_to_file()  # Save the updated list to file

    def save_toggle_keys(self):
        start_stop_new_key = self.toggle_start_stop_edit.text().strip()
        if start_stop_new_key:
            self.toggle_start_stop_key = self.get_key_from_text(start_stop_new_key)
        else:
            self.toggle_start_stop_key = self.get_key_from_text(self.default_stop_start_toggle_key)

    def save_click_delay(self):
        try:
            self.click_delay = float(self.delay_edit.text().strip())
            # self.delay_edit.clear() 
            print(f"Click delay set to: {self.click_delay} seconds")
        except ValueError:
            QMessageBox.information(self.main_self, "err", "Invalid delay value entered")
            print("Invalid delay value entered")

    def show_help(self):
        help_text = (
        "Developer: Alaa Hamdy (Velor)\n"
        "Github: https://github.com/Velor81/Python-Velor-AutoClicker\n"
        "Licensed under the MIT License\n"
        "------------------------------\n"
            "Available Keys for Auto Clicker:\n"
            "- Alphabets (e.g., 'a', 'b', 'c')\n"
            "- Special keys like 'enter', 'space', 'tab', 'shift', 'ctrl'\n"
            "- Numeric keys (e.g., '1', '2', '3')\n"
            "- Function keys (e.g., 'f1', 'f2', 'f3')\n"
            "\nInstructions:\n"
            "1. Enter a key in the input box and click 'Add Key' to add it to the list.\n"
            "2. Use 'Remove Key' to delete the selected key from the list.\n"
            "3. Use 'Move Up' and 'Move Down' to rearrange the keys in the list.\n"
            "4. Set a toggle key to start/stop the auto clicker from the keyboard.\n"
            "5. Adjust the delay between clicks using the 'Click Delay' input."
        )
        QMessageBox.information(self.main_self, "Help", help_text)

    def toggle_autoclicker(self):
        if self.autoclicker_is_running:
            self.autoclicker_is_running = False
            print("Automation stopped")
        else:
            self.autoclicker_is_running = True
            click_thread = threading.Thread(target=self.start_autoclicker)
            click_thread.start()
            print("Automation started")
    def start_autoclicker(self):
        while self.autoclicker_is_running:
            for i in range(self.list_widget.count()):
                if not self.autoclicker_is_running:
                    break
                item = self.list_widget.item(i).text()
                item_splited = item.split(':')
                print(item_splited[0])
                
                if item_splited[0] == 'Key press':
                    pyautogui.press(item_splited[1].strip())
                elif item_splited[0] == 'Key combo':
                    keys = item_splited[1].split('+')
                    # Press down multiple keys
                    for key in keys:
                        pyautogui.keyDown(key)
                    time.sleep(0.2)  # Hold for x second
                    # Release multiple keys
                    for key in keys:
                        pyautogui.keyUp(key)
                elif item_splited[0] == 'Left-click' or item_splited[0] == 'Right-click':
                    pyautogui.click(button='left' if item_splited[0] == 'Left-click' else 'right')

                elif item_splited[0] == 'Left-hold' or item_splited[0] == 'Right-hold':
                    if item_splited[0] == 'Left-hold':
                        m_hold_delay = self.add_left_hold_lineEdit.text()
                    else:
                        m_hold_delay = self.add_right_hold_lineEdit.text()
                    pyautogui.mouseDown(button='left' if 'Left-hold' in item_splited[0] else 'right')
                    time.sleep(int(m_hold_delay.strip()))
                    pyautogui.mouseUp(button='left' if 'Left-hold' in item_splited[0] else 'right')

                elif item_splited[0] == 'delay':
                    delay_time = float(item_splited[1])
                    print(f"Sleeping for {delay_time} seconds")
                    time.sleep(delay_time)  # Apply the delay

                time.sleep(self.click_delay)

    # File saving and loading logic
    def save_keys_to_file(self):
        keys = [self.list_widget.item(i).text() for i in range(self.list_widget.count())]
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
                            icon = QIcon(self.resource_path("icons/mouse.png"))
                        elif 'Key press' in key:
                            icon = QIcon(self.resource_path('icons/key.png'))
                        elif 'delay' in key:
                            icon = QIcon(self.resource_path('icons/delay.png'))
                        elif 'Mouse hold at' in key:
                            icon = QIcon(self.resource_path('icons/mouse_hold.png'))
                        elif 'Mouse release at' in key:
                            icon = QIcon(self.resource_path('icons/mouse_release.png'))
                        item = QListWidgetItem(icon, key)
                        # self.list_widget.addItem(key.strip())
                        self.list_widget.addItem(item)
    def resource_path(self, relative_path): #used for (auto-py-to-exe) to get the icons path when convert to one exe
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

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
        self.list_widget.addItem(list_item)
