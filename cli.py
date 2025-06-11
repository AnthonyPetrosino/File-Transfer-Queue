# Intro project
# Task scheduler
import logging
import threading
import schedule
from file_ops import run_file_ops
from task_parser import parse_cmd
from scheduler import run_scheduler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(threadName)s - %(message)s'
)

def main():

    # Start the scheduler in a separate thread
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True, name="Scheduler")
    scheduler_thread.start()

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
                print("move <src> <dest> - Move file from src to dest")
                print("copy <src> <dest> - Copy file from src to dest")
                print("Type 'quit', 'q' or 'exit' to exit.")
                continue

            if cmd.lower() in {"list", "ls"}:
                print("Listing all scheduled tasks:")
                jobs = schedule.get_jobs()
                if not jobs:
                    print("No tasks scheduled yet.")
                else:
                    print("Scheduled tasks:")
                    for job in jobs:
                        print(f" - {job}")
                continue

            # Parse the command to get task, source, and destination
            task, src, dest = parse_cmd(cmd)

            run_file_ops(task, src, dest)

            # Schedule the task            

            # Prompt user for interval
            # print("How often should the task be executed (in minutes)?")
            # interval = input(cmd + "> ")
            # while not interval.isdigit() or int(interval) <= 0:
            #     print("Please enter a valid integer number for the interval.")
            #     interval = input(cmd + "> ")
            #     if interval.lower() in {"quit", "q", "exit"}:
            #         return

            # schedule.every(int(interval)).minutes.do(run_file_ops, task=task, src=src, dest=dest)
            # logging.info(f"Scheduled task: {cmd} to run every {interval} minute(s).")
            # print(f"Task '{cmd}' scheduled to run every {interval} minute(s).")

        except (KeyboardInterrupt, EOFError):
            print("Shutdown initiated by user (Ctrl+C or Ctrl+D).")
            break
        except Exception as e:
            print("Error in the main loop: ", e)

if __name__ == "__main__":
    main()
