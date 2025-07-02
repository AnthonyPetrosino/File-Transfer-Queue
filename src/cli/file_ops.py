# Handles resolving/validating path and file manipulation functionality.
# Current operations:
# move:
# copy: 
# upload:
# download:

import os
import shutil
import time
import paramiko

# Parse and execute a file operation
def run_file_ops(task, *args):
    try:
        task_number = args[-1]
        print(f"\nExecuting task #{task_number}: {task} {' '.join(args[:-1])}") # Print the task being executed

        if task in {"move", "copy"}:
            # Resolve source and destination paths
            src, dest = args[0], args[1]
            src = resolve_path(src)
            print("Source: ", src)
            dest = resolve_path(dest)
            print("Destination: ", dest)
            # Execute the task
            if task == "move":
                move_file(src, dest)
            elif task == "copy":
                copy_file(src, dest)
        # Handle SFTP tasks
        elif task == "sftp":
            direction, local_path, remote_details = args[0], args[1], args[2]
            sftp_task(direction, local_path, remote_details)

    except Exception as e:
        print(f"\nFailed to execute task #{task_number}:\n{task} {src} {dest}\nError: {e}\n")
        time.sleep(5)

# Handle SFTP tasks
def sftp_task(direction, local_path, remote_details):
    try:
        user_host, password, remote_path = remote_details.split(':', 2)
        user, host = user_host.split('@')

        # Setup transport object for SFTP connection
        with paramiko.Transport((host, 22)) as transport:   # TODO: Make port configurable?
            transport.connect(None, username=user, password=password)
            # Create SFTP client
            with paramiko.SFTPClient.from_transport(transport) as sftp:
                print(f"Connected to {host} as {user}.")
                if direction == "upload":
                    sftp.put(local_path, remote_path)
                    print(f"Success, uploaded {local_path} to {remote_path}")
                elif direction == "download":
                    sftp.get(remote_path, local_path)
                    print(f"Success, downloaded {remote_path} to {local_path}")
                else:
                    raise ValueError("Invalid SFTP direction. Use 'upload' or 'download'.")
            
            sftp.close()
            transport.close()
            print("SFTP connection closed.")

    except Exception as e:
        print(f"Error during SFTP transfer: {e}")

# Resolve the file paths
def resolve_path(path: str):
    return os.path.abspath(path)

# Local move functionality
def move_file(src, dest):
    shutil.move(src, dest)
    print(f"Success, moved {src} to {dest}")

# Local copy functionality
def copy_file(src, dest):
    if os.path.isdir(src):
        shutil.copytree(src, dest)
    else:
        shutil.copy(src, dest)
    print(f"Success, copied {src} to {dest}")