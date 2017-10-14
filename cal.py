from tkinter import*

        
def buttonClick(input):
    text_input.set(text_input.get()+str(input))
    

def onButtonChangeSign():
    val = eval(text_input.get())
    val = -1*val;
    text_input.set(str(val))
    

def onButtonClear():
    val = text_input.get()
    val = val[:len(val)-1]
    text_input.set(val)
    
    
def onButtonClearAll():
    text_input.set("")
    

def onButtonEquals():
    text_input.set("{0:.6f}".format(eval(text_input.get())))
    

def validate(char, entry_value):
    if char in '0123456789.-+*/()':
        return True
    else:
        return False
    

window = Tk()
window.title("Calculator")
vcmd = (window.register(validate), '%S', '%P')
text_input = StringVar()
txtDisplay = Entry(window, font=('arial',20,'bold'), textvariable=text_input,
                   bd=10,insertwidth=4,bg="powder blue",
                   justify='right', validate = 'key', validatecommand = vcmd).grid(columnspan=4)



btn7=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="7",bg="powder blue", command=lambda:buttonClick(7)).grid(row=1,column=0)
btn8=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="8",bg="powder blue", command=lambda:buttonClick(8)).grid(row=1,column=1)
btn9=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="9",bg="powder blue", command=lambda:buttonClick(9)).grid(row=1,column=2)
btnAddition=Button(window,padx=41,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="+",bg="powder blue", command=lambda:buttonClick("+")).grid(row=1,column=3)

#==================================================================================================#
btn4=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="4",bg="powder blue", command=lambda:buttonClick(4)).grid(row=2,column=0)
btn5=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="5",bg="powder blue", command=lambda:buttonClick(5)).grid(row=2,column=1)
btn6=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="6",bg="powder blue", command=lambda:buttonClick(6)).grid(row=2,column=2)
btnSubtraction=Button(window,padx=45,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="-",bg="powder blue", command=lambda:buttonClick("-")).grid(row=2,column=3)

#===================================================================================================#
btn1=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="1",bg="powder blue", command=lambda:buttonClick(1)).grid(row=3,column=0)
btn2=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="2",bg="powder blue", command=lambda:buttonClick(2)).grid(row=3,column=1)
btn3=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="3",bg="powder blue", command=lambda:buttonClick(3)).grid(row=3,column=2)
btnMultiplication=Button(window,padx=45,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="*",bg="powder blue", command=lambda:buttonClick("*")).grid(row=3,column=3)
#===================================================================================================#
btn0=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="0",bg="powder blue", command=lambda:buttonClick(0)).grid(row=4,column=0)
btnDot=Button(window,padx=45,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text=".",bg="powder blue", command=lambda:buttonClick(".")).grid(row=4,column=1)
btnSign=Button(window,padx=35,pady=24,bd=4,fg="black",font=('arial',14,'bold'),
            text="+/-",bg="powder blue", command=onButtonChangeSign).grid(row=4,column=2)
btnDivision=Button(window,padx=45,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="/",bg="powder blue", command=lambda:buttonClick("/")).grid(row=4,column=3)
#===================================================================================================#
btnParenthLeft=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="(",bg="powder blue", command=lambda:buttonClick("(")).grid(row=4,column=0)
btnParenthRight=Button(window,padx=45,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text=")",bg="powder blue", command=lambda:buttonClick(")")).grid(row=4,column=1)
btnSquareRoot=Button(window,padx=35,pady=24,bd=4,fg="black",font=('arial',14,'bold'),
            text="sqrt",bg="powder blue", command=lambda:buttonClick("**0.5")).grid(row=4,column=2)
btnCubicRoot=Button(window,padx=25,pady=20,bd=4,fg="black",font=('arial',14,'bold'),
            text="qbrt",bg="powder blue", command=lambda:buttonClick("**(1/3)")).grid(row=4,column=3)
#===================================================================================================#
btnClear=Button(window,padx=40,pady=25,bd=4,fg="black",font=('arial',14,'bold'),
            text="C",bg="powder blue", command=onButtonClear).grid(row=5,column=0)
btnClearAll=Button(window,padx=35,pady=25,bd=4,fg="black",font=('arial',14,'bold'),
            text="CA",bg="powder blue", command=onButtonClearAll).grid(row=5,column=1)
btnEquals=Button(window,padx=40,pady=20,bd=4,fg="black",font=('arial',20,'bold'),
            text="=",bg="powder blue", command=onButtonEquals).grid(row=5,column=2)
btnPower=Button(window,padx=30,pady=25,bd=4,fg="black",font=('arial',14,'bold'),
            text="pow",bg="powder blue", command=lambda:buttonClick("**")).grid(row=5,column=3)

window.mainloop()
