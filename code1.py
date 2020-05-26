from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")#cget is used to find text from button
    print(text)

    if text=='=':
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            try:
                value=eval(screen.get()) #eval will evaluate the string value
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        screen.update()
    elif text=='c':
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root=Tk()

root.geometry('666x500')

root.title('My Calculator')

scvalue = StringVar()
scvalue.set("")

screen=Entry(root,textvar=scvalue,font='lucida 40 bold')
screen.pack(fill='x',padx=9,pady=9)

frame1=Frame(root,bg='black')
b=Button(frame1,text="9",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="8",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="7",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg='black')
b=Button(frame1,text="6",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="5",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="4",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg='black')
b=Button(frame1,text="3",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="2",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="1",font='lucida 30 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg='black')
b=Button(frame1,text="0",font='lucida 31 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="+",font='lucida 31 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="-",font='lucida 31 bold')
b.pack(side='left',padx=9,pady=11)
b.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg='black')
b=Button(frame1,text="*",font='lucida 31 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="/",font='lucida 31 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="%",font='lucida 31 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)
frame1.pack()

frame1=Frame(root,bg='black')
b=Button(frame1,text="=",font='lucida 32 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text="c",font='lucida 32 bold')
b.pack(side='left',padx=9,pady=5)
b.bind("<Button-1>",click)

b=Button(frame1,text=".",font='lucida 32 bold')
b.pack(side='left',padx=9,pady=9)
b.bind("<Button-1>",click)
frame1.pack()

root.mainloop()