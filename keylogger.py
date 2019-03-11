from Tkinter import *

class keyLog():
	def __init__(self,root):
		self.logTxt=open("logsKeys.txt",'a+')
		self.root=root
		self.root.title("KeyLogger")
		self.root.config(background="black")
		self.labelTitle=Label(root,text="KeyLogger V.4", background="black", fg="green") #able to use shortned versions of words ; bg
		self.labelTitle.grid(row=0, column=0)
		self.textLog=Text(root, state='normal', height=11,width=50, bg="black",foreground="red", highlightthickness=0)
		self.textLog.grid(row=1,column=0)
		self.logs=Text(root,state="normal",height=11,width=50,bg="black",fg="yellow",highlightthickness=0)
		self.logs.grid(row=3,column=0)

		def keyStroke(event):
			print("Key ",event.char, " Repr ",repr(event.char))
			self.logs.insert(END, repr(event.char),"\n")
			self.logTxt.write(repr(event.char))


		self.textLog.bind('<Key>',keyStroke)

if __name__=="__main__":
	root=Tk()
	root.resizable(0,0)
	keylog=keyLog(root)
	root.mainloop()
