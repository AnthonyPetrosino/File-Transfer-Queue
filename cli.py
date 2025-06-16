# Intro project
# Task Scheduler: Get task scheduler to run this script at intervals
import csv
import sys
import time
from file_ops import run_file_ops
from task_parser import parse_cmd
from task_manager import create_task, remove_task

def main():

    if len(sys.argv) == 2 and int(sys.argv[1]) == 1:
        # Task scheduler to run this script at intervals
        print("Running in task scheduler mode. Executing tasks...")

        # Read and execute tasks from the CSV file
        try:
            with open('localtasks.csv', mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

            if len(rows) <= 1:
                print("No tasks to execute.")
                return

            for task_number, row in enumerate(rows[1:], start=1):
                cmd_str = row[1]
                try:
                    task, *args = parse_cmd(cmd_str)
                    run_file_ops(task, *args, task_number)
                except ValueError as e:
                    print(f"Skipping invalid task #{task_number}: '{cmd_str}'. {e}")
                    time.sleep(5)
                time.sleep(0.1)  # Sleep to simulate task execution time

        except FileNotFoundError:
            print("Unable to locate localtasks.csv. Please ensure it exists.")
            time.sleep(5)

        print("Task execution completed. Exiting.")
        time.sleep(5)  # Wait before exiting
        return

    else:
        print("File transfer queue. Type 'quit', 'q' or 'exit' to exit. Type 'help' for command syntax.")
        while True:
            try:
                # Prompt user for command
                cmd = input("> ").strip()
                if cmd.lower() in {"quit", "q", "exit", "bye"}:
                    print("Exit command received. Shutting down.")
                    break

                cmd_word = cmd.split()[0].lower() 

                # Check for help command
                if cmd_word in {"help", "h", "?"}:
                    print("Available commands:")
                    print("sftp <upload/download> <local_path> <user>@<host>:<password>:<remote_path> - Schedule SFTP transfer")
                    print("<move/copy> <src> <dest> - Schedule local file move/copy from src to dest")
                    print("list - List all scheduled tasks")
                    print("clear - Clear all scheduled tasks")
                    print("remove - Remove a specific task")
                    print("Type 'quit', 'q' or 'exit' to exit.")
                    continue

                # List all scheduled tasks
                if cmd_word in {"list", "ls"}:
                    print("Listing all scheduled tasks:")
                    try:
                        reader = csv.reader(open('localtasks.csv', mode='r', newline=''))
                        rows = list(reader)

                        if not rows or len(rows) == 1:
                            print("No tasks scheduled.")
                        else:
                            for task_number, row in enumerate(rows[1:], start=1):
                                print(f"{task_number}: {row[0]} -> {row[1]}")
                    except FileNotFoundError:
                        print(f"File not found: 'localtasks.csv'")
                    continue

                # Clear all tasks
                if cmd_word in {"clear", "cls"}:
                    confirmation = input("This will clear all tasks. Are you sure? (yes/no) ").strip().lower()
                    if confirmation != 'yes' and confirmation != 'y':
                        print("Clear operation cancelled.")
                        continue
                    print("Clearing all tasks...")
                    try:
                        writer = csv.writer(open('localtasks.csv', mode='w', newline=''))
                        writer.writerow(['Timestamp','Task', 'Source', 'Destination'])  # Reset the file with header
                        print("All tasks cleared.")
                    except Exception as e:
                        print(f"Error clearing tasks: {e}")
                    continue

                # Remove a specific task
                if cmd_word in {"remove", "rm"}:
                    remove_task(cmd)
                    continue

                # Add a new task
                try: 
                    parse_cmd(cmd)  # Validate the command
                    create_task(cmd)  # Create the task
                except ValueError as e:
                    print(f"Error: {e}")
                    
            except (KeyboardInterrupt, EOFError):
                print("Shutdown initiated by user (Ctrl+C or Ctrl+D).")
                break
            except Exception as e:
                print("Error in the main loop: ", e)

if __name__ == "__main__":
    main()
