
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hi Python", "Hi World")

B = Tkinter.Button(top, text ="Book", command = helloCallBack)

B.pack()
top.mainloop()

