
from Tkinter import Tk
import time
while(True):
	root = Tk()
	root.withdraw()
	try:
		number = root.clipboard_get()
    except:
		print "Caught it"
		number = 0
	if(number == '11'):
		r = Tk()
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append('Hello I am a hacker')
		r.mainloop()
	root.destroy()

	
	
	
