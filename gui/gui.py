from tkinter import *
from button_functions import show_csv, remove_task_btn, clear_csv_btn, execute_csv_btn, open_source_file, open_destination_folder
from task_manager import create_task, remove_task, check_sftp

root = Tk() # Instantiate the main window

def start_gui():
    root.geometry("850x600") # Set the size of the window
    root.title("File Transfer Queue GUI") # Set the title of the window

    logo = PhotoImage(file='images/leaderbank_logo.png') # Load logo image
    # photo = PhotoImage(file='images/red_stars.png') # Load red stars image

    root.iconphoto(True, logo) # Set the icon of the window
    root.configure(bg='white') # Set the background color of the window

    header = Label(root, text="File Transfer Queue", font=("Arial", 24), bg='white', fg="#ba0e0e", padx=10, pady=10, compound=RIGHT) # Create a label with the title

    #header.pack(pady=20) # Add some padding and place the label in the window
    #header.place(x=0, y=0) # For absolute positioning
    header.grid(row=0, column=0, rowspan=2, columnspan=2, padx=10, pady=10) # Use grid layout for the label 

    selected_csv = StringVar() # Create a StringVar to hold the selected CSV file
    selected_csv.set("Select csv") # Set the default value for the dropdown menu
    show_csv(root, "localtasks.csv") # Show the content of the default CSV file
    csv_dropdown = OptionMenu(root, selected_csv, "localtasks.csv", "sftptasks.csv", command=lambda value:show_csv(root, value)) # Create a dropdown menu for selecting CSV files
    csv_dropdown.grid(row=2, column=0, padx=10, pady=10) # Place the dropdown in the grid layout 

    # selected_command = StringVar() # Create a StringVar to hold the selected command
    # selected_command.set("Selected Command") # Set the default value for the dropdown menu
    remove_button = Button(root, command=lambda:remove_task_btn(root), text="Remove", bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to remove tasks
    remove_button.grid(row=2, column=1, padx=10, pady=10) # Place the button in the grid layout

    clear_button = Button(root, command=lambda:clear_csv_btn(root), text="Clear", bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to clear tasks
    clear_button.grid(row=2, column=2, padx=10, pady=10) # Place the button in the grid layout

    execute_csv_button = Button(root, command=lambda:execute_csv_btn(root), text="Execute .csv", bg="#ba0e0e", fg="white", font=("Arial", 14), padx=10) # Create a button to add tasks ro selected csv
    execute_csv_button.grid(row=2, column=4, padx=10, pady=10) # Place the button in the grid layout

    source_button = Button(root, text = "Select Source File", command=lambda:open_source_file(root))
    source_button.grid(row=6, column=3, padx=10, pady=10) # Place the button in the grid layout

    destination_button = Button(root, text = "Select Destination Location", command=lambda:open_destination_folder(root))
    destination_button.grid(row=7, column=3, padx=10, pady=10) # Place the button in the grid layout

    root.mainloop() # Place window on screen and wait for user interaction
