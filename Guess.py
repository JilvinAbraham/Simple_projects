import random
from tkinter import *
class Guess:
    
    
    
    def __init__(self):
        
        win = Tk()
        win.title("Guess")
        win.geometry("300x300")
        
        self.List1 = [i for i in range(1,101)]
        self.x = random.choice(self.List1)
#         print(self.x)
        self.count=3
        
        Label(win,text = "GUESS GAME").place(x=110,y=20)
        var = StringVar()
        label1 = Message(win,textvariable = var,width=180).place(x=60,y=50)
        var.set("Guess a number between (1-100) if it matches with the system's guess you WIN.")
        
        Label(win,text = "Enter your number below").place(x=80,y=120)
        self.v1 = IntVar()
        self.v1.set(" ")
        entry1 = Entry(win,textvariable=self.v1,width=10).place(x=118,y=150)
        l1 = Label(win,text = "Hint:").place(x=80,y=175)
        self.l2 = Label(win,text = " ")
        self.l2.place(x=120,y=175)
        
        b1 = Button(win,text="Check",command=self.guess)
        b1.place(x=130,y=200)
        
        b2 = Button(win,text="Resest",command=self.reset)
        b2.place(x=200,y=200)
        win.mainloop()
    
    def guess(self):
        
       
        if(self.v1.get()==self.x):
            self.l2["text"]="Right Guess You won"


        elif(self.v1.get()<self.x):
            self.l2["text"]="Number is greater"
        else:
            self.l2["text"]="Number is smaller"

        self.count-=1
        
        if(self.count<=0):
            self.l2["text"]="Chances over,Press Reset"
        
    def reset(self):
        
        self.x = random.choice(self.List1)
#         print(self.x)
        self.l2["text"]="Number is resetted"
        self.count=3

        
Guess()
