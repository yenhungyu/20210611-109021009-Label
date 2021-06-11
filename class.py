from tkinter import *

flag = True

def setButTextCircle(Circle):
    global flag
    if Circle == 1:
        if flag:
            But1.config(text="0")
        else:
            But1.config(text="X")
        But1.config(state="disabled")
    elif Circle == 2:
        if flag:
            But2.config(text="0")
        else:
            But2.config(text="X")
        But2.config(state="disabled")    
    elif Circle == 3:
        if flag:
            But3.config(text="0")
        else:
            But3.config(text="X")
        But3.config(state="disabled")
    elif Circle == 4:
        if flag:
            But4.config(text="0")
        else:
            But4.config(text="X")
        But4.config(state="disabled")
    elif Circle == 5:
        if flag:
            But5.config(text="0")
        else:
            But5.config(text="X")
        But5.config(state="disabled")
    elif Circle == 6:
        if flag:
            But6.config(text="0")
        else:
            But6.config(text="X")
        But6.config(state="disabled")
    elif Circle == 7:
        if flag:
            But7.config(text="0")
        else:
            But7.config(text="X")
        But7.config(state="disabled")
    elif Circle == 8:
        if flag:
            But8.config(text="0")
        else:
            But8.config(text="X")
        But8.config(state="disabled")
    elif Circle == 9:
        if flag:
            But9.config(text="0")
        else:
            But9.config(text="X")
        But9.config(state="disabled")
    flag = not flag #重新設定flag

    if But1.cget("text") == But2.cget("text") and But1.cget("text") == But3.cget("text"):
        if But1.cget("text") =="0":
            print("winner player 1")
        elif But1.cget("text") == "X":
            print("winner player 2")
        elif But1.cget("text") == But2.cget("text") and But1.cget("text") == But3.cget("text"):
            print("peace")
    if  But4.cget("text") == But5.cget("text") and But4.cget("text") == But6.cget("text"):
        if But4.cget("text") =="0":
            print("winner player 1")
        elif But4.cget("text") == "X":
            print("winner player 2")
        elif But4.cget("text") != But5.cget("text") and But4.cget("text") != But6.cget("text"):
            print("peace")
    if  But7.cget("text") == But8.cget("text") and But7.cget("text") == But9.cget("text"):
        if But7.cget("text") =="0":
            print("winner player 1")
        elif But7.cget("text") == "X":
            print("winner player 2")            
        elif But7.cget("text") != But8.cget("text") and But7.cget("text") != But9.cget("text"):
            print("peace")
    if  But4.cget("text") == But1.cget("text") and But4.cget("text") == But7.cget("text"):
        if But4.cget("text") =="0":
            print("winner player 1")
        elif But4.cget("text") == "X":
            print("winner player 2")
        elif But4.cget("text") != But1.cget("text") and But4.cget("text") == But7.cget("text"):
            print("peace")
    if  But5.cget("text") == But2.cget("text") and But5.cget("text") == But8.cget("text"):
        if But5.cget("text") =="0":
            print("winner player 1")
        elif But5.cget("text") == "X":
            print("winner player 2")
        elif But5.cget("text") != But2.cget("text") and But5.cget("text") != But8.cget("text"):
            print("peace")
    if  But6.cget("text") == But3.cget("text") and But6.cget("text") == But9.cget("text"):
        if But6.cget("text") =="0":
            print("winner player 1")
        elif But6.cget("text") == "X":
            print("winner player 2")
        elif But6.cget("text") != But3.cget("text") and But6.cget("text") != But9.cget("text"):
            print("peace")
    if  But4.cget("text") == But2.cget("text") and But4.cget("text") == But9.cget("text"):
        if But4.cget("text") =="0":
            print("winner player 1")
        elif But4.cget("text") == "X":
            print("winner player 2")
        elif But4.cget("text") != But2.cget("text")and But4.cget("text") != But9.cget("text"):
            print("peace")
    if  But6.cget("text") == But2.cget("text") and But6.cget("text") == But7.cget("text"):
        if But6.cget("text") =="0":
            print("winner player 1")
        elif But6.cget("text") == "X":
            print("winner player 2")
        elif But6.cget("text") != But2.cget("text") and But6.cget("text") != But7.cget("text"):
            print("peace")
  
window = Tk()
window.title= "0611 class"
window.geometry("800x600+150+100")
window.rowconfigure(0 , weight= 1)#調整按鈕大小倍率
window.rowconfigure(1 , weight= 1)
window.rowconfigure(2 , weight= 1)
window.columnconfigure(0 , weight= 1)
window.columnconfigure(1 , weight= 1)
window.columnconfigure(2 , weight= 1)
window.size="120"

But1= Button(window, text="" , command=lambda:setButTextCircle(1))#lambda匿名函式
But1.grid(row= 1 , column= 0 , sticky=NSEW)#grid照座標擺放位置
But2= Button(window, text="" , command=lambda:setButTextCircle(2))
But2.grid(row= 1 , column= 1 , sticky=NSEW)
But3= Button(window, text="" , command=lambda:setButTextCircle(3))
But3.grid(row= 1 , column= 2 , sticky=NSEW)

But4= Button(window, text="" , command=lambda:setButTextCircle(4))
But4.grid(row= 2 , column= 0 , sticky=NSEW)
But5= Button(window, text=""  , command=lambda:setButTextCircle(5))
But5.grid(row= 2 , column= 1 , sticky=NSEW)
But6= Button(window, text="" ,command=lambda:setButTextCircle(6))
But6.grid(row= 2 , column= 2 , sticky=NSEW)

But7= Button(window, text="" ,command=lambda:setButTextCircle(7))
But7.grid(row= 0 , column= 0 , sticky=NSEW)
But8= Button(window, text=""  , command=lambda:setButTextCircle(8))
But8.grid(row= 0 , column= 1 , sticky=NSEW)
But9= Button(window, text="" , command=lambda:setButTextCircle(9))
But9.grid(row= 0 , column= 2 , sticky=NSEW)

window.mainloop()