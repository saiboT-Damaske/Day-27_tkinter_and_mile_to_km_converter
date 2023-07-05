from tkinter import *

window = Tk()
window.title("Mile to km converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# empty label
label0 = Label(text="")
label0.grid(column=0, row=0)
# Text input

field = Entry(width=10)
field.grid(column=1, row=0)

# Miles label
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

# is equal to label
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

# km label
label_km = Label(text="Km")
label_km.grid(column=2, row=1)


# calculation function

def calculate_input():
    result = round(float(field.get()) * 1.609, 2)
    label_res.config(text=result)


# Calculate Button
button = Button(text="Calculate", command=calculate_input)
button.grid(column=1, row=2)

# result label
label_res = Label(text="0")
label_res.grid(column=1, row=1)

window.mainloop()
