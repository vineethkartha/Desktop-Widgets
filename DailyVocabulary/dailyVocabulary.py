from gi.repository import Gtk, GObject,Gdk
from bs4 import BeautifulSoup
import requests

url="http://wordsmith.org/words/today.html";
#r=requests.get(url);

#data=r.text
#soup=BeautifulSoup(data);

CSScool = """
GtkWindow {
	background: #FFFFFF;
    opacity:0.8;
}
GtkHeaderBar{
	background: #FFFFFF;
}
"""


class MyWidget(Gtk.Window):
	
	def __init__(self):
		self._flag=0
		
		Gtk.Window.__init__(self,title="Word for the day")
		self.resize(300,200)
		self.set_icon_from_file('/media/E/my_works/desktopWidgets/DailyVocabulary/pic/vocab-icon.jpg')
		self.set_skip_taskbar_hint(False)
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		self.label=Gtk.Label()
		self.box.pack_start(self.label,True,True,0)
		
		self._loader=Gtk.Spinner()
		self.box.pack_start(self._loader,True,True,0)
		self._loader.start()
		
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("Word for the day")
		self.set_titlebar(self.header)
		
		
		self.connect("delete-event", Gtk.main_quit)
		#self.connect("button_press_event", self.button_press_event)
		#self.newWord()
		
		self.cssprovider = Gtk.CssProvider()
		self.cssprovider.load_from_data(CSScool)
		screen = Gdk.Screen.get_default()
		sc = Gtk.StyleContext()
		sc.add_provider_for_screen(screen, self.cssprovider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		
		self.timeout_id = GObject.timeout_add(5000, self.newWord)
	
	def newWord(self):
		r=requests.get(url);
		data=r.text
		soup=BeautifulSoup(data);
		count=0;
		dispText=""
		for heading in soup.find_all('h3'):
			dispText=dispText+''.join(heading.contents)
		for divs in soup.find_all('div',style="margin-left: 20px;"):
			if(count>1):
				self._flag=1
				break;
			count=count+1
			dispText=dispText+divs.getText();
			self.label.set_text(dispText)
		if(self._flag==1):
			self._loader.stop()
			GObject.source_remove(self.timeout_id)
		return True
		
	def button_press_event(self,widget,event):
		if(event.button==3):
			print"right click"
		return True
		
		
win = MyWidget()
win.show_all()
Gtk.main()


