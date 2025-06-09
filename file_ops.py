# Handles resolving/validating path and file manipulation functionality.
# Current operations:
# move:
# copy: 
# upload: TODO

import os
import shutil

# Parse and execute a file operation
def run_file_ops(task, src, dest):
    try:
        # Resolve the paths
        src = resolve_path(src)
        print("Source: ", src)
        dest = resolve_path(dest)
        print("Destination: ", dest)
        # Execute the task
        if task == "move":
            move_file(src, dest)
        elif task == "copy":
            copy_file(src, dest)
    except Exception as e:
        print(f"Failed to execute task '{task} {src} {dest}'. Error: {e}")

def resolve_path(path: str):
    return os.path.abspath(path)

def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Success, moved {src} to {dest}")

def copy_file(src, dest):
    shutil.copy(src, dest)
    print(f"Success, copied {src} to {dest}")