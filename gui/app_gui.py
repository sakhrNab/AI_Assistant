import tkinter as tk
from tkinter import scrolledtext
import threading
import datetime
from PIL import Image, ImageTk

class AppGUI:
    def __init__(self, screen_observer):
        self.screen_observer = screen_observer
        self.root = tk.Tk()
        self.root.title("AI Assistant")

        # Create Start and Stop buttons
        self.start_button = tk.Button(self.root, text="Start Observing", command=self.start_observing)
        self.start_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop Observing", command=self.stop_observing)
        self.stop_button.pack()

        # Text area to display detected text
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both')

        # Label to display images
        self.image_label = tk.Label(self.root)
        self.image_label.pack()
        
    def start_observing(self):
        # Start screen observation in a separate thread
        self.observer_thread = threading.Thread(target=self.screen_observer.run)
        self.observer_thread.start()

    def stop_observing(self):
       # Stop the screen observation
        self.screen_observer.stop()
        self.observer_thread.join()

    def update_text_area(self, text):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_text = f"[{timestamp}] {text}\n" + '-'*40 + '\n'
        self.text_area.insert(tk.END, formatted_text)
        self.text_area.yview(tk.END)
    
    def update_image(self, image):
        # Convert the image to a format Tkinter can use and update the label
        tk_image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=tk_image)
        self.image_label.image = tk_image  # Keep a reference to avoid garbage collection

    def run(self):
        self.root.mainloop()
