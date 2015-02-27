from gi.repository import Gtk, GObject,Gdk


CSS = """
GtkWindow {
	background: #CCFF66;
    opacity:0.9;
}
GtkHeaderBar{
	background: #CCFF66;
}

"""
class MyWidget(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self,title="CPU Temperature")
		self.resize(200,100)
		self.T=""
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		t1 = Gtk.Image.new_from_file('/media/E/my_works/desktopWidgets/temperatureMonitor/pic/temp.png')
		self.box.pack_start(t1,True,True,0)
		
		self.label=Gtk.Label(self.T)
		self.box.pack_start(self.label,True,True,0)
		
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("CPU Temparature")
		self.set_titlebar(self.header)
	
		self.connect("delete-event", Gtk.main_quit)
		
		self.timeout_id = GObject.timeout_add(5000, self.readTemperature, None)
		
		self.readTemperature('s')
		cssprovider = Gtk.CssProvider()
		cssprovider.load_from_data(CSS)
		screen = Gdk.Screen.get_default()
		sc = Gtk.StyleContext()
		sc.add_provider_for_screen(screen, cssprovider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		
	def readTemperature(self,filename):
		content = open('/sys/class/thermal/thermal_zone0/temp')
		self.T=str(int(content.read())/1000)
		displayTemp=self.T+u'\u00B0'+"C"
		self.label.set_text(displayTemp)
		#print self.T
		return True
		
	def readBatStatus(self,filename):
		
		return True
win = MyWidget()
win.show_all()
Gtk.main()


