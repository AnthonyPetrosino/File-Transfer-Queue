import csv
import os
from datetime import datetime

def create_task(cmd):
    # Record the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Determine the kind of task
    if cmd.split()[0].lower() == 'sftp':
        filename = 'sftptasks.csv'
    else:
        filename = 'localtasks.csv'

    # Create the tasks.csv file if it does not exist
    if not os.path.exists(filename):
        writer = csv.writer(open(filename, mode='w', newline=''))
        writer.writerow(['Timestamp', 'Command'])

    # Create a new task entry
    writer = csv.writer(open(filename, mode='a', newline=''))
    if open(filename, mode='a', newline='').tell() == 0:
        # Write header if file is empty
        writer.writerow(['Timestamp','Command'])
    writer.writerow([timestamp, cmd])

    print(f"New task added: {cmd}")

def remove_task(task_num, filename):
    # filename = check_sftp(cmd)
    # print("Removing a task...")
    try:
        # Read the existing tasks
        reader = csv.reader(open(filename, mode='r', newline=''))
        rows = list(reader)

        if len(rows) <= 1:
            print("No tasks to remove.")
            return

        # Display tasks for selection
        # print("Select a task to remove (by number):")
        # for i, row in enumerate(rows[1:], start=1):
        #     print(f"{i}: {row[0]} -> {row[1]}")

        # # Get user input for task number
        # task_num = int(input("Enter task number to remove: ")) - 1

        if 0 <= task_num < len(rows) - 1:
            del rows[task_num + 1]  # +1 because of header row
            writer = csv.writer(open(filename, mode='w', newline=''))
            writer.writerows(rows)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print(f"No {filename} file found. Please create a task first.")
    except Exception as e:
        print(f"Error removing task: {e}")
    return

def check_sftp(cmd):
    # try: TODO
        if len(cmd.split()) == 1:
            return 'localtasks.csv'
        elif len(cmd.split()) == 2:
            if cmd.split()[1].lower() == 'sftp':
                return 'sftptasks.csv'
            else:
                return "Invalid command. Type 'help' for command syntax." 
        else:
            return "Invalid command. Type 'help' for command syntax."
    # except