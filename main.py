#!/usr/bin/env python3

import os
import shutil
import zipfile
from argparse import ArgumentParser

print("[INFO] supersu patcher running...")

from src.utils.utils import Utils
from src.utils.config import Config
from src.core.patcher import Patcher

u = Utils()
c = Config()
p = Patcher()

exit(1)

parser = ArgumentParser(description='supersu patcher')

parser.add_argument("-q", "--quiet",
                    action="store_false", 
                    dest="verbose", 
                    default=True,
                    help="don't print status messages to stdout")


required_args = parser.add_argument_group('required arguments')
required_args.add_argument("-i", "--input", dest="input_file",
                    help="input super su file to patch", 
                    metavar="SUPERSU ZIP",
                    required=True)


args = parser.parse_args()

abs_zip_path = os.path.abspath(args.input_file)

if not os.path.isfile(abs_zip_path) or abs_zip_path[-4:] != ".zip":
    exit(f"[ERROR] Could not recognise file {args.input_file} at {abs_zip_path}")

root_path = os.path.dirname(os.path.realpath(__file__))
output_path = os.path.join(root_path, "output")

base_zip_name = os.path.basename(abs_zip_path)
unzip_abs_path = os.path.join(output_path, "unzipped-" + base_zip_name)

# Recursively delete the old output dir if there is one
if os.path.isdir(output_path):
    try:
        shutil.rmtree(output_path)
    except OSError:
        print ("Deletion of the directory %s failed" % path)

# Create an output dir
try:
    os.makedirs(output_path)
except OSError:
    print ("Creation of the directory %s failed" % output_path)
else:
    print ("Successfully created the directory %s" % output_path)

with zipfile.ZipFile(abs_zip_path,"r") as zip_ref:
    zip_ref.extractall(os.path.join(output_path, "unzipped-" + base_zip_name))