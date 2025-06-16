# Parse user input

def parse_cmd(cmd: str):
    tokens = cmd.strip().split()
    command = tokens[0].lower()

    # Check for move or copy commands
    if command in {"move", "copy"}:
        if len(tokens) != 3:
            raise ValueError("Invalid syntax for move/copy. Type 'help' for command syntax.")
        task, src, dest = tokens
        return command, src, dest

    # Check for sftp command
    elif command == "sftp":
        if len(tokens) != 4:
            raise ValueError("Invalid syntax for sftp. Use: sftp <direction> <local_path> <user>@<host>:<password>:<remote_path>")
        
        direction = tokens[1].lower()
        local_path = tokens[2]
        remote_details = tokens[3]
        
        if direction not in {"upload", "download"}:
            raise ValueError("Invalid sftp direction. Use 'upload' or 'download'.")
        
        return command, direction, local_path, remote_details

    else:
        raise ValueError("Invalid command. Type 'help' for command syntax.")