import pygetwindow as gw
import pyautogui
import time

class ScreenObserver:
    def __init__(self):
        self.active = True

    def capture_screen(self):
        # Capture the current screen
        screenshot = pyautogui.screenshot()
        return screenshot

    def process_screen(self, screenshot):
        # Process the screenshot (Placeholder for now)
        pass

    def run(self):
        while self.active:
            screenshot = self.capture_screen()
            self.process_screen(screenshot)
            time.sleep(1)  # Add a delay to avoid high CPU usage

    def stop(self):
        self.active = False
