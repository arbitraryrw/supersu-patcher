#!/usr/bin/env python3

import os
from argparse import ArgumentParser

from src.utils.config import Config
from src.core.core import Core

print(Config.BANNER)

parser = ArgumentParser(description='supersu patcher')

parser.add_argument("-q", "--quiet",
                    action="store_true", 
                    dest="verbose", 
                    default=False,
                    help="don't print status messages to stdout")

parser.add_argument("-p", "--purge",
                    action="store_true", 
                    dest="purge", 
                    default=False,
                    help="purge output directory before running")

parser.add_argument("-o", "--ouput", dest="output_dir",
                    help="output directory for final artifacts", 
                    metavar="DIRECTORY",
                    required=False)


required_args = parser.add_argument_group('required arguments')
required_args.add_argument("-i", "--input", dest="input_file",
                    help="input super su file to patch", 
                    metavar="SUPERSU ZIP",
                    required=True)

args = parser.parse_args()

Config.verbose = args.verbose
Config.purge = args.purge

Config.archive_path = os.path.abspath(args.input_file)

if (not os.path.isfile(Config.archive_path) or 
    Config.archive_path[-4:] != ".zip"):
    exit(f"[ERROR] Could not recognise file " + 
    f"{args.input_file} at {Config.archive_path}")

if args.output_dir is not None:

    abs_output_dir = os.path.abspath(args.output_dir)

    if not os.path.isdir(abs_output_dir):
        exit(f"[ERROR] Unknown output directory {abs_output_dir}")
    
    Config.output_dir_path = os.path.join(abs_output_dir, 
        "supersu_patcher_output")

else:
    Config.root_dir_path = os.path.dirname(os.path.realpath(__file__))
    Config.output_dir_path = os.path.join(Config.root_dir_path, "output")

Config.archive_copy_path = os.path.join(
    Config.output_dir_path, "copy-" + 
    os.path.basename(Config.archive_path)
)

Config.unzip_dir_path = os.path.join(
    Config.output_dir_path, "unzipped-" + 
    os.path.basename(Config.archive_path)
)

Config.output_archive_path = os.path.join(
    Config.output_dir_path, "patched-" + 
    os.path.basename(Config.archive_path)
)

core = Core()
core.start()