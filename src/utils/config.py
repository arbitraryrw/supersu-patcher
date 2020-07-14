#!/usr/bin/env python3

class Config:

    VERSION = "0.1"
    BANNER = (
        "_"*35 
        + "\n" + "|" 
        +"-"*9 + "SuperSu Patcher" + "-"*9 
        + "|" 
        + "\n" + "|"+ 
        "-"*20 + f"v{VERSION}" + "-"*9
        + "|" + 
        "\n" + "‾"*35)

    archive_path = None
    root_dir_path = None
    output_dir_path = None
    unzip_dir_path = None
    archive_copy_path = None

    verbose = None
    purge = None

    def __init__(self):
        pass

    def __del__(self):
        pass