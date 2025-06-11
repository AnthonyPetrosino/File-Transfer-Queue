import csv
from datetime import datetime
from task_parser import parse_cmd

def new_task(cmd):
    # Parse the command to get task, source, and destination
    task, src, dest = parse_cmd(cmd)

    # Record the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Create a new task entry
    with open('tasks.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            # Write header if file is empty
            writer.writerow(['Timestamp','Task', 'Source', 'Destination'])
        writer.writerow([timestamp,task, src, dest])

        print("New task added: ", task, src, dest)

def end_task(cmd):
    print("Removing a task...")
    try:
        # Read the existing tasks
        with open('tasks.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        if len(rows) <= 1:
            print("No tasks to remove.")
            return

        # Display tasks for selection
        print("Select a task to remove (by number):")
        for i, row in enumerate(rows[1:], start=1):
            print(f"{i}: {row[0]} -> {row[1]} {row[2]} {row[3]}")

        # Get user input for task number
        task_num = int(input("Enter task number to remove: ")) - 1

        if 0 <= task_num < len(rows) - 1:
            del rows[task_num + 1]  # +1 because of header row
            with open('tasks.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Task removed successfully.")
        else:
            print("Invalid task number.")
    except Exception as e:
        print(f"Error removing task: {e}")
    return