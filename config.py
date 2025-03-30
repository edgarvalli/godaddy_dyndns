import json
from dataclasses import dataclass
from typing import List,Dict

@dataclass
class Task:
    domain: str
    record_name: str
    record_type: str
    last_public_ip: str
    

class Config:
    GODADDY_API_KEY: str
    GODADDY_API_SECRET: str
    TIMEOUT: float
    tasks: List[Task] = []
    
    def __init__(self):
        self.load_config()

    def load_config(self):
        with open("config.json", "r") as config_file:
            config_data = json.load(config_file)
            self.GODADDY_API_KEY = config_data["GODADDY_API_KEY"]
            self.GODADDY_API_SECRET = config_data["GODADDY_API_SECRET"]
            self.TIMEOUT = config_data["TIMEOUT"]
            tasks = config_data["tasks"]
            for task in tasks:
                task = Task(**task)
                self.tasks.append(task)
    
    def set_public_ip(self, domain, ip):
        for task in self.tasks:
            if task.domain == domain:
                task.last_public_ip = ip
                break
        self.save_config()

    def save_config(self):
        with open("config.json", "w") as config_file:
            json.dump(self.__dict__, config_file, indent=4)

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)
        self.save_config()

    def __delitem__(self, key):
        delattr(self, key)
        self.save_config()

    def __contains__(self, key):
        return hasattr(self, key)

    def __iter__(self):
        return iter(vars(self))

    def __len__(self):
        return len(vars(self))

    def __str__(self):
        return str(vars(self))

    def __repr__(self):
        return repr(vars(self))

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __ne__(self, other):
        return vars(self) != vars(other)