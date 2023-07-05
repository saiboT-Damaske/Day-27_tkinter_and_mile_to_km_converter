
import tkinter

window = tkinter.Tk()
window.title("first GUI")
window.minsize(width=500, height=400)
window.config(padx=100, pady= 100)

# label
label1 = tkinter.Label(text="me label", font=("roman", 24, "bold"))
label1["text"] = "new text"
label1.config(text="oh yeah")
# label1.place(x=200, y=80)
label1.grid(column=0, row=0)
label1.config(padx=40, pady=60)


def clicked():
    label1.config(text=input.get())


# Button

button = tkinter.Button(text="click me", command=clicked)
#button.pack()
button.grid(column=1, row=1)

button2 = tkinter.Button(text="click me", command=clicked)
button2.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=15)
#input.pack()
input.grid(column=3, row=3)
print(input.get())



window.mainloop()
# Playground

def my_f(*args):
    summm = 0
    for n in args:
        summm += n
    print(summm)

my_f(1,2,3,4,5)
