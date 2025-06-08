# Handles resolving/validating path and file manipulation functionality.
# Current operations:
# move:
# copy: TODO
# upload: TODO

import os

def resolve_path(path: str):
    return os.path.abspath(path)

def move_file(src, dest):
    os.rename(src, dest)
    print("done!")

def copy_file(src, dest):
    os.system(f"copy {src} {dest}")
    print("done!")