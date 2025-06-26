# Intro project
# Task Scheduler: Get task scheduler to run this script at intervals
import csv
import sys
import time
from task_parser import parse_cmd
from task_manager import create_task, remove_task
from task_executor import execute_scheduled_tasks
from gui import start_gui

def main():
    try:
        # Task execution mode
        if len(sys.argv) == 2 and int(sys.argv[1]) == 1:
            print("Running in task scheduler mode. Executing tasks...")
            execute_scheduled_tasks('localtasks.csv')
            execute_scheduled_tasks('sftptasks.csv')

            print("Task execution completed. Exiting.")
            time.sleep(5)  # Wait before exiting
            return

        # Interactive command line mode
        elif sys.argv[0] == 'main.py' and len(sys.argv) == 1:
            start_gui()
            # print("File transfer queue. Type 'quit', 'q' or 'exit' to exit. Type 'help' for command syntax.")
            # while True:
            #     try:
            #         # Prompt user for command
            #         cmd = input("> ").strip()
            #         if cmd.lower() in {"quit", "q", "exit", "bye"}:
            #             print("Exit command received. Shutting down.")
            #             break

            #         cmd_word = cmd.split()[0].lower() 
                    
            #         # Check for help command
            #         if cmd_word in {"help", "h", "?"}:
            #             print("Available commands:")
            #             print("sftp <upload/download> <local_path> <user>@<host>:<password>:<remote_path> - Schedule SFTP transfer")
            #             print("move/copy <src> <dest> - Schedule local file move/copy from src to dest")
            #             print("list/ls - List all locally scheduled tasks")
            #             print("list/ls sftp - List all sftp scheduled tasks")
            #             print("clear - Clear all locally scheduled tasks")
            #             print("clear sftp - Clear all sftp scheduled tasks")
            #             print("remove - Remove a specific local task")
            #             print("remove sftp - Remove a specific sftp task")
            #             print("Type 'quit', 'q' or 'exit' to exit.")
            #             continue

            #         # List all scheduled tasks
            #         if cmd_word in {"list", "ls"}:
            #             filename = check_sftp(cmd) # TODO improve exceptions
            #             print(f"Listing all scheduled tasks in {filename}:")
            #             try:
            #                 reader = csv.reader(open(filename, mode='r', newline=''))
            #                 rows = list(reader)

            #                 if not rows or len(rows) == 1:
            #                     print(f"No tasks scheduled in {filename}.")
            #                 else:
            #                     for task_number, row in enumerate(rows[1:], start=1):
            #                         print(f"{task_number}: {row[0]} -> {row[1]}")
            #             except FileNotFoundError:
            #                 print(f"Error: {filename}")
            #             continue

            #         # Clear all tasks
            #         if cmd_word in {"clear", "cls"}:
            #             filename = check_sftp(cmd)
            #             confirmation = input(f"This will clear all tasks in {filename}. Are you sure? (yes/no) ").strip().lower()
            #             if confirmation != 'yes' and confirmation != 'y':
            #                 print("Clear operation cancelled.")
            #                 continue
            #             print(f"Clearing all tasks in {filename}...")
            #             try:
            #                 writer = csv.writer(open(filename, mode='w', newline=''))
            #                 writer.writerow(['Timestamp','Command'])  # Reset the file with header
            #                 print("All tasks cleared.")
            #             except Exception as e:
            #                 print(f"Error clearing tasks: {e}")
            #             continue

            #         # Remove a specific task
            #         if cmd_word in {"remove", "rm"}:
            #             remove_task(cmd)
            #             continue

            #         # Add a new task
            #         try: 
            #             parse_cmd(cmd)  # Validate the command
            #             create_task(cmd)  # Create the task
            #         except ValueError as e:
            #             print(f"Error: {e}")
                        
            #     except (KeyboardInterrupt, EOFError):
            #         print("Shutdown initiated by user (Ctrl+C or Ctrl+D).")
            #         break
            #     except Exception as e:
            #         print("Error in the main loop: ", e)
        else: 
            print("Error: Valid arguments are main.py and main.py 1")
    except Exception as e:
        print("Error: Valid arguments are main.py and main.py 1")

if __name__ == "__main__":
    main()
