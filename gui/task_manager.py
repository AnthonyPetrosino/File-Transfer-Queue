from tkinter import *
import csv
import os
from datetime import datetime

def create_task(cmd):
    # Record the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Determine the kind of task
    if cmd.split()[0].lower() == 'sftp':
        selected_csv_file = 'sftptasks.csv'
    else:
        selected_csv_file = 'localtasks.csv'

    # Create the tasks.csv file if it does not exist
    if not os.path.exists(selected_csv_file):
        writer = csv.writer(open(selected_csv_file, mode='w', newline=''))
        writer.writerow(['Timestamp', 'Command'])

    # Create a new task entry
    writer = csv.writer(open(selected_csv_file, mode='a', newline=''))
    if open(selected_csv_file, mode='a', newline='').tell() == 0:
        # Write header if file is empty
        writer.writerow(['Timestamp','Command'])
    writer.writerow([timestamp, cmd])

    print(f"New task added: {cmd}")

def remove_task(root, task_id, selected_csv_file):
    try:
        # Read the existing tasks
        reader = csv.reader(open(selected_csv_file, mode='r', newline=''))
        rows = list(reader)

        if len(rows) <= 1:
            remove_task_result = Label(root, text=f"{selected_csv_file} is empty.", bg='white', fg='#ba0e0e', font=("Arial", 14))
            remove_task_result.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
            return

        if 0 <= task_id < len(rows) - 1:
            del rows[task_id + 1]  # +1 because of header row
            writer = csv.writer(open(selected_csv_file, mode='w', newline=''))
            writer.writerows(rows)

    except FileNotFoundError:
            remove_task_result = Label(root, text=f"{selected_csv_file} not found.", bg='white', fg='#ba0e0e', font=("Arial", 14))
            remove_task_result.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
    except Exception as e:
            remove_task_result = Label(root, text=f"Error removing task:{e}.", bg='white', fg='#ba0e0e', font=("Arial", 14))
            remove_task_result.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
    return