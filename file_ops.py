# Handles resolving/validating path and file manipulation functionality.
# Current operations:
# move: TODO
# copy: TODO
# upload: TODO

import os

def resolve_path(path: str):
    return os.path.abspath(path)

def validate_path(src, dest):
    if not os.path.exists(path):
        raise FileNotFoundError("Soure file does not exist: ", src)
    dest_dir = dest if os.path.isdir(dest) else os.path.dirname(dest)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

def move_file(src, dest):
    os.rename(src, dest)
    print("done!")