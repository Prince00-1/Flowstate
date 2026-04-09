import tkinter as tk
from tkinter import ttk
import time

class MicroBreakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Micro-Break")
        self.root.geometry("500x400")
        self.root.configure(bg="#ffffff")
        self.root.attributes("-topmost", True)

        # Container to hold different "Pages"
        self.container = tk.Frame(self.root, bg="#ffffff")
        self.container.pack(fill="both", expand=True)

        self.show_notification_page()

    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_notification_page(self):
        """Page 1: The Notification (Matches your 'Hey! Time for a Break!' sketch)"""
        self.clear_frame()
        
        header = tk.Label(self.container, text="🔔 Micro-Break Alert", 
                         font=("Arial", 16, "bold"), bg="#ffffff", fg="#3b82f6")
        header.pack(pady=30)

        msg = tk.Label(self.container, text="You've met your 45-min focus goal.\nReady for a quick stretch?", 
                      font=("Arial", 11), bg="#ffffff", fg="#64748b")
        msg.pack(pady=10)

        # Action Buttons
        tk.Button(self.container, text="Start Stretching", command=self.show_activity_page,
                  bg="#3b82f6", fg="white", font=("Arial", 10, "bold"), width=20, height=2).pack(pady=10)
        
        tk.Button(self.container, text="Snooze (5 min)", command=self.root.destroy,
                  bg="#f1f5f9", fg="#64748b", font=("Arial", 10), width=20).pack(pady=5)

    def show_activity_page(self):
        """Page 2: Guided Activity (Matches your 'Wrist, Neck, Arms' menu)"""
        self.clear_frame()

        # Two-column layout
        sidebar = tk.Frame(self.container, bg="#f8fafc", width=150)
        sidebar.pack(side="left", fill="y")
        
        main_area = tk.Frame(self.container, bg="#ffffff")
        main_area.pack(side="right", fill="both", expand=True)

        # Sidebar Menu [cite: 4, 5, 6]
        tk.Label(sidebar, text="FOCUS AREA", font=("Arial", 8, "bold"), bg="#f8fafc", fg="#3b82f6").pack(pady=10)
        for area in ["Wrist", "Neck", "Arms"]:
            tk.Button(sidebar, text=area, font=("Arial", 9), bg="#ffffff", relief="flat", anchor="w").pack(fill="x", padx=10, pady=2)

        # Illustrasions Area [cite: 13]
        tk.Label(main_area, text="Guided Activity: Neck Release", font=("Arial", 12, "bold"), bg="#ffffff").pack(pady=10)
        
        illustration = tk.Frame(main_area, bg="#f1f5f9", height=150, width=250, highlightbackground="#cbd5e1", highlightthickness=2)
        illustration.pack(pady=10)
        tk.Label(illustration, text="[ Animation Placeholder ]", bg="#f1f5f9", fg="#94a3b8").place(relx=0.5, rely=0.5, anchor="center")

        # Timer Logic
        self.timer_label = tk.Label(main_area, text="02:00", font=("Arial", 24, "bold"), bg="#ffffff", fg="#10b981")
        self.timer_label.pack(pady=10)

        tk.Button(main_area, text="End Early", command=self.show_notification_page, 
                  bg="#ef4444", fg="white", font=("Arial", 9, "bold")).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MicroBreakApp(root)
    root.mainloop()