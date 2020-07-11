#!/usr/bin/env python3

class Config:

    BANNER = "-"*10 + "SuperSu Patcher Running" + "-"*10

    archive_path = None
    root_dir_path = None
    output_dir_path = None
    unzip_dir_path = None

    verbose = None
    purge = None

    def __init__(self):
        pass

    def __del__(self):
        pass