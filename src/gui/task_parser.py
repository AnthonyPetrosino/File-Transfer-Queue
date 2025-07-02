# Parse user input
import shlex

def parse_cmd(cmd: str):
    tokens = shlex.split(cmd.strip())
    task = tokens[0].lower()

    # Check for move or copy commands
    if task in {"move", "copy"}:
        if len(tokens) != 3:
            raise ValueError("Invalid syntax for move/copy. Use: move/copy <src> <dest>.")
        task, src, dest = tokens
        return task, src, dest

    # Check for sftp command
    elif task == "sftp":
        if len(tokens) != 4:
            raise ValueError("Invalid syntax for sftp. Use: sftp <direction> <local_path> <user>@<host>:<password>:<remote_path>")
        
        direction = tokens[1].lower()
        local_path = tokens[2]
        remote_details = tokens[3]
        
        if direction not in {"upload", "download"}:
            raise ValueError("Invalid sftp direction. Use 'upload' or 'download'.")
        
        return task, direction, local_path, remote_details

    else:
        raise ValueError(f"Invalid command: '{task}'. Type 'help' for command syntax.")