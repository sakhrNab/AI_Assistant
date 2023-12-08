import tkinter as tk

class MainApplication:
    def __init__(self, master, ai_assistant):
        self.master = master
        self.ai_assistant = ai_assistant

        master.title("AI Assistant")

        # Command Input Area
        self.command_entry = tk.Entry(master)
        self.command_entry.pack()

        # Feedback Display
        self.feedback_text = tk.Text(master, height=10, width=50)
        self.feedback_text.pack()

        # Control Buttons
        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(master, text="Stop", command=self.stop)
        self.stop_button.pack()

    def start(self):
        # Start AI Assistant processes
        self.ai_assistant.start()
        self.feedback_text.insert(tk.END, "AI Assistant started.\n")

    def stop(self):
        # Stop AI Assistant processes
        self.ai_assistant.stop()
        self.feedback_text.insert(tk.END, "AI Assistant stopped.\n")

    def display_message(self, message):
        self.feedback_text.insert(tk.END, message + '\n')

def run_app(ai_assistant):
    root = tk.Tk()
    MainApplication(root, ai_assistant)  # Directly pass the root and ai_assistant without assigning to a variable
    root.mainloop()

