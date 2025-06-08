# Handles resolving/validating path and file manipulation functionality.
# Current operations:
# move:
# copy: TODO
# upload: TODO

import os
import shutil

def resolve_path(path: str):
    return os.path.abspath(path)

def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Moved {src} to {dest}")

def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Copied {src} to {dest}")