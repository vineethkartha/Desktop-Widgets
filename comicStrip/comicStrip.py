"""
This is a Widget to display a comic strip from the website www.arcamax.com
"""
from gi.repository import Gtk, GObject,Gdk
from bs4 import BeautifulSoup
import requests
import urllib
import os

#url="http://www.arcamax.com/thefunnies/hiandlois/?morec=1";
url="http://www.uclick.com/client/nydn/bod/"
class ComicStrip(Gtk.Window):
	"""
	This is the ComicStrip class of the widget, the window on which the Comic appears
	
	
	"""
	def __init__(self):
		Gtk.Window.__init__(self,title="Comic Strip")
		self.resize(300,200)
		self.connect("delete-event", Gtk.main_quit)
		self.set_skip_taskbar_hint(True)
		
		self.move(1100,200)
		
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("Comic for the Day")
		self.set_titlebar(self.header)
		
		self.setFlag=0;
		self.comic = Gtk.Image()
		self.comicImg=""
		
		self.timeout_id = GObject.timeout_add(5000, self.loadComic)
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		
		self.box.pack_start(self.comic,True,True,0)
		self.comic.set_from_file("/media/E/my_works/desktopWidgets/comicStrip/loading.gif")
		
	def loadComic(self):
		r=requests.get(url);
		print r.status_code
		data=r.text
		soup=BeautifulSoup(data)

		count=0;
		imgs=soup.findAll('img')
		print imgs
		if(imgs==[]):
			self.setFlag=0
			return True
		else:
			self.setFlag=1
		
		self.comicImg=imgs[0].get('src')
		urllib.urlretrieve(self.comicImg, os.path.basename(self.comicImg))
		if(self.setFlag==1):
			GObject.source_remove(self.timeout_id)
			self.comic.set_from_file(os.path.basename(self.comicImg))
		return True
		
win = ComicStrip()
win.show_all()
Gtk.main()
