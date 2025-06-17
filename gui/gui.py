from tkinter import *

def create_gui():
    window = Tk()  # Instantiate the main window
    window.geometry("800x500")  # Set the size of the window
    window.title("FTQ GUI")  # Set the title of the window

    logo = PhotoImage(file='images//leaderbank_logo.png')  # Load the logo image
    photo = PhotoImage(file='images//red_stars.png')  # Load red stars image

    window.iconphoto(True, logo)  # Set the icon of the window
    window.configure(bg='white')  # Set the background color of the window

    label = Label(window, text="File Transfer Queue", font=("Arial", 24), bg='grey', fg="#ba0e0e", padx=10, pady=10, image=photo, compound=RIGHT)  # Create a label with the title
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)  # Use grid layout for the label

    start_button = Button(window, text="Start Transfer", command=lambda: print("Starting task scheduler..."), bg='green', fg='white', padx=20, pady=10)
    start_button.grid(row=1, column=0, padx=10, pady=10)  # Place the button in the window

    window.mainloop()  # Place window on screen and wait for user interaction

create_gui()
