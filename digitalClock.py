from tkinter import Tk, Label

window = Tk()
window.title("Digital Clock")
window.configure(bg="steelblue")
label = Label(window, text="Digital Clock!", font=("Arial"))
label.pack(pady=100)
window.mainloop()
