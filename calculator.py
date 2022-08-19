from tkinter import *

cal_string = ''

app = Tk()
app.geometry('260x460')
app.title('Calculator')
app.config(background='Dark gray')

melabel = Label(app, text='Calculator')
melabel.pack(side=TOP)

textbox = StringVar()
metext = Entry(app, textvar=textbox)
metext.pack()

def clickBtn(operator):
    global cal_string
    cal_string += str(operator)
    textbox.set(cal_string)

def calculate():
    global cal_string
    cal_string = str(eval(cal_string))
    textbox.set(cal_string)

def clear():
    global cal_string
    cal_string = ''
    textbox.set(cal_string)

# First Row
btn_7 = Button(app, padx=14, pady=14, text='7', command=lambda:clickBtn(7))
btn_7.place(x=10, y=100)

btn_8 = Button(app, padx=14, pady=14, text='8', command=lambda:clickBtn(8))
btn_8.place(x=75, y=100)

btn_9 = Button(app, padx=14, pady=14, text='9', command=lambda:clickBtn(9))
btn_9.place(x=140, y=100)

btn_plus = Button(app, padx=14, pady=14, text='+', command=lambda:clickBtn('+'))
btn_plus.place(x=205, y=100)

# Second Row
btn_4 = Button(app, padx=14, pady=14, text='4', command=lambda:clickBtn(4))
btn_4.place(x=10, y=170)

btn_5 = Button(app, padx=14, pady=14, text='5', command=lambda:clickBtn(5))
btn_5.place(x=75, y=170)

btn_6 = Button(app, padx=14, pady=14, text='6', command=lambda:clickBtn(6))
btn_6.place(x=140, y=170)

btn_minus = Button(app, padx=15, pady=14, text='-', command=lambda:clickBtn('-'))
btn_minus.place(x=205, y=170)

# Third Row
btn_1 = Button(app, padx=14, pady=14, text='1', command=lambda:clickBtn(1))
btn_1.place(x=10, y=240)

btn_2 = Button(app, padx=14, pady=14, text='2', command=lambda:clickBtn(2))
btn_2.place(x=75, y=240)

btn_3 = Button(app, padx=14, pady=14, text='3', command=lambda:clickBtn(3))
btn_3.place(x=140, y=240)

btn_multiply = Button(app, padx=14, pady=14, text='*', command=lambda:clickBtn('*'))
btn_multiply.place(x=205, y=240)

# Fourth Row
btn_0 = Button(app, padx=14, pady=14, text='0', command=lambda:clickBtn(0))
btn_0.place(x=10, y=310)

btn_dot = Button(app, padx=16, pady=14, text='.', command=lambda:clickBtn('.'))
btn_dot.place(x=75, y=310)

btn_clear = Button(app, padx=10, pady=14, text='CE', command=clear)
btn_clear.place(x=140, y=310)

btn_divide = Button(app, padx=16, pady=14, text='/', command=lambda:clickBtn('/'))
btn_divide.place(x=205, y=310)

# Fifth Row
btn_equal = Button(app, padx=112, pady=14, text='=', command=calculate)
btn_equal.place(x=10, y=375)

app.mainloop()