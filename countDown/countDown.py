"""
This is a Widget to display A countDown
"""
from datetime import datetime
from gi.repository import Gtk, GObject,Gdk
import os
import time

class countDown(Gtk.Window):
	"""
	This is the CountDown class of the widget
	
	"""
	def __init__(self):
		
                self.orgTime=datetime(2015,5,13,10,0,0)
		self.remTime=0			

		Gtk.Window.__init__(self,title="Count Down")
		self.resize(200,100)
		self.connect("delete-event", Gtk.main_quit)
		self.set_skip_taskbar_hint(True)
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		self.label=Gtk.Label(self.remTime)
		self.box.pack_start(self.label,True,True,0)

		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(True)
		self.header.set_title("count down")
		self.set_titlebar(self.header)
		
		self.timeout_id = GObject.timeout_add(1000, self.calremTime)
		
	def calremTime(self):
                self.remTime=self.orgTime-datetime.utcnow()
                hours, remainder = divmod(self.remTime.seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.label.set_text(str(self.remTime.days)+"days and "+str(hours)+":"+str(minutes)+":"+str(seconds))
                return True
	
win = countDown()
win.show_all()
Gtk.main()
