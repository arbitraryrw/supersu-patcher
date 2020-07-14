#!/usr/bin/env python3

import os

from src.utils.utils import Utils
from src.utils.config import Config
from src.core.patcher import Patcher

class Core:

    patcher = None
    utils = None

    def __init__(self):
        self.patcher = Patcher()
        self.utils = Utils()

    def start(self):
        print("Starting core logic..")

        self.setup()

    def setup(self): 
        if Config.purge:
            # Recursively delete the old output dir if there is one
            self.utils.delete_dir_tree(Config.output_dir_path)

        # Create an output dir
        self.utils.create_dir(Config.output_dir_path)

        # Create a copy of the original artifact
        self.utils.copy_file(Config.archive_path, Config.archive_copy_path)

        # Unzip archive
        self.utils.unzip_archive(
            Config.archive_copy_path, 
            Config.unzip_dir_path
        )

        # ToDo: Patching functionality
        self.patcher.patch()

        # Zip patched files into output archive
        self.utils.zip_archive(
            Config.unzip_dir_path, 
            Config.output_archive_path
        )