#!/usr/bin/env  python

import gtk
import webkit

def go(widget):
	address = addressbar.get_text()
	View.open(address)
	 
window = gtk.Window()
window.connect('destroy', lambda w: gtk.main.quit())
window.show()

mainbox = gtk.VBox()
window.add(mainbox)
mainbox.show()

toolbar = gtk.HBox()
mainbox.pack_start(toolbar)
toolbar.show()

addressbar = gtk.Entry()
toolbar.pack_start(addressbar)
addressbar.show()

Go = gtk.Button("GO")
toolbar.pack_start(Go)
Go.connect("clicked", go)
Go.show()

ScrollWindow = gtk.ScrolledWindow()
mainbox.pack_start(ScrollWindow)
ScrollWindow.show()

View = webkit.WebView()
ScrollWindow.add(View)
View.show()

gtk.main()
