import tkinter
import time

screen= tkinter.Tk()
screen.geometry("400x400")
screen.title("67 clock")

hours=tkinter.StringVar()
minutes=tkinter.StringVar()
seconds=tkinter.StringVar()

def stopwatch():
    hg=int(h.get())
    mg=int(m.get())
    sg=int(se.get())
    ts=hg*60*60+mg*60+sg
    while ts>0:
      ts-=1
      print(ts)
      time.sleep(1)
se= tkinter.Entry(screen,textvariable=seconds) 
m= tkinter.Entry(screen,textvariable=minutes) 
h= tkinter.Entry(screen,textvariable=hours) 
st= tkinter.Button(screen,text = "go",command=stopwatch) 
hla=tkinter.Label(screen,text="hours")

mla=tkinter.Label(screen,text="minutes")
sela=tkinter.Label(screen,text="seconds")

se.grid(row=1,column=4)
m.grid(row=1,column=3)
h.grid(row=1,column=2)
st.grid(row=1,column=5)
hla.grid(row=2,column=2)
mla.grid(row=2,column=3)
sela.grid(row=2,column=4)
screen.mainloop()