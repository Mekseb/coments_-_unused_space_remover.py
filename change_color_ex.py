from tkinter import *
from random import randint
import random

fen1 = Tk()
fen1.geometry("300x300")
can1=Canvas(fen1,width=200,height=200,bg="green")
can1.pack(side=LEFT)
x1, y1, x2, y2 = 10,190,190,10
coul = "black"
def drowline():

    global x1,x2,y1,y2,coul
    y2,y1 = y2+10, y1-10
    can1.create_line(x1, y1, x2, y2,width= 2 ,fill=coul)
    print(x1,x2,y1,y2)



def colorchange():
    changing_color=["red","blue","green","yellow"]

    for i in range(len(changing_color)):
        x = random.randint(0, len(changing_color) - 1)
        coul=changing_color[i]
        print(coul)
        can1.create_line(x1, y1, x2, y2, width=2, fill=changing_color[x])

        print(changing_color[x])
    drowline()

btn=Button(fen1,text = "click me!",command=drowline , font=( "arial",16))
btn.pack(padx=10,pady=10)

btn2= Button(fen1,text = "color-changer",command=colorchange, font=( "arial",16))
btn2.pack(side=LEFT)
fen1.mainloop()