from tkinter import *

class Email_slicer:
    
    def __init__(self):
        
        win = Tk()
        win.title("Email Slicer")
        win.geometry("300x200")
        
        l1 = Label(win,text="Enter your email id :")
        l1.place(x=10,y=20)
        
        self.t1 = StringVar()        
        e1 = Entry(win,textvariable = self.t1,width=25)
        e1.place(x=125,y=20)
        
        l2 = Label(win,text = "User name :")
        l2.place(x=10,y=50)
        self.l21 = Label(win,text = " ")
        self.l21.place(x=125,y=50)
        
        l3 = Label(win,text = "Domain name :")
        l3.place(x=10,y=80)
        self.l31 = Label(win,text = " ")
        self.l31.place(x=125,y=80)
        
        b1 = Button(win,text="Split",width=10,command = lambda : self.slicer(self.t1.get()))
        b1.place(x=110,y=120)
        
        win.mainloop()
    
    def slicer(self,email):
        
        l1 = email.split("@")
        self.l21['text'] = l1[0]
        self.l31['text'] = l1[1]
    
        
        
        
Email_slicer()
