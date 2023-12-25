from tkinter import Tk, Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.configure(bg="steelblue")
label = Label(window, text="Digital Clock!", font=("Arial"))
label.pack(pady=100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500,clock)
clock()
window.mainloop()
