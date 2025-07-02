# Intro project
# Task Scheduler: Get task scheduler to run this script at intervals
import sys
from .task_executor import execute_scheduled_tasks
from .gui import start_gui

def main():
    start_gui()
    try:
        # Task execution mode
        if len(sys.argv) == 2 and int(sys.argv[1]) == 1:
            print("Running in task scheduler mode. Executing tasks...")
            execute_scheduled_tasks('localtasks.csv')
            execute_scheduled_tasks('sftptasks.csv')

            print("Task execution completed. Exiting.")
            # time.sleep(5)  # Wait before exiting
            return

        # Interactive command line mode
        elif sys.argv[0] == 'main.py' and len(sys.argv) == 1:
            start_gui()

        else: 
            print(sys.argv[0])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
