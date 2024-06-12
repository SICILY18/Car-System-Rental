import tkinter as tk
from tkinter import Canvas, NW, Button, Label

def open_new_record_page():
    new_window = tk.Toplevel(root)
    new_window.title("New Record Page")
    new_window.geometry("400x300")
    
    # Add widgets to the new window
    label = tk.Label(new_window, text="This is the New Record page")
    label.pack()

root = tk.Tk()
root.title("Car System")

canvas = Canvas(root, width=3900, height=2500)
canvas.pack()
img = tk.PhotoImage(file="bg.jpg")
canvas.create_image(0, 0, anchor=NW, image=img)

canvas.create_text(1000, 40, text="Gian Sports Car System", font=("Helvetica", 36), fill="white")

button1 = Button(root, text="New Record", fg="black", bg="#4CCD99", font="Helvetica", relief="raised", command=open_new_record_page) 
button_window1 = canvas.create_window(800, 100, anchor=tk.CENTER, window=button1)

button2 = Button(root, text="Show Cars", fg="black", relief="raised", borderwidth=3, bg="#4CCD99")  
button_window2 = canvas.create_window(900, 100, anchor=tk.CENTER, window=button2)

button3 = Button(root, text="Edit", fg="black", relief="raised", borderwidth=3, bg="#4CCD99")  
button_window3 = canvas.create_window(1000, 100, anchor=tk.CENTER, window=button3)

button4 = Button(root, text="Update", fg="black", relief="raised", borderwidth=3, bg="#4CCD99")  
button_window4 = canvas.create_window(1100, 100, anchor=tk.CENTER, window=button4)

button5 = Button(root, text="Delete", fg="black", relief="raised", borderwidth=3, bg="#4CCD99")  
button_window5 = canvas.create_window(1200, 100, anchor=tk.CENTER, window=button5)

button6 = Button(root, text="Record", fg="black", relief="raised", borderwidth=3, bg="#4CCD99")  
button_window6 = canvas.create_window(1300, 100, anchor=tk.CENTER, window=button6)

root.mainloop()
