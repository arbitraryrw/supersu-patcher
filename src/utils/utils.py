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

    def unzip_archive(self, archive_path, unzip_dir_path):
        if os.path.isfile(unzip_dir_path) or os.path.isdir(unzip_dir_path):
            exit(f"[ERROR] file {unzip_dir_path} already exists")

        with zipfile.ZipFile(archive_path,"r") as zip_ref:
            zip_ref.extractall(unzip_dir_path)
    
    def zip_archive(self, dir_to_zip_path, output_dir_path):

        files_to_zip = self.get_files_in_dir(dir_to_zip_path)

        with zipfile.ZipFile(output_dir_path,'w') as zip: 
            for file in files_to_zip: 
                # Write the file to the zip but remove the abs path
                zip.write(file, file.replace(dir_to_zip_path,"")) 
        
        if not os.path.isfile(output_dir_path):
            exit(f"[ERROR] unable to copy file {dir_to_zip_path} to {output_dir_path}")

    def get_files_in_dir(self, dir_path):
        file_paths = [] 
    
        # crawling through directory and subdirectories 
        for root, dirs, files in os.walk(dir_path): 
            for filename in files: 
                # join the two strings in order to form the full filepath. 
                filepath = os.path.join(root, filename) 
                file_paths.append(filepath) 
    
        # returning all file paths 
        return file_paths 

    def copy_file(self, src_file, dest_file):
        shutil.copyfile(src_file,dest_file)

        if not os.path.isfile(dest_file):
            exit(f"[ERROR] unable to copy file {src_file} to {dest_file}")

            
        