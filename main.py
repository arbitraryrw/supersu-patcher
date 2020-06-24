#!/usr/bin/env python3

import os
from argparse import ArgumentParser

print("[INFO] supersu patcher running...")


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

if not os.path.isfile(abs_zip_path):
    exit(f"[ERROR] Could not recognise file {args.input_file} at {abs_zip_path}")



