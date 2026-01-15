import customtkinter as ctk
import pyautogui
import keyboard
import threading
import time
from config_manager import ConfigManager
from automator import Automator

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Valo Instalock")
        self.geometry("400x500")
        self.resizable(False, False)

        self.config_manager = ConfigManager()
        self.automator = Automator()
        
        self.is_running = False
        self.selected_agent_var = ctk.StringVar(value="Select Agent")

        self.create_widgets()
        self.refresh_agent_list()

        # Keyboard hook
        keyboard.add_hotkey('F8', self.on_hotkey_trigger)

    def create_widgets(self):
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_run = self.tabview.add("Run")
        self.tab_config = self.tabview.add("Config")

        # --- RUN TAB ---
        self.label_status = ctk.CTkLabel(self.tab_run, text="STATUS: IDLE", font=("Arial", 20, "bold"), text_color="gray")
        self.label_status.pack(pady=40)

        self.option_agent = ctk.CTkOptionMenu(self.tab_run, variable=self.selected_agent_var)
        self.option_agent.pack(pady=10)

        self.btn_toggle = ctk.CTkButton(self.tab_run, text="Unready (F8 to Trigger)", command=self.toggle_listening, state="disabled") # visual only really
        self.btn_toggle.pack(pady=10)
        
        self.label_info = ctk.CTkLabel(self.tab_run, text="Press F8 to LOCK IN selected agent.\nMake sure you are in the agent select screen.", text_color="gray")
        self.label_info.pack(pady=20, padx=10)

        # --- CONFIG TAB ---
        self.btn_add_agent = ctk.CTkButton(self.tab_config, text="Add New Agent", command=self.add_agent_flow)
        self.btn_add_agent.pack(pady=10)

        self.btn_set_lock = ctk.CTkButton(self.tab_config, text="Set Lock Button Position", command=self.set_lock_flow, fg_color="red")
        self.btn_set_lock.pack(pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(self.tab_config, label_text="Saved Agents")
        self.scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)

    def refresh_agent_list(self):
        # Update OptionMenu
        agents = self.config_manager.get_all_agents()
        if agents:
            self.option_agent.configure(values=agents)
            if self.selected_agent_var.get() not in agents:
                self.selected_agent_var.set(agents[0])
            self.label_status.configure(text="READY (F8)", text_color="green")
            self.is_running = True
        else:
            self.option_agent.configure(values=["No Agents Found"])
            self.selected_agent_var.set("No Agents Found")
            self.label_status.configure(text="SETUP REQUIRED", text_color="red")
            self.is_running = False

        # Update Config List
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        for agent in agents:
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(fill="x", pady=2)
            lbl = ctk.CTkLabel(frame, text=agent)
            lbl.pack(side="left", padx=10)
            btn = ctk.CTkButton(frame, text="X", width=30, fg_color="red", command=lambda a=agent: self.delete_agent(a))
            btn.pack(side="right", padx=10)

    def delete_agent(self, name):
        self.config_manager.remove_agent(name)
        self.refresh_agent_list()

    def add_agent_flow(self):
        dialog = ctk.CTkInputDialog(text="Enter Agent Name:", title="Add Agent")
        name = dialog.get_input()
        if name:
            self.countdown_and_record(lambda x, y: self.config_manager.add_agent(name, x, y), f"Hover over {name}")

    def set_lock_flow(self):
        self.countdown_and_record(self.config_manager.set_lock_btn, "Hover over LOCK button")

    def countdown_and_record(self, callback, msg):
        # We need a non-blocking countdown so the GUI updates
        top = ctk.CTkToplevel(self)
        top.geometry("300x100")
        top.title("Recording...")
        top.attributes("-topmost", True)
        
        lbl = ctk.CTkLabel(top, text=f"{msg}\nRecording in 3...", font=("Arial", 16))
        lbl.pack(expand=True)
        
        def step(count):
            if count > 0:
                lbl.configure(text=f"{msg}\nRecording in {count}...")
                self.after(1000, lambda: step(count-1))
            else:
                x, y = pyautogui.position()
                callback(x, y)
                lbl.configure(text=f"Recorded: {x}, {y}")
                self.after(1000, top.destroy)
                self.refresh_agent_list()

        step(3)

    def toggle_listening(self):
        # Actually failsafe: F8 is always listening if app is open
        pass

    def on_hotkey_trigger(self):
        if not self.is_running:
            return

        agent_name = self.selected_agent_var.get()
        agent_coords = self.config_manager.get_agent_coords(agent_name)
        lock_coords = self.config_manager.get_lock_btn_coords()

        if not lock_coords:
            # print("Lock button not set!") 
            self.label_status.configure(text="LOCK POS MISSING", text_color="red")
            return

        if agent_coords:
            # print(f"Locking {agent_name}...")
            self.label_status.configure(text=f"LOCKED {agent_name}", text_color="cyan")
            self.automator.lock_in(agent_coords, lock_coords)

if __name__ == "__main__":
    app = App()
    app.mainloop()
