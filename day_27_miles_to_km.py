from tkinter import *


def button_clicked():
    print('I got clicked')
    data = input.get()
    print(data)


window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=150)

# Label
my_label = Label(text='Miles')
my_label.grid(column=3, row=1)


#Entries
entry = Entry(width=10)
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
entry.grid(column=2, row=1)


def miles_to_km():
    entry_str = entry.get()
    miles = int(entry_str) * 1.60934
    x = (round(miles, 1))
    input.delete(0, END)
    input.insert(END, string=x)

# Text
my_label_2 = Label(text='Miles')
my_label_2.config(text='is equal to')
my_label_2.grid(column=1, row=2)

# Text
my_label_4 = Label(text='Miles')
my_label_4.config(text='Km')
my_label_4.grid(column=3, row=2)

# Button
button = Button(text='Calculate', command=miles_to_km)
button.grid(column=2, row=3)

# Entry
input = Entry(width=10)
input.grid(column=2, row=2)
input.insert(END, string='0')

window.mainloop()
