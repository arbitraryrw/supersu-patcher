#!/usr/bin/env python3

import os
import zipfile
import shutil

class Utils:

    def __init__(self):
        pass
    
    def delete_dir_tree(self, dir_path):
        if os.path.isdir(dir_path):
            try:
                shutil.rmtree(dir_path)
            except OSError:
                print ("Deletion of the directory %s failed" % dir_path)

    def create_dir(self, output_dir_path):
        if os.path.isfile(output_dir_path) or os.path.isdir(output_dir_path):
            exit(f"[ERROR] file {output_dir_path} already exists")

        try:
            os.makedirs(output_dir_path)
        except OSError:
            print (f"[ERROR]Creation of the directory {output_dir_path} failed")
        else:
            pass

    def unzip(self, archive_path, unzip_dir_path):
        if os.path.isfile(unzip_dir_path) or os.path.isdir(unzip_dir_path):
            exit(f"[ERROR] file {unzip_dir_path} already exists")

        with zipfile.ZipFile(archive_path,"r") as zip_ref:
            zip_ref.extractall(unzip_dir_path)

            
        