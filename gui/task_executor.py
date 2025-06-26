from tkinter import *
import csv
import time
from file_ops import run_file_ops
from task_parser import parse_cmd

def execute_scheduled_tasks(root, selected_csv_file):
        # Read and execute tasks from the given CSV file
        executing_tasks = Label(root, text=f"Executing tasks...", bg='white', fg='#ba0e0e', font=("Arial", 14))
        executing_tasks.grid(row=3, column=0, columnspan=5, padx=10, pady=10)
        try:
            with open(selected_csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows = list(reader)

            if len(rows) <= 1:
                print("No tasks to execute.")
            else:
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
            print(f"Unable to locate {selected_csv_file}. Please ensure it exists.")
            time.sleep(5)