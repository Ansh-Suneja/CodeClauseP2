import tkinter as tk
import math

calc=""
def addTO(symbol):
    global calc
    calc += str(symbol)
    ter.delete(1.0,"end")
    ter.insert(1.0,calc)
def evalu():
    global calc
    try:
        result = str(eval(calc))
        calc=""
        ter.delete(1.0,"end")
        ter.insert(1.0,result)

    except:
        clear()
        ter.insert(1.0,"error")
        pass    
    
def clear():
    global calc
    calc=""
    ter.delete(1.0,"end")

def deleter():
    global calc
    calc = calc[:-1]
    ter.delete(1.0, "end")
    ter.insert(1.0, calc)    

def trig(func):
    global calc
    try:
        result = str(eval("math." + func + "(math.radians(" + calc + "))"))
        calc = ""
        ter.delete(1.0, "end")
        ter.insert(1.0, result)
    except:
        clear()
        ter.insert(1.0, "error")
        pass    

root=tk.Tk()
root.geometry("500x475")
root.title(" Simple Calculator")
root.iconbitmap(r"calc.ico")

ter=tk.Text(root,height=5,width=16,font=("Arial",32))
ter.grid(columnspan=5)

bt1=tk.Button(root,text="1",command=lambda:addTO(1),width=5,font=("Arial",14))
bt1.grid(row=2,column=1)
bt2=tk.Button(root,text="2",command=lambda:addTO(2),width=5,font=("Arial",14))
bt2.grid(row=2,column=2)
bt3=tk.Button(root,text="3",command=lambda:addTO(3),width=5,font=("Arial",14))
bt3.grid(row=2,column=3)
bt4=tk.Button(root,text="4",command=lambda:addTO(4),width=5,font=("Arial",14))
bt4.grid(row=3,column=1)
bt5=tk.Button(root,text="5",command=lambda:addTO(5),width=5,font=("Arial",14))
bt5.grid(row=3,column=2)
bt6=tk.Button(root,text="6",command=lambda:addTO(6),width=5,font=("Arial",14))
bt6.grid(row=3,column=3)
bt7=tk.Button(root,text="7",command=lambda:addTO(7),width=5,font=("Arial",14))
bt7.grid(row=4,column=1)
bt8=tk.Button(root,text="8",command=lambda:addTO(8),width=5,font=("Arial",14))
bt8.grid(row=4,column=2)
bt9=tk.Button(root,text="9",command=lambda:addTO(9),width=5,font=("Arial",14))
bt9.grid(row=4,column=3)
bt0=tk.Button(root,text="0",command=lambda:addTO(0),width=5,font=("Arial",14))
bt0.grid(row=5,column=2)
btad=tk.Button(root,text="+",command=lambda:addTO("+"),width=5,font=("Arial",14))
btad.grid(row=2,column=5)
btsub=tk.Button(root,text="-",command=lambda:addTO("-"),width=5,font=("Arial",14))
btsub.grid(row=3,column=5)
btmul=tk.Button(root,text="*",command=lambda:addTO("*"),width=5,font=("Arial",14))
btmul.grid(row=4,column=5)
btdiv=tk.Button(root,text="/",command=lambda:addTO("/"),width=5,font=("Arial",14))
btdiv.grid(row=5,column=5)
btrem=tk.Button(root,text="%",command=lambda:addTO("%"),width=5,font=("Arial",14))
btrem.grid(row=6,column=5)
btop=tk.Button(root,text="(",command=lambda:addTO("("),width=5,font=("Arial",14))
btop.grid(row=5,column=1)
btcl=tk.Button(root,text=")",command=lambda:addTO(")"),width=5,font=("Arial",14))
btcl.grid(row=5,column=3)
btclr=tk.Button(root,text="C",command=clear,width=5,font=("Arial",14))
btclr.grid(row=6,column=6)
btequ=tk.Button(root,text="=",command=evalu,width=5,font=("Arial",14))
btequ.grid(row=5,column=5)
btdec=tk.Button(root,text=".",command=lambda:addTO("."),width=5,font=("Arial",14))
btdec.grid(row=1,column=5)

btdel = tk.Button(root, text="Del", command=deleter, width=5, font=("Arial", 14))
btdel.grid(row=6, column=5) 

btsin = tk.Button(root, text="sin", command=lambda: trig("sin"), width=5, font=("Arial", 14))
btsin.grid(row=2, column=4)  

btcos = tk.Button(root, text="cos", command=lambda: trig("cos"), width=5, font=("Arial", 14))
btcos.grid(row=3, column=4)  

bttan = tk.Button(root, text="tan", command=lambda: trig("tan"), width=5, font=("Arial", 14))
bttan.grid(row=4, column=4)  



root.mainloop()
