'''.
This is a Widget to display a comic strip from the website www.arcamax.com
'''
from gi.repository import Gtk, GObject,Gdk
from bs4 import BeautifulSoup
import requests
import urllib
import os

url="http://www.arcamax.com/thefunnies/hiandlois/?morec=1";

class ComicStrip(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self,title="Comic Strip")
		self.resize(300,200)
		self.connect("delete-event", Gtk.main_quit)
		#self.set_icon_from_file()
		self.set_skip_taskbar_hint(True)
		
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("Comic for the Day")
		self.set_titlebar(self.header)
		
		self.setflag=0;
		self.comic = Gtk.Image()
		self.f1=""
		
		self.timeout_id = GObject.timeout_add(5000, self.loadComic)
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		
		self.box.pack_start(self.comic,True,True,0)
		self.comic.set_from_file("loading.gif")
		
	def loadComic(self):
		r=requests.get(url);
		data=r.text
		soup=BeautifulSoup(data)
		count=0;
		imgs=soup.findAll("img")
		if(imgs==[]):
			self.setflag=0
			return True
		else:
			self.setflag=1
		self.f1=imgs[0].get('src')
		urllib.urlretrieve(self.f1, os.path.basename(self.f1))
		if(self.setflag==1):
			GObject.source_remove(self.timeout_id)
			self.comic.set_from_file(os.path.basename(self.f1))
		return True
		
win = ComicStrip()
win.show_all()
Gtk.main()
