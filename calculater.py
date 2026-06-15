from tkinter import *

def func(num):
    equation.set(equation.get()+num)

def sign(x):
    if equation.get()=="":
        return
    s=["-","+","/","*","."]
    if equation.get()[-1] in s:
        equation.set(equation.get()[:-1]+x)
    else:
        equation.set(equation.get()+x)

def equal():
    try:
        equation.set(eval(equation.get()))
    except:
        equation.set("Error")

def back():
    equation.set(equation.get()[:-1])

root=Tk()
root.title("calculater")

equation=StringVar()

lbl=Label(textvariable=equation,font=("times new roman",14,"bold"),fg="#0091FF",bg="#e4e3e3",padx=10,pady=10)
lbl.grid(columnspan=4,sticky="we")

btn1=Button(text="1",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("1")).grid(row=2,column=0)

btn2=Button(text="2",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("2")).grid(row=2,column=1)

btn3=Button(text="3",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("3")).grid(row=2,column=2)

btn4=Button(text="4",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("4")).grid(row=3,column=0)

btn5=Button(text="5",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("5")).grid(row=3,column=1)

btn6=Button(text="6",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("6")).grid(row=3,column=2)

btn7=Button(text="7",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("7")).grid(row=4,column=0)

btn8=Button(text="8",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("8")).grid(row=4,column=1)

btn9=Button(text="9",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("9")).grid(row=4,column=2)

btn0=Button(text="0",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:func("0")).grid(row=5,column=1)

btnequal=Button(text="=",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=equal).grid(row=5,column=2)

btnmul=Button(text="*",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:sign("*")).grid(row=2,column=3)

btndiv=Button(text="/",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:sign("/")).grid(row=3,column=3)

btnplus=Button(text="+",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:sign("+")).grid(row=4,column=3)

btnsub=Button(text="-",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:sign("-")).grid(row=5,column=3)

btnc=Button(text="c",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:equation.set("")).grid(row=1,column=2)

btnpried=Button(text=".",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:sign(".")).grid(row=5,column=0)

btnpower=Button(text="x²",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:equation.set(equation.get()+"**2")).grid(row=1,column=0)

btnsqrt=Button(text="√",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda:equation.set(equation.get()+"**0.5")).grid(row=1,column=1)

btnback=Button(text="⌫",font=("times new roman",14,"bold"),fg="#0091FF",width=5,height=2,command=lambda: back()).grid(row=1,column=3)

root.mainloop()
