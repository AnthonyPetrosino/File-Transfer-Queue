import csv
from tkinter import *
from tkinter.ttk import Treeview
from tkinter import filedialog, messagebox
from task_manager import create_task, remove_task

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
                        move_button = Button(root, text="Move", command=lambda:move_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to move files
                        move_button.grid(row=8, column=0, padx=10, pady=10)
                        copy_button = Button(root, text="Copy", command=lambda:copy_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to copy files
                        copy_button.grid(row=8, column=1, padx=10, pady=10)
            elif selected_csv_file == "sftptasks.csv":
                        download_button = Button(root, text="Download", command=lambda:download_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to download files
                        download_button.grid(row=8, column=0, padx=10, pady=10)
                        upload_button = Button(root, text="Upload", command=lambda:upload_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to upload files
                        upload_button.grid(row=8, column=1, padx=10, pady=10)

    except FileNotFoundError:
        root.log_output(f"Error: {selected_csv_file} not found.")

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
        remove_task_result = Label(root, text="CSV not displayed.", bg='white', fg="#ba0e0e", font=("Arial", 14))
        remove_task_result.grid(row=3, column=0, columnspan=5, padx=10, pady=10)  

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
    # Function to add a task to the queue
    root.log_output("Execute functionality not implemented.")


def open_source_file(root):
    # Function to open the source file path
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select a file")
    source_file_result = Label(root, text=root.filename)
    source_file_result.grid(row=6, column=0, padx=10, pady=10)

def open_destination_folder(root):
    # Function to open the destination folder path
    root.filename = filedialog.askdirectory(initialdir="/", title="Select destination folder")
    destination_file_result = Label(root, text=root.filename)
    destination_file_result.grid(row=7, column=0, padx=10, pady=10)

def move_file(root):
    # Function to move a file
    root.log_output("Move functionality not implemented.")


def copy_file(root):
    # Function to copy a file
    root.log_output("Copy functionality not implemented.")


def download_file(root):
    # Function to download a file
    root.log_output("Download functionality not implemented.")


def upload_file(root):
    # Function to upload a file
    root.log_output("Upload functionality not implemented.")
