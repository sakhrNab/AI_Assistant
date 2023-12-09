from modules.screen_observer import ScreenObserver
from gui.app_gui import AppGUI
import pytesseract

import threading
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sakhr.al-absi\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def main():
    # Define a callback function for updating the GUI
    def update_text(text):
        app_gui.update_text_area(text)

    def update_image(image):
        app_gui.update_image(image)

    screen_observer = ScreenObserver(update_text_callback=update_text, update_image_callback=update_image)

    # Create GUI object
    app_gui = AppGUI(screen_observer)

    # Run the GUI
    app_gui.run()    
    # Run the screen observer in a separate thread to prevent blocking the main thread
    # observer_thread = threading.Thread(target=screen_observer.run)
    #observer_thread.start()

    try:
        # Main application loop
        while True:
            # Placeholder for main application logic
            # You can add user interaction or other functionalities here
            pass
    except KeyboardInterrupt:
        # Graceful exit on a keyboard interrupt (Ctrl+C)
        print("Stopping Screen Observer...")
        screen_observer.stop()
        observer_thread.join()
        print("Application stopped.")


if __name__ == "__main__":
    main()
