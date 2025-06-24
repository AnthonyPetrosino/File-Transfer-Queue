from tkinter import *
from tkinter.ttk import Treeview
from tkinter import filedialog
from task_manager import create_task, remove_task, check_sftp

def show_csv(root, selected_file):
    # Function to display the selected CSV file
    try:
        with open(selected_file, 'r') as file: 
            content = file.read()

            # Clear previous content
            for widget in root.grid_slaves():
                if isinstance(widget, Label) and widget.grid_info()['row'] == 3:
                    widget.destroy()

            csv_tree = Treeview(root)
            csv_tree['columns'] = ('ID', 'Timestamp', 'Command') # Define the columns
            csv_tree.column("ID", width=50, anchor=W)
            csv_tree.column("Timestamp", width=150, anchor=W)
            csv_tree.column("Command", width=400, anchor=CENTER)

            # Insert the content into the Treeview
            csv_tree.insert(parent="", index="end", values=("ID", "Timestamp", "Command")) # Add a header row

            # Populate the Treeview with the csv content
            for i, line in enumerate(content.splitlines()):
                if i == 0:
                    continue  # Skip csv header
                try:
                    timestamp, command = line.split(",", 1)
                    csv_tree.insert("", "end", text=str(i), values=(i, timestamp.strip(), command.strip()))
                except ValueError:
                    continue

            csv_tree.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

            if selected_file == "localtasks.csv":
                        move_button = Button(root, text="Move", command=lambda:move_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to move files
                        move_button.grid(row=8, column=0, padx=10, pady=10)
                        copy_button = Button(root, text="Copy", command=lambda:copy_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to copy files
                        copy_button.grid(row=8, column=1, padx=10, pady=10)
            elif selected_file == "sftptasks.csv":
                        download_button = Button(root, text="Download", command=lambda:download_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to download files
                        download_button.grid(row=8, column=0, padx=10, pady=10)
                        upload_button = Button(root, text="Upload", command=lambda:upload_file(root), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to upload files
                        upload_button.grid(row=8, column=1, padx=10, pady=10)

    except FileNotFoundError:
        error_label = Label(root, text=f"Error: {selected_file} not found.", bg='white', fg="#ba0e0e", font=("Arial", 14))
        error_label.grid(row=3, column=0, columnspan=5, padx=10, pady=10) # Place the label in the grid layout

def remove_task_btn(root):
    # Function to remove a task from the queue
    remove_task_result = Label(root, text="Remove functionality not implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    remove_task_result.grid(row=3, column=0, padx=10, pady=10) # Place the label in the grid layout
    
    # remove_task(task_num, filename)

def clear_csv_btn(root):
    # Function to clear tasks in csv
    clear_csv_result = Label(root, text="Clear Functionality Not Implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    clear_csv_result.grid(row=3, column=0, padx=10, pady=10) # Place the label in the grid layout

def execute_csv_btn(root):
    # Function to add a task to the queue
    execute_csv_result = Label(root, text="Execute Functionality Not Implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    execute_csv_result.grid(row=3, column=0, padx=10, pady=10) # Place the label in the grid layout

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
    move_file_result = Label(root, text="Move functionality not implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    move_file_result.grid(row=3, column=4, padx=10, pady=10) # Place the label in the grid layout

def copy_file(root):
    # Function to copy a file
    copy_file_result = Label(root, text="Copy functionality not implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    copy_file_result.grid(row=3, column=0, padx=10, pady=10) # Place the label in the grid layout

def download_file(root):
    # Function to download a file
    download_file_result = Label(root, text="Download functionality not implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    download_file_result.grid(row=3, column=0, padx=10, pady=10) # Place the label in the grid layout

def upload_file(root):
    # Function to upload a file
    upload_file_result = Label(root, text="Upload functionality not implemented", bg='white', fg="#ba0e0e", font=("Arial", 14))
    upload_file_result.grid(row=3, column=0, padx=10, pady=10) # Place the label in the grid layout