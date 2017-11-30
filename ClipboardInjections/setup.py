

#setup.py
from distutils.core import setup
import py2exe
from Tkinter import Tk

setup(console=['Download.py'],
	options = {'tkinter':{
		'packages':['Tk']
		}
	}
)