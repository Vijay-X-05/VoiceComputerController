import pyautogui
import subprocess


class ActionExecutor:

    def __init__(self):
        # Small delay between PyAutoGUI operations
        pyautogui.PAUSE = 0.3

        # Safety feature:
        # moving the mouse to the top-left corner
        # can trigger PyAutoGUI's fail-safe.
        pyautogui.FAILSAFE = True


    # ---------------------------
    # KEYBOARD
    # ---------------------------

    def type_text(self, text):
        print(f"Typing: {text}")
        pyautogui.write(text, interval=0.03)


    def press_key(self, key):
        print(f"Pressing key: {key}")
        pyautogui.press(key)


    def hotkey(self, *keys):
        print(f"Hotkey: {' + '.join(keys)}")
        pyautogui.hotkey(*keys)


    # ---------------------------
    # MOUSE
    # ---------------------------

    def move_mouse(self, x, y):
        print(f"Moving mouse to: {x}, {y}")
        pyautogui.moveTo(x, y, duration=0.5)


    def click(self):
        print("Clicking...")
        pyautogui.click()


    def double_click(self):
        print("Double clicking...")
        pyautogui.doubleClick()


    def right_click(self):
        print("Right clicking...")
        pyautogui.rightClick()


    def scroll(self, amount):
        print(f"Scrolling: {amount}")
        pyautogui.scroll(amount)


    # ---------------------------
    # APPLICATIONS
    # ---------------------------

    def open_application(self, application):
        print(f"Opening: {application}")

        subprocess.Popen(application)