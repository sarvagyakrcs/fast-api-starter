from dotenv import load_dotenv
import os
from app.config import ENV_FILE_PATH

class LoadEnv:
    def __init__(self, env_path: str):
        self.env_path = env_path
        self.load_env()

    def load_env(self) -> None:
        if(os.path.exists(self.env_path)):
            load_dotenv(self.env_path)
        else:
            raise FileNotFoundError(f"Environment file not found at {self.env_path}")

    def get_env_variable(self, variable_name: str) -> str:
        if(os.getenv(variable_name)):
            return os.getenv(variable_name)
        else:
            raise ValueError(f"Environment variable {variable_name} not found")

env = LoadEnv(ENV_FILE_PATH)