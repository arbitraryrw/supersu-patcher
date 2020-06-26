#!/usr/bin/env python3

import os
import zipfile
import shutil

class Utils:

    def __init__(self):
        print("Utils running..")
        pass

    
    def delete_dir_tree(self, dir_path):
        if os.path.isdir(dir_path):
            try:
                shutil.rmtree(dir_path)
            except OSError:
                print ("Deletion of the directory %s failed" % dir_path)

    def create_dir(self, output_dir_path):
        try:
            os.makedirs(output_dir_path)
        except OSError:
            print ("Creation of the directory %s failed" % output_dir_path)
        else:
            print ("Successfully created the directory %s" % output_dir_path)

    def unzip(self, archive_path, output_dir_path):

        base_name = os.path.basename(archive_path)

        unzip_archive_path = os.path.join(output_dir_path, "unzipped-" + base_name)


        with zipfile.ZipFile(archive_path,"r") as zip_ref:
            zip_ref.extractall(unzip_archive_path)

        return unzip_archive_path
            
        