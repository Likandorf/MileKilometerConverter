from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=25, pady=25)


def calculate():
    miles = float(entry.get())
    km = round(miles * 1.60934, 1)
    label3.config(text=km)


entry = Entry(width=10)
entry.insert(END, string="0")
print(entry.get())
entry.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()
