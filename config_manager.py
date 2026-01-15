import json
import os

CONFIG_FILE = "config.json"

class ConfigManager:
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(CONFIG_FILE):
            return {"agents": {}, "lock_btn": None}
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {"agents": {}, "lock_btn": None}

    def save_config(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.config, f, indent=4)

    def add_agent(self, name, x, y):
        self.config["agents"][name] = {"x": x, "y": y}
        self.save_config()

    def get_agent_coords(self, name):
        return self.config["agents"].get(name)

    def set_lock_btn(self, x, y):
        self.config["lock_btn"] = {"x": x, "y": y}
        self.save_config()

    def get_lock_btn_coords(self):
        return self.config.get("lock_btn")

    def get_all_agents(self):
        return list(self.config["agents"].keys())

    def remove_agent(self, name):
        if name in self.config["agents"]:
            del self.config["agents"][name]
            self.save_config()
