import customtkinter as ctk
import threading
import time
from PIL import Image 


ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")

class MicroBreakApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Micro-Break Professional v3.5")
        self.geometry("900x650")
        self.configure(fg_color="#f8fafc")

       
        self.is_active = ctk.BooleanVar(value=True)
        self.frequency = ctk.IntVar(value=45)
        self.focus_session = ctk.StringVar(value="Intensive")
        self.notif_mode = ctk.StringVar(value="Gentle")
        
        self.current_area = "Neck" 
        self.exercise_data = {
            "Wrist": {
                "title": "Wrist Rotations",
                "info": "Slowly rotate your wrists in circles.",
                "image_path": "C:/Users/Princ/Desktop/innovation/WRIST.png", 
                "color": "#10b981"
            },
            "Neck": {
                "title": "Neck Release",
                "info": "Gently tilt your head to the right and hold...",
                "image_path": "C:/Users/Princ/Desktop/innovation/NECK.png",
                "color": "#3b82f6"
            },
            "Arms": {
                "title": "Overhead Reach",
                "info": "Interlace fingers and reach for the ceiling.",
                "image_path": "C:/Users/Princ/Desktop/innovation/ARM.png",
                "color": "#f59e0b"
            }
        }
        
        self.time_left = 120 
        self.timer_running = False

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.show_control_hub()

    def clear_screen(self):
        self.timer_running = False
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_control_hub(self):
        self.clear_screen()
        self.attributes("-topmost", False)

        header = ctk.CTkFrame(self.container, height=70, corner_radius=0, fg_color="#ffffff", border_width=1, border_color="#e2e8f0")
        header.pack(side="top", fill="x")
        ctk.CTkLabel(header, text="Micro Break - Configurations", font=("Inter", 20, "bold"), text_color="#1e293b").pack(pady=20, padx=30, anchor="w")

        grid = ctk.CTkFrame(self.container, fg_color="transparent")
        grid.pack(expand=True, fill="both", padx=40, pady=20)
        grid.columnconfigure((0, 1), weight=1)

        left_col = ctk.CTkFrame(grid, fg_color="#ffffff", corner_radius=12, border_width=1, border_color="#e2e8f0")
        left_col.grid(row=0, column=0, padx=15, sticky="nsew")
        ctk.CTkLabel(left_col, text="NOTIFICATION FUNCTIONS", font=("Inter", 11, "bold"), text_color="#3b82f6").pack(pady=(20, 10), padx=25, anchor="w")
        
        status_frame = ctk.CTkFrame(left_col, fg_color="transparent")
        status_frame.pack(padx=25, anchor="w", pady=5)
        self.status_cb = ctk.CTkCheckBox(status_frame, text="Active Status", width=20)
        self.status_cb.select()
        self.status_cb.pack(side="left")

        ctk.CTkLabel(left_col, text="Focus Sessions", font=("Inter", 12, "bold")).pack(padx=25, anchor="w", pady=(20, 5))
        for mode in ["Intensive", "None", "Light"]:
            ctk.CTkRadioButton(left_col, text=mode, variable=self.focus_session, value=mode).pack(padx=25, anchor="w", pady=5)

        right_col = ctk.CTkFrame(grid, fg_color="#ffffff", corner_radius=12, border_width=1, border_color="#e2e8f0")
        right_col.grid(row=0, column=1, padx=15, sticky="nsew")
        ctk.CTkLabel(right_col, text="ACTIVITY REMINDERS", font=("Inter", 11, "bold"), text_color="#3b82f6").pack(pady=(20, 10), padx=25, anchor="w")
        
        self.slider_val_label = ctk.CTkLabel(right_col, text=f"Interval: {self.frequency.get()} min", font=("Inter", 12, "bold"))
        self.slider_val_label.pack(padx=25, anchor="w")
        ctk.CTkSlider(right_col, from_=1, to=60, variable=self.frequency, 
                      command=lambda v: self.slider_val_label.configure(text=f"Interval: {int(v)} min")).pack(fill="x", padx=25, pady=10)

        ctk.CTkButton(self.container, text="Save Changes", command=self.arm_timer, 
                      fg_color="#22c55e", hover_color="#16a34a", height=45, width=200, font=("Inter", 14, "bold")).pack(pady=30)

    def trigger_notification(self):
        self.clear_screen()
        self.attributes("-topmost", True)
        self.geometry("480x320")

        card = ctk.CTkFrame(self.container, fg_color="white", corner_radius=15, border_width=1, border_color="#e2e8f0")
        card.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(card, text="Time to step away?", font=("Inter", 18, "bold")).pack(pady=(20, 10))
        ctk.CTkLabel(card, text="A quick stretch will boost your debugging speed!", font=("Inter", 12), text_color="#64748b").pack()

        ctk.CTkButton(card, text="Start Stretching", command=self.show_guided_activity, fg_color="#3b82f6", width=200, height=45).pack(pady=20)
        ctk.CTkButton(card, text="Snooze (5m)", fg_color="white", text_color="#64748b", border_width=1, border_color="#e2e8f0", width=200, command=self.show_control_hub).pack()

    def show_guided_activity(self):
        self.clear_screen()
        self.geometry("900x650")
        self.timer_running = True

        top = ctk.CTkFrame(self.container, height=60, fg_color="#ffffff", corner_radius=0, border_width=1, border_color="#e2e8f0")
        top.pack(side="top", fill="x")
        ctk.CTkLabel(top, text="Micro-Break: Guided Recovery", font=("Inter", 16, "bold")).pack(pady=15, padx=20, anchor="w")

        self.body_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        self.body_frame.pack(fill="both", expand=True)

        self.side_nav = ctk.CTkFrame(self.body_frame, width=200, fg_color="white", corner_radius=0, border_width=1, border_color="#e2e8f0")
        self.side_nav.pack(side="left", fill="y")
        self.side_nav.pack_propagate(False)

        ctk.CTkLabel(self.side_nav, text="FOCUS AREA", font=("Inter", 10, "bold"), text_color="#3b82f6").pack(pady=(20, 10), padx=25, anchor="w")
        
        self.nav_buttons = {}
        for area in ["Wrist", "Neck", "Arms"]:
            btn = ctk.CTkButton(self.side_nav, text=area, height=45, corner_radius=8, 
                                command=lambda a=area: self.switch_exercise(a))
            btn.pack(pady=5, padx=15, fill="x")
            self.nav_buttons[area] = btn

        self.main_content = ctk.CTkFrame(self.body_frame, fg_color="transparent")
        self.main_content.pack(side="right", fill="both", expand=True)

        ctk.CTkButton(self.container, text="Finish Early", fg_color="#ef4444", hover_color="#dc2626", 
                      corner_radius=8, command=self.show_control_hub).pack(side="bottom", pady=20)

        self.switch_exercise(self.current_area)
        self.run_timer_loop()

    def switch_exercise(self, area):
        self.current_area = area
        data = self.exercise_data[area]

        for name, btn in self.nav_buttons.items():
            if name == area:
                btn.configure(fg_color="#3b82f6", text_color="white")
            else:
                btn.configure(fg_color="#f1f5f9", text_color="#1e293b")

        for widget in self.main_content.winfo_children():
            widget.destroy()

        illus_frame = ctk.CTkFrame(self.main_content, width=500, height=300, corner_radius=20, 
                                fg_color="#ffffff", border_width=1, border_color="#e2e8f0")
        illus_frame.pack(pady=(40, 10))
        illus_frame.pack_propagate(False)

        try:
            pill_img = Image.open(data["image_path"])
            
            ctk_img = ctk.CTkImage(light_image=pill_img, dark_image=pill_img, size=(350, 250))
            
            img_label = ctk.CTkLabel(illus_frame, image=ctk_img, text="")
            img_label.place(relx=0.5, rely=0.5, anchor="center")
            
        except Exception as e:
            ctk.CTkLabel(illus_frame, text=f"Image for {area} not found", 
                        font=("Inter", 14), text_color="#94a3b8").place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(self.main_content, text=data["title"], font=("Inter", 24, "bold")).pack(pady=(10, 0))
        ctk.CTkLabel(self.main_content, text=data["info"], font=("Inter", 14, "italic"), text_color="#475569").pack()

        mins, secs = divmod(self.time_left, 60)
        self.timer_label = ctk.CTkLabel(self.main_content, text=f"{mins:02d}:{secs:02d}", 
                                        font=("Inter", 64, "bold"), text_color=data["color"])
        self.timer_label.pack(pady=20)

   
    def run_timer_loop(self):
        if self.timer_running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            if hasattr(self, 'timer_label'):
                self.timer_label.configure(text=f"{mins:02d}:{secs:02d}")
            self.time_left -= 1
            self.after(1000, self.run_timer_loop)

    def arm_timer(self):
        wait_time = self.frequency.get()
        self.withdraw()
        threading.Thread(target=self.wait_and_trigger, args=(wait_time,), daemon=True).start()

    def wait_and_trigger(self, mins):
        time.sleep(3) 
        self.after(0, self.deiconify)
        self.after(0, self.trigger_notification)

if __name__ == "__main__":
    app = MicroBreakApp()
    app.mainloop()