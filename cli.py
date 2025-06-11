# Intro project
# Task Scheduler: Get task scheduler to run this script at intervals
import logging
import csv
from file_ops import run_file_ops
from task_parser import parse_cmd
from task_manager import new_task, end_task

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(message)s'
)

def main():

    print("File transfer queue. Type 'quit', 'q' or 'exit' to exit. Type 'help' for command syntax.")

    while True:
        try:
            # Prompt user for command
            cmd = input("> ").strip()
            if cmd.lower() in {"quit", "q", "exit"}:
                logging.info("Exit command received. Shutting down.")
                break

            # Check for help command
            if cmd.lower() == "help":
                print("Available commands:")
                print("move <src> <dest> - Schedule file move from src to dest")
                print("copy <src> <dest> - Schedule file copy from src to dest")
                print("list - List all scheduled tasks")
                print("clear - Clear all scheduled tasks")
                print("remove - Remove a specific task")
                print("Type 'quit', 'q' or 'exit' to exit.")
                continue

            # List all scheduled tasks
            if cmd.lower() in {"list", "ls"}:
                print("Listing all scheduled tasks:")
                csv_path = 'tasks.csv'
                try:
                    with open(csv_path, mode='r', newline='') as file:
                        reader = csv.reader(file)
                        rows = list(reader)

                    if not rows or len(rows) == 1:
                        print("No tasks scheduled.")
                    else:
                        for row in rows[1:]:
                            print(f"{row[0]} -> {row[1]} {row[2]} {row[3]}")
                except FileNotFoundError:
                    print(f"File not found: {csv_path}")
                continue

            # Clear all tasks
            if cmd.lower() in {"clear", "cls"}:
                print("Clearing all tasks...")
                try:
                    with open('tasks.csv', mode='w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(['Timestamp','Task', 'Source', 'Destination'])  # Reset the file with header
                    print("All tasks cleared.")
                except Exception as e:
                    print(f"Error clearing tasks: {e}")
                continue

            # Remove a specific task
            if cmd.lower() in {"remove", "rm"}:
                end_task(cmd)
                continue

            # Add a new task
            new_task(cmd)

        except (KeyboardInterrupt, EOFError):
            print("Shutdown initiated by user (Ctrl+C or Ctrl+D).")
            break
        except Exception as e:
            print("Error in the main loop: ", e)

if __name__ == "__main__":
    main()
