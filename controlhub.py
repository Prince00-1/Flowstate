import tkinter as tk
from tkinter import ttk

class MicroBreakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Micro-Break Configuration")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffffff")
        
        # --- App State (Default values from your sketch) ---
        self.is_active = tk.BooleanVar(value=True)
        self.frequency = tk.IntVar(value=45) # 0-45 min slider 
        self.focus_mode = tk.StringVar(value="Intensive") # Intensive, None, Light 
        self.notif_mode = tk.StringVar(value="Gentle") # Gentle vs Persistence 

        self.container = tk.Frame(self.root, bg="#ffffff")
        self.container.pack(fill="both", expand=True)

        self.show_settings_page()

    def clear_frame(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_settings_page(self):
        """The Control Hub (Matches your two-column configuration sketch) """
        self.clear_frame()

        # Header
        header = tk.Label(self.container, text="Micro Break - Configurations", 
                         font=("Arial", 16, "bold"), bg="#f1f3f5", fg="#1e293b", pady=15)
        header.pack(fill="x")

        main_grid = tk.Frame(self.container, bg="#ffffff")
        main_grid.pack(fill="both", expand=True, padx=20, pady=20)

        # LEFT COLUMN: Notification Functions 
        left_col = tk.Frame(main_grid, bg="#ffffff")
        left_col.grid(row=0, column=0, sticky="nsew", padx=10)
        
        tk.Label(left_col, text="NOTIFICATION FUNCTIONS", font=("Arial", 9, "bold"), fg="#3b82f6", bg="#ffffff").pack(anchor="w", pady=10)
        
        tk.Checkbutton(left_col, text="Active Status (On/Off)", variable=self.is_active, bg="#ffffff").pack(anchor="w")
        
        tk.Label(left_col, text="Focus Sessions:", bg="#ffffff", font=("Arial", 9, "bold")).pack(anchor="w", pady=(15, 5))
        for mode in ["Intensive", "None", "Light"]:
            tk.Radiobutton(left_col, text=mode, value=mode, variable=self.focus_mode, bg="#ffffff").pack(anchor="w")

        # RIGHT COLUMN: Activity Reminders 
        right_col = tk.Frame(main_grid, bg="#ffffff")
        right_col.grid(row=0, column=1, sticky="nsew", padx=10)

        tk.Label(right_col, text="ACTIVITY REMINDERS", font=("Arial", 9, "bold"), fg="#3b82f6", bg="#ffffff").pack(anchor="w", pady=10)

        tk.Label(right_col, text=f"Frequency Slider (0-45 min)", bg="#ffffff").pack(anchor="w")
        tk.Scale(right_col, from_=0, to=45, orient="horizontal", variable=self.frequency, bg="#ffffff", length=200).pack(anchor="w")

        tk.Label(right_col, text="Notification Mode:", bg="#ffffff", font=("Arial", 9, "bold")).pack(anchor="w", pady=(15, 5))
        tk.Radiobutton(right_col, text="Gentle", value="Gentle", variable=self.notif_mode, bg="#ffffff").pack(anchor="w")
        tk.Radiobutton(right_col, text="Persistence", value="Persistence", variable=self.notif_mode, bg="#ffffff").pack(anchor="w")

        # Footer Button 
        tk.Button(self.container, text="Save Changes", command=self.save_and_test, 
                  bg="#28a745", fg="white", font=("Arial", 10, "bold"), width=20, pady=10).pack(pady=20)

    def save_and_test(self):
        print(f"Settings Saved: {self.frequency.get()} mins, Mode: {self.notif_mode.get()}")
        # Here we would trigger the timer logic
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MicroBreakApp(root)
    root.mainloop()