from tkinter import *
import webbrowser

class Map_Search:
    
    def __init__(self):
        
        win = Tk()
        win.title("Map Search")
        win.geometry("300x150")
        
        Label(win,text = "Enter the address").place(x=90,y=10)
        
        self.addr = StringVar()
        entr1 = Entry(win,textvariable=self.addr,width=40)
        entr1.place(x=25,y=40)
        
        button = Button(win,text="Search",command = self.map)
        button.place(x=120,y=80)
        
        win.mainloop()
        
    def map(self):
        webbrowser.open("https://www.google.co.in/maps/place/"+self.addr.get())
        
Map_Search()
