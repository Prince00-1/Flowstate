import tkinter as tk
from tkinter import messagebox
import time

# Constants from your Mid-Fed design
APP_NAME = "Micro-Break"
PRIMARY_COLOR = "#3b82f6"  # The blue from our CSS
BG_COLOR = "#ffffff"

class MicroBreakApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("350x250")
        self.root.configure(bg=BG_COLOR)
        
        # Make the window stay on top of other apps (like VS Code)
        self.root.attributes("-topmost", True)

        # Header (Matches your 'Micro-Break' heading)
        self.header = tk.Label(root, text="🔔 Time for a Break!", 
                              font=("Arial", 14, "bold"), bg=BG_COLOR, fg="#1e293b")
        self.header.pack(pady=20)

        # Content (Matches your 'Hey! Time for a Break!' text)
        self.label = tk.Label(root, text="You've been in deep focus.\nTake 2 minutes to stretch!", 
                             font=("Arial", 10), bg=BG_COLOR, fg="#64748b")
        self.label.pack(pady=10)

        # Buttons (Matches your 'Start Stretching' and 'Snooze' buttons)
        self.start_btn = tk.Button(root, text="Start Stretching", command=self.start_stretch,
                                  bg=PRIMARY_COLOR, fg="white", font=("Arial", 10, "bold"),
                                  width=20, height=2, bd=0)
        self.start_btn.pack(pady=5)

        self.snooze_btn = tk.Button(root, text="Snooze (5 min)", command=self.snooze,
                                   bg="#f1f5f9", fg="#64748b", font=("Arial", 10),
                                   width=20, bd=1, relief="flat")
        self.snooze_btn.pack(pady=5)

    def start_stretch(self):
        print("User started stretching activity.")
        messagebox.showinfo("Guided Activity", "Opening the Stretching Guide...")
        self.root.destroy()

    def snooze(self):
        print("User requested a 5-minute snooze.") # Matches 'Snooze (5 min)' requirement
        self.root.destroy()

def trigger_ui():
    root = tk.Tk()
    app = MicroBreakApp(root)
    root.mainloop()

if __name__ == "__main__":
    print(f"🚀 {APP_NAME} Engine Active...")
    # For testing, we trigger it immediately. 
    # In production, this would follow your 45-min slider logic.
    trigger_ui()