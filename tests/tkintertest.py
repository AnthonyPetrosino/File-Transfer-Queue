from tkinter import *

window = Tk() # Instantiate the main window
window.geometry("750x500") # Set the size of the window
window.title("FTQ GUI") # Set the title of the window

logo = PhotoImage(file='leaderbank_logo.png') # Load the logo image
photo = PhotoImage(file='red_stars.png') # Load red stars image

window.iconphoto(True, logo) # Set the icon of the window
window.configure(bg='white') # Set the background color of the window

label = Label(window, text="File Transfer Queue", font=("Arial", 24), bg='white', fg="#ba0e0e", padx=10, pady=10, image=photo, compound=RIGHT) # Create a label with the title
#label.pack(pady=20) # Add some padding and place the label in the window
#label.place(x=0, y=0) # For absolute positioning
label.grid(row=0, column=0, columnspan=2, padx=10, pady=10) # Use grid layout for the label

window.mainloop() # Place window on screen and wait for user interaction
