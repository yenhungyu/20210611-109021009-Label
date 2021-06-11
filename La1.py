from tkinter import *
OP= 0
Y=0
def setText(num):
    if int(lab["text"]) != 0 :
        lab["text"] = lab["text"] + num
    else:
        lab["text"] = num

def OPset(OPY):
    global OP
    global Y
    Y= int(lab["text"])
    OP= OPY

def com():
    Y2= int(lab["text"])
    global OP
    if OP == 1:
        lab["text"] = Y+Y2
    elif OP == 2:
        lab["text"] = Y- Y2
    elif OP == 3:
        lab["text"] = Y * Y2
    elif OP == 4:
        lab["text"] = Y/Y2

window = Tk()
window.title= "0611 class2 Digital keyboard"
window.geometry("300x400+200+100")
window.rowconfigure(1 , weight= 1)#調整按鈕大小倍率
window.rowconfigure(2 , weight= 1)
window.rowconfigure(3 , weight= 1)
window.rowconfigure(4 , weight= 1)
window.columnconfigure(0 , weight= 1)
window.columnconfigure(1 , weight= 1)
window.columnconfigure(2 , weight= 1)
window.columnconfigure(3 , weight= 1)
lab = Label(window,text= "0",
                    justify="right",
                    anchor="c",#文字的位置
                    font=("Monaco",26,"bold"),
                    background="#ccddff",
                    foreground="#000000")
lab.grid(row=0, column=0 , columnspan=3, sticky=EW)

But1= Button(window, text="7" , font=("Monaco",36,"bold"), command=lambda:setText("7"))#lambda匿名函式
But1.grid(row= 1 , column= 0 , sticky=NSEW)#grid照座標擺放位置
But2= Button(window, text="8", font=("Monaco",36,"bold"), command=lambda:setText("8"))
But2.grid(row= 1 , column= 1 , sticky=NSEW)
But3= Button(window, text="9", font=("Monaco",36,"bold"), command=lambda:setText("9"))
But3.grid(row= 1 , column= 2 , sticky=NSEW)
Butx= Button(window, text="x", font=("Monaco",36,"bold"), command=lambda:OPset("x"))
Butx.grid(row= 1 , column= 3 , sticky=NSEW)

But4= Button(window, text="4" , font=("Monaco",36,"bold"), command=lambda:setText("4"))#lambda匿名函式
But4.grid(row= 2 , column= 0 , sticky=NSEW)#grid照座標擺放位置
But5= Button(window, text="5", font=("Monaco",36,"bold"), command=lambda:setText("5"))
But5.grid(row= 2 , column= 1 , sticky=NSEW)
But6= Button(window, text="6", font=("Monaco",36,"bold"), command=lambda:setText("6"))
But6.grid(row= 2 , column= 2 , sticky=NSEW)
Buttr= Button(window, text="/", font=("Monaco",36,"bold"), command=lambda:OPset("/"))
Buttr.grid(row= 2 , column= 3 , sticky=NSEW)

But7= Button(window, text="1" , font=("Monaco",36,"bold"), command=lambda:setText("1"))#lambda匿名函式
But7.grid(row= 3 , column= 0 , sticky=NSEW)#grid照座標擺放位置
But8= Button(window, text="2", font=("Monaco",36,"bold"), command=lambda:setText("2"))
But8.grid(row= 3 , column= 1 , sticky=NSEW)
But9= Button(window, text="3", font=("Monaco",36,"bold") , command=lambda:setText("3"))
But9.grid(row= 3 , column= 2 , sticky=NSEW)
Butch= Button(window, text="-", font=("Monaco",36,"bold") , command=lambda:OPset("-"))
Butch.grid(row= 3 , column= 3 , sticky=NSEW)

But10= Button(window, text="." , font=("Monaco",36,"bold"), command=lambda:setText("."))#lambda匿名函式
But10.grid(row= 4 , column= 0 , sticky=NSEW)#grid照座標擺放位置
But11= Button(window, text="0", font=("Monaco",36,"bold"), command=lambda:setText("0"))
But11.grid(row= 4 , column= 1 , sticky=NSEW)
But12= Button(window, text="=", font=("Monaco",36,"bold"), command=lambda:setText("="))
But12.grid(row= 4 , column= 2 , sticky=NSEW)
But12pl= Button(window, text="+", font=("Monaco",36,"bold"), command=lambda:OPset("+"))
But12pl.grid(row= 4 , column= 3 , sticky=NSEW)

window.mainloop()