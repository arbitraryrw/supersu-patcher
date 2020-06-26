

from src.utils.config import Config
from src.core.patcher import Patcher

class Core:
    
    patcher = None

    def __init__(self):
        self.patcher = Patcher()

    def start(self):
        print("Starting core logic..")