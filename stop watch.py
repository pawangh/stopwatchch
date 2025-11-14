import tkinter

screen= tkinter.Tk()
screen.geometry("400x400")
screen.title("67 clock")

s= tkinter.Entry(screen) 
m= tkinter.Entry(screen) 
h= tkinter.Entry(screen) 
s.grid(row=1,column=2)
m.grid(row=1,column=3)
h.grid(row=1,column=4)
screen.mainloop()