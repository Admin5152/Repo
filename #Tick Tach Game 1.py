#Tick Tach Game 1

#open window
from tkinter import *
from tkinter import messagebox

def ButtonClick(button):
    global x_o, flag
    button['bg'] = '#2ec4b6'
    if button['text'] == '' and x_o == True:
        button['text'] = 'x'
        x_o = False
        CheckForwin()
        flag = flag+1
    elif button['text'] == '' and x_o == False:
        button['text'] = 'o'
        x_o = True 
        CheckForwin
        flag = flag+1
    else:
        messagebox.showinfo('Tick Tack', 'PLayer has already enterd')


"""

1 2 3
4 5 6
7 8 9
1 5 9
3 5 7
1 4 7
2 5 8
3 6 9
"""

def CheckForwin():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    if button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x' or button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x' or button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x' or button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x' or button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x' or button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x' or button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x' or button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x':
        messagebox.showinfo('X wins!') 
    elif button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o' or button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == 'o' or button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o' or button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o' or button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o' or button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o' or button3['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o':
        messagebox.showinfo('O wins!') 
    elif flag ==8:
        messagebox.showinfo('its a tie')

    












main = Tk()
main.title('Tick Tack')

x_o = True
flag = 0


#Button
button1 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3, command=lambda: ButtonClick(button1))
button1.grid(row=0,column=0)

button2 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3, command=lambda: ButtonClick(button2))
button2.grid(row=0,column=1)

button3 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button3))
button3.grid(row=0,column=2)


button4 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button4))
button4.grid(row=1,column=0)

button5 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button5))
button5.grid(row=1,column=1)

button6 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button6))
button6.grid(row=1,column=2)


button7 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button7))
button7.grid(row=2,column=0)

button8 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button8))
button8.grid(row=2,column=1)

button9 = Button(main,text='',font=('arial',60,'bold'),bg='#ffb5a7',fg='white',width=3,  command=lambda: ButtonClick(button9))
button9.grid(row=2,column=2)


main.mainloop()