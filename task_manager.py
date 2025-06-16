import csv
import os
from datetime import datetime

def create_task(cmd):
    # Record the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Create the tasks.csv file if it does not exist
    if not os.path.exists('localtasks.csv'):
        writer = csv.writer(open('localtasks.csv', mode='w', newline=''))
        writer.writerow(['Timestamp', 'Command'])

    # Create a new task entry
    writer = csv.writer(open('localtasks.csv', mode='a', newline=''))
    if open('localtasks.csv', mode='a', newline='').tell() == 0:
        # Write header if file is empty
        writer.writerow(['Timestamp','Command'])
    writer.writerow([timestamp, cmd])

    print(f"New task added: {cmd}")

def remove_task(cmd):
    print("Removing a task...")
    try:
        # Read the existing tasks
        reader = csv.reader(open('localtasks.csv', mode='r', newline=''))
        rows = list(reader)

        if len(rows) <= 1:
            print("No tasks to remove.")
            return

        # Display tasks for selection
        print("Select a task to remove (by number):")
        for i, row in enumerate(rows[1:], start=1):
            print(f"{i}: {row[0]} -> {row[1]}")

        # Get user input for task number
        task_num = int(input("Enter task number to remove: ")) - 1

        if 0 <= task_num < len(rows) - 1:
            del rows[task_num + 1]  # +1 because of header row
            writer = csv.writer(open('localtasks.csv', mode='w', newline=''))
            writer.writerows(rows)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")

    except FileNotFoundError:
        print("No localtasks.csv file found. Please create a task first.")
    except Exception as e:
        print(f"Error removing task: {e}")
    return