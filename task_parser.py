# Parse user input

def parse_cmd(cmd: str):
    tokens = cmd.strip().split()
    # Check if the command has the correct format
    if len(tokens) != 3 or tokens[0].lower() not in {"move", "copy"}:
        raise ValueError("Invalid syntax. Use: move <src> <dest> or copy <src> <dest>")
    # Return the task, source, and destination from the tokens
    task, src, dest = tokens
    return task, src, dest