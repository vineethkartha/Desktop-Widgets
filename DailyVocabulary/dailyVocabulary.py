from gi.repository import Gtk, GObject,Gdk


CSScool = """
GtkWindow {
	background: #00FF00;
    opacity:0.4;
}
GtkHeaderBar{
	background: #00FF00;
}
"""


class MyWidget(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self,title="Daily Words")
		self.resize(300,200)
		self.set_icon_from_file('/media/E/my_works/desktopWidgets/DailyVocabulary/pic/vocab-icon.jpg')
		self.set_skip_taskbar_hint(False)
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		self.label=Gtk.Label("New Word")
		self.box.pack_start(self.label,True,True,0)
		
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("Daily Words")
		self.set_titlebar(self.header)
	
		self.connect("delete-event", Gtk.main_quit)
		self.connect("button_press_event", self.button_press_event)
		
		self.cssprovider = Gtk.CssProvider()
		screen = Gdk.Screen.get_default()
		sc = Gtk.StyleContext()
		sc.add_provider_for_screen(screen, self.cssprovider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	
		
	def button_press_event(self,widget,event):
		if(event.button==3):
			print"right click"
		return True
win = MyWidget()
win.show_all()
Gtk.main()


