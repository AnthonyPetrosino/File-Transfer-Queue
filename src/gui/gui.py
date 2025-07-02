from tkinter import *
from .button_functions import show_csv, remove_task_btn, clear_csv_btn, execute_csv_btn, open_source_file, open_destination_folder, create_task_btn
import os

root = Tk() # Instantiate the main window

def start_gui():
    root.geometry("800x700") # Set the size of the window
    root.title("File Transfer Queue GUI") # Set the title of the window

    BASE_DIR = os.path.dirname(__file__)  # gets path to src/gui
    image_path = os.path.join(BASE_DIR, "images", "leaderbank_logo.png")
    logo = PhotoImage(file=image_path) 
    
    root.iconphoto(True, logo) # Set the icon of the window
    root.configure(bg='white') # Set the background color of the window

    header = Label(root, text="File Transfer Queue", font=("Arial", 24), bg='white', fg="#ba0e0e", padx=10, pady=10, compound=RIGHT) # Create a label with the title
    header.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=10) # Use grid layout for the label 

    selected_csv = StringVar() # Create a StringVar to hold the selected CSV file
    selected_csv.set("localtasks.csv") # Set the default value for the dropdown menu
    root.selected_csv = selected_csv
    show_csv(root, "localtasks.csv") # Show the content of the default CSV file
    csv_dropdown = OptionMenu(root, selected_csv, "localtasks.csv", "sftptasks.csv", command=lambda value:show_csv(root, value)) # Create a dropdown menu for selecting CSV files
    csv_dropdown.grid(row=2, column=0, padx=10, pady=10) # Place the dropdown in the grid layout 

    remove_button = Button(root, command=lambda:remove_task_btn(root, selected_csv.get()), text="Remove", bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to remove tasks
    remove_button.grid(row=2, column=1, padx=10, pady=10) # Place the button in the grid layout

    clear_button = Button(root, command=lambda:clear_csv_btn(root), text="Clear", bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to clear tasks
    clear_button.grid(row=2, column=2, padx=10, pady=10) # Place the button in the grid layout

    execute_csv_button = Button(root, command=lambda:execute_csv_btn(root), text="Execute .csv", bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to add tasks ro selected csv
    execute_csv_button.grid(row=2, column=3, padx=10, pady=10) # Place the button in the grid layout

    # Source Path
    root.source_entry = Entry(root, width=80, bd=2, relief="groove")
    root.source_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    source_button = Button(root, text = "Select Source File", command=lambda:open_source_file(root))
    source_button.grid(row=6, column=3, padx=10, pady=10) # Place the button in the grid layout

    # Destination Path
    root.destination_entry = Entry(root, width=80, bd=2, relief="groove")
    root.destination_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    destination_button = Button(root, text = "Select Destination Location", command=lambda:open_destination_folder(root))
    destination_button.grid(row=7, column=3, padx=10, pady=10) # Place the button in the grid layout

    # Store source and destination paths as attributes of root
    root.source_path = None
    root.destination_path = None

    # Store task type as an attribute of root
    root.task_type_var = StringVar()
    root.task_type_var.set("Move")

    add_task_button = Button(root, text="Add Task", command=lambda:create_task_btn(root, selected_csv.get()), bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to add task to selected csv
    add_task_button.grid(row=8, column=3, padx=10, pady=10)

    # Frame for the output box and its scrollbar
    output_frame = Frame(root)
    output_frame.grid(row=10, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    # Scrollbar
    scrollbar = Scrollbar(output_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Output Text box
    output_box = Text(output_frame, height=6, bg="white", fg="black", font=("Arial", 13), yscrollcommand=scrollbar.set, wrap=WORD)
    output_box.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=output_box.yview)

    # Log function
    def log_output(msg):
        output_box.config(state=NORMAL)
        output_box.insert(END, f"{msg}\n")
        output_box.see(END) 
        output_box.config(state=DISABLED)

    root.log_output = log_output

    root.mainloop() # Place window on screen and wait for user interaction
