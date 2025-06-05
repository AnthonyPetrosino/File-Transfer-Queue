# Intro project

import os 
import shutil #
import sys
from task_parser import parse_cmd
from file_ops import resolve_path, move_file

# def parse_command(command: str):

def main():
    print("File transfer queue (local mode). Type 'quit', 'q' or 'exit' to exit.")
    while True:
        try:
            cmd = input("> ").strip()
            if cmd.lower() in {"quit", "q", "exit"}:
                break

            task, src, dest = parse_cmd(cmd)
            src = resolve_path(src)
            dest = resolve_path(dest)
            if task == "move":
                move_file(src, dest)
            elif task == "copy":
                move_file(src, dest)
        except Exception as e:
            print("Error: ", e)

if __name__ == "__main__":
    main()
