from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def Handle_keypress(event):
    print(event.char)

window.bind("<Key>", Handle_keypress)

def HandleClick(event):
    print("The button was clicked.")

btn = Button(text = "Click Me!")
btn.pack()
btn.bind("<Button-1>", HandleClick)

window.mainloop()