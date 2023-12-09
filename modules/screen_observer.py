import time
import numpy as np
import cv2
import pytesseract
from PIL import Image
import pyautogui

class ScreenObserver:
    def __init__(self, update_text_callback=None, update_image_callback=None):
        self.active = True
        self.update_text_callback = update_text_callback

        self.update_image_callback = update_image_callback



    def capture_screen(self):
        # Capture the current screen
        screenshot = pyautogui.screenshot()
        return screenshot

    def process_screen_for_color(self, screenshot):
        # Convert PIL Image to an OpenCV format
        open_cv_image = np.array(screenshot)
        open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR

        # Define the range of the target color in BGR
        lower_bound = np.array([110, 50, 50])
        upper_bound = np.array([130, 255, 255])

        # Threshold the image to only get the selected color
        mask = cv2.inRange(open_cv_image, lower_bound, upper_bound)

        # Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            cv2.drawContours(open_cv_image, [contour], -1, (0, 255, 0), 3)

        # Convert back to PIL Image
        processed_image = Image.fromarray(open_cv_image[:, :, ::-1])  # Convert BGR to RGB

        # Save or display the processed image
        processed_image.save("processed_screenshot.png")
        
        processed_image = Image.fromarray(open_cv_image[:, :, ::-1])  # Convert BGR to RGB
        
        if self.update_image_callback:
            self.update_image_callback(processed_image)

    def process_screen_for_text(self, screenshot):
        # Convert screenshot to a format suitable for Tesseract
        text = pytesseract.image_to_string(screenshot)
        if self.update_text_callback:
            self.update_text_callback(text)

        # Process the extracted text (print, analyze, etc.)
        print(text)

    def run(self):
        while self.active:
            screenshot = self.capture_screen()
            
            # Example of processing for color
            self.process_screen_for_color(screenshot)

            # Example of processing for text
            self.process_screen_for_text(screenshot)

            time.sleep(1)  # Add a delay to avoid high CPU usage

    def stop(self):
        self.active = False
