from tkinter import *


def button_clicked():
    print('I got clicked')
    data = input.get()
    print(data)
    my_label.config(text=f' Hi {data.title()} ')


window = Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.config(text='What\'s Your Name')
my_label.grid(column=0, row=0)

# Button
button = Button(text='Click Me!!', command=button_clicked)
button.grid(column=1, row=2)

# Button 2
button_2 = Button(text='Click Me As Well')
button_2.grid(column=2, row=2)

# Entry
input = Entry()
input.grid(column=0, row=2)








window.mainloop()