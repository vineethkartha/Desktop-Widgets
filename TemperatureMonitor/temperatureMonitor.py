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

CSSmed = """
GtkWindow {
	background: #FF3300;
    opacity:0.7;
}
GtkHeaderBar{
	background: #FF3300;
}
"""
CSShot = """
GtkWindow {
	background: #FF0000;
    opacity:0.7;
}
GtkHeaderBar{
	background: #FF0000;
}
"""

class MyWidget(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self,title="CPU Temperature")
		self.resize(200,100)
		self.set_icon_from_file('/media/E/my_works/desktopWidgets/temperatureMonitor/pic/temp.png')
		self.set_skip_taskbar_hint(True)
		self.T=""
		
		self.box=Gtk.Box(spacing=2)
		self.add(self.box)
		
		self.t1 = Gtk.Image.new_from_file('/media/E/my_works/desktopWidgets/temperatureMonitor/pic/temp.png')
		self.box.pack_start(self.t1,True,True,0)
		
		self.label=Gtk.Label(self.T)
		self.box.pack_start(self.label,True,True,0)
		
		self.header=Gtk.HeaderBar()
		self.header.set_show_close_button(False)
		self.header.set_title("CPU Temparature")
		self.set_titlebar(self.header)
	
		self.connect("delete-event", Gtk.main_quit)
		self.connect("button_press_event", self.button_press_event)
		
		self.timeout_id = GObject.timeout_add(5000, self.readTemperature, None)
		
		
		self.cssprovider = Gtk.CssProvider()
		self.readTemperature('s')
		if(int(self.T)>60):
			self.cssprovider.load_from_data(CSShot)
		else:
			self.cssprovider.load_from_data(CSScool)
			
		screen = Gdk.Screen.get_default()
		sc = Gtk.StyleContext()
		sc.add_provider_for_screen(screen, self.cssprovider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		
	def readTemperature(self,filename):
		content = open('/sys/class/thermal/thermal_zone0/temp')
		self.T=str(int(content.read())/1000)
		displayTemp=self.T+u'\u00B0'+"C"
		self.label.set_text(displayTemp)
		if(int(self.T)<50):
			self.cssprovider.load_from_data(CSScool)
			self.t1.set_from_file('/media/E/my_works/desktopWidgets/temperatureMonitor/pic/cool.png')
		elif(int(self.T)<70):
			self.cssprovider.load_from_data(CSSmed)
			self.t1.set_from_file('/media/E/my_works/desktopWidgets/temperatureMonitor/pic/temp.png')
		else:
			self.cssprovider.load_from_data(CSShot)
			self.t1.set_from_file('/media/E/my_works/desktopWidgets/temperatureMonitor/pic/hot.png')
		return True
		
	def button_press_event(self,widget,event):
		if(event.button==1):
			print "Left click"
			Gtk.Window.window_position(2)
		if(event.button==3):
			print self.get_position()
		return True
win = MyWidget()
win.show_all()
Gtk.main()


