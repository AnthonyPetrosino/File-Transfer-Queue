import csv
from tkinter import *
from tkinter.ttk import Treeview, Combobox
from tkinter import filedialog, messagebox
from task_manager import create_task, remove_task
from task_executor import execute_scheduled_tasks_root
import shlex

def show_csv(root, selected_csv_file):
    # Function to display the selected CSV file
    try:
        with open(selected_csv_file, 'r') as file: 
            content = file.read()

            # Clear previous content
            for widget in root.grid_slaves():
                if isinstance(widget, Label) and widget.grid_info()['row'] == 3:
                    widget.destroy()

            tree_frame = Frame(root)
            tree_frame.grid(row=4, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

            # Vertical scrollbar
            scrollbar = Scrollbar(tree_frame)
            scrollbar.pack(side=RIGHT, fill=Y)

            csv_tree = Treeview(tree_frame, yscrollcommand=scrollbar.set)
            scrollbar.config(command=csv_tree.yview)

            csv_tree['columns'] = ('ID', 'Timestamp', 'Command') # Define the columns
            csv_tree.column("#0", width=0, stretch=NO) # Hide the default first column
            csv_tree.column("ID", width=50, anchor=W)
            csv_tree.column("Timestamp", width=150, anchor=W)
            csv_tree.column("Command", width=400, anchor=CENTER)
            csv_tree.heading("ID", text="ID", anchor=W)
            csv_tree.heading("Timestamp", text="Timestamp", anchor=W)
            csv_tree.heading("Command", text="Command", anchor=W)

            # Populate the Treeview with the csv content
            for i, line in enumerate(content.splitlines()):
                if i == 0:
                    continue  # Skip csv header
                try:
                    timestamp, command = line.split(",", 1)
                    csv_tree.insert("", "end", iid=str(i), values=(i, timestamp.strip(), command.strip()))
                except ValueError:
                    continue

            csv_tree.pack(side=LEFT, fill=BOTH, expand=True)
            root.csv_tree = csv_tree # Store the treeview in root for access by other functions

            if selected_csv_file == "localtasks.csv":
                local_task_type_var = StringVar()
                local_task_type_dropdown = Combobox(root, textvariable=local_task_type_var, state="readonly", font=("Arial", 12))
                local_task_type_dropdown['values'] = ("Move", "Copy")
                local_task_type_dropdown.grid(row=8, column=0, padx=10, pady=10)
                local_task_type_dropdown.set("Move")
                root.task_type_var = local_task_type_var  # Store the StringVar in root
            elif selected_csv_file == "sftptasks.csv":
                sftp_task_type_var = StringVar()
                sftp_task_type_dropdown = Combobox(root, textvariable=sftp_task_type_var, state="readonly", font=("Arial", 12))
                sftp_task_type_dropdown['values'] = ("Upload", "Download")
                sftp_task_type_dropdown.grid(row=8, column=0, padx=10, pady=10)
                sftp_task_type_dropdown.set("Upload")

    except FileNotFoundError:
        root.log_output(f"Error: {selected_csv_file} not found.")

def create_task_btn(root, selected_csv_file):
    # Check if source and destination paths are selected
    if not hasattr(root, 'source_path') or not root.source_path:
        root.log_output("Please select a source file first.")
        return
    if not hasattr(root, 'destination_path') or not root.destination_path:
        root.log_output("Please select a destination folder first.")
        return

    # Get the selected task type (move/copy upload/download)
    task_type = root.task_type_var.get().lower()

    # Quote paths to handle spaces correctly, resolves parsing error
    quoted_source_path = shlex.quote(root.source_path)
    quoted_destination_path = shlex.quote(root.destination_path)

    if selected_csv_file == "localtasks.csv":
        # Construct the command string
        cmd = f"{task_type} {quoted_source_path} {quoted_destination_path}"
        create_task(cmd, selected_csv_file=selected_csv_file, root=root)
        show_csv(root, selected_csv_file)

def remove_task_btn(root, selected_csv_file):
    # Function to remove a task from the queue
    if hasattr(root, 'csv_tree'):
        selected_item = root.csv_tree.selection() # Retrieve the tree's item identifier (row id)
        if selected_item:
            task_id = int(root.csv_tree.item(selected_item[0])['values'][0])
            remove_task(root, task_id - 1, selected_csv_file) # Call remove function
            show_csv(root, selected_csv_file) # Refresh the Treeview
            root.log_output(f"Successfully removed task number {task_id}.")
        else:
            root.log_output("No task selected to remove.")
    else:
        root.log_output("CSV not displayed.")

def clear_csv_btn(root):
    # Function to clear tasks in csv
    if hasattr(root, 'csv_tree'):
        current_file = root.selected_csv.get() if hasattr(root, 'selected_csv') else "localtasks.csv"
        confirm = messagebox.askyesno("Confirm Clear", f"This will clear all tasks in {current_file}. Are you sure?")
        if not confirm:
            root.log_output("Clear operation cancelled.")
            return

        try:
            with open(current_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Timestamp', 'Command'])  # Write header only
            show_csv(root, current_file)  # Refresh the view
            root.log_output(f"All tasks in {current_file} cleared.")
        except Exception as e:
            root.log_output(f"Error clearing tasks: {e}")
    else:
        root.log_output("No CSV file loaded to clear.")

def execute_csv_btn(root):
    # Function to execute the selected csv
    selected_file = root.selected_csv.get()
    root.log_output(f"Executing tasks from {selected_file}...")

    try:
        execute_scheduled_tasks_root(root, selected_file)
        root.log_output(f"Finished executing tasks from {selected_file}.")
    except Exception as e:
        root.log_output(f"Error executing tasks: {e}")

def open_source_file(root):
    # Function to open the source file path
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file")
    root.source_path = root.filename
    source_file_result = Label(root, text=root.filename)
    source_file_result.grid(row=6, column=0, padx=10, pady=10)

def open_destination_folder(root):
    # Function to open the destination folder path
    root.filename = filedialog.askdirectory(initialdir="/", title="Select destination folder")
    root.destination_path = root.filename
    destination_file_result = Label(root, text=root.filename)
    destination_file_result.grid(row=7, column=0, padx=10, pady=10)
