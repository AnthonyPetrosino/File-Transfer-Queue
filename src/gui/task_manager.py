from tkinter import *
import csv
import os
from datetime import datetime

def create_task(cmd, selected_csv_file, root):
    # Record the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

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

    root.log_output(f"New task added to {selected_csv_file}")

def remove_task(root, task_id, selected_csv_file):
    try:
        # Read the existing tasks
        reader = csv.reader(open(selected_csv_file, mode='r', newline=''))
        rows = list(reader)

        if len(rows) <= 1:
            root.log_output(f"{selected_csv_file} is empty.")
            return

        if 0 <= task_id < len(rows) - 1:
            del rows[task_id + 1]  # +1 because of header row
            writer = csv.writer(open(selected_csv_file, mode='w', newline=''))
            writer.writerows(rows)

    except FileNotFoundError:
            root.log_output(f"{selected_csv_file} not found.")
    except Exception as e:
            root.log_output(f"Error removing task:{e}.")
    return