from tkinter import *
class ExpressionSolver:
    
    def __init__(self):
        win = Tk()
        
        win.title("Expression Solver")
        win.geometry("300x150")
        label1 = Label(win,text="Value of x:")
        label1.place(x=10,y=10)
        
        self.value = IntVar()
        entry1 = Entry(win,textvariable=self.value)
        entry1.place(x=150,y=10)
        
        label2 = Label(win,text="Enter Expression in x:")
        label2.place(x=10,y=50)
        
        self.expr=StringVar()
        entry2 = Entry(win,textvariable=self.expr)
        entry2.place(x=150,y=50)
        
        button = Button(win,text="Compute",command=self.express)
        button.place(x=10,y=100)
        
        label3 = Label(win,text="Answer :")
        label3.place(x=150,y=100)
        
        self.label4 = Label(win,text="0")
        self.label4.place(x=200,y=100)
        
        win.mainloop()
    
    def express(self):
        x = self.value.get()
        print("x",x)
        a = eval(self.expr.get())
        print("expr",self.expr.get())
        self.label4["text"]=str(a)
        
        
        
ExpressionSolver()
    
    
