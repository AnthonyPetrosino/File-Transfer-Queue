# Handles resolving/validating path and file manipulation functionality.
# Current operations:
# move:
# copy: 
# upload: TODO

import os
import shutil
import time

# Parse and execute a file operation
def run_file_ops(task, src, dest, task_number):
    try:
        # Resolve the file paths
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
        print(f"\nFailed to execute task #{task_number}:\n{task} {src} {dest}\nError: {e}\n")
        time.sleep(5)

# Resolve the file paths
def resolve_path(path: str):
    return os.path.abspath(path)

# Move functionality
def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Success, moved {src} to {dest}")

# Copy functionality
def copy_file(src, dest):
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)
    print(f"Success, copied {src} to {dest}")