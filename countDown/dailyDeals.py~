"""
This is a Widget to display a comic strip from the website www.arcamax.com
"""
from gi.repository import Gtk, GObject,Gdk
from bs4 import BeautifulSoup
import requests
import urllib
import os
import time

today=time.strftime("%Y/%m/%d/");
mainURL="http://www.uclick.com/client/nydn/bod/"


class ComicStrip(Gtk.Window):
	"""
	This is the ComicStrip class of the widget, the window on which the Comic appears
	
	
	"""
	def __init__(self):
		self.comicDate=time.strftime("%Y/%m/%d/");
		self.day=int(time.strftime("%d"))
		self.year=int(time.strftime("%Y"))
		self.month=int(time.strftime("%m"))
		
		self.comicurl=mainURL
		
		Gtk.Window.__init__(self,title="Comic Strip")
		self.resize(300,200)
		self.connect("delete-event", Gtk.main_quit)
		self.set_skip_taskbar_hint(True)
		
		self.move(1100,200)
		
		self.loader = Gtk.Spinner()
		
		
		self.loader.start()
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("Comic for the Day")
		self.set_titlebar(self.header)
		
		self.navBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		Gtk.StyleContext.add_class(self.navBox.get_style_context(), "linked")
        
		
		
		self.nextBtn=Gtk.Button()
		self.nextBtn.add(Gtk.Arrow(Gtk.ArrowType.RIGHT,Gtk.ShadowType.NONE))
		
		self.prevBtn=Gtk.Button()
		self.prevBtn.add(Gtk.Arrow(Gtk.ArrowType.LEFT,Gtk.ShadowType.NONE))
		
		self.nextBtn.connect("clicked",self.nextComic)
		self.prevBtn.connect("clicked",self.prevComic)
		
		self.navBox.add(self.prevBtn)
		self.navBox.add(self.nextBtn)
		
		self.header.pack_start(self.navBox)
		
		self.setFlag=0;
		self.comic = Gtk.Image()
		#self.comic.set_from_file("/media/E/my_works/desktopWidgets/comicStrip/loading.gif")
		self.comicImg=""
		
		self.timeout_id = GObject.timeout_add(5000, self.loadComic,self.comicurl)
		print self.comicurl
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		self.box.pack_start(self.loader,True,True,0)
		self.box.pack_start(self.nextBtn,True,True,0)
		self.box.pack_start(self.comic,True,True,0)
		
		
	def loadComic(self,url):
		r=requests.get(url);
		print r.status_code
		data=r.text
		soup=BeautifulSoup(data)

		count=0;
		imgs=soup.findAll('img')
		if(imgs==[]):
			self.setFlag=0
			return True
		else:
			self.setFlag=1
			self.loader.stop()
		
		self.comicImg=imgs[0].get('src')
		urllib.urlretrieve(self.comicImg, "/home/kartha/.comic/"+os.path.basename(self.comicImg))
		if(self.setFlag==1):
			GObject.source_remove(self.timeout_id)
			self.comic.set_from_file("/home/kartha/.comic/"+os.path.basename(self.comicImg))
			#self.comic.set_from_file(os.path.basename(self.comicImg))
		return True
		
	def prevComic(self,some):
		self.day=self.day-1
		if(self.day<1):
			return
		self.comicDate=str(self.year)+"/"+str("%02d"%self.month)+"/"+str("%02d"%self.day);
		self.comicurl=mainURL+self.comicDate
		self.loadComic(self.comicurl)
		print self.comicurl
		
	def nextComic(self,event):
		self.day=self.day+1
		if(self.day>int(time.strftime("%d"))):
			return 
		
		self.comicDate=str(self.year)+"/"+str("%02d"%self.month)+"/"+str("%02d"%self.day);
		self.comicurl=mainURL+self.comicDate
		self.loadComic(self.comicurl)
		#print self.comicurl
win = ComicStrip()
win.show_all()
Gtk.main()
