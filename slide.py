#!/usr/bin/python
from gi.repository import Gtk
from gi.repository.GdkPixbuf import Pixbuf 
width = 10
height= 10



class HeaderBarWindow(Gtk.Window):
	def __init__(self):
	 Gtk.Window.__init__(self, title="Slide show")
	 self.set_border_width(10)
	 self.set_default_size(600, 600)

	 vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
	 self.add(vbox)

	 stack = Gtk.Stack()
	 stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
	 stack.set_transition_duration(1000)

	 image = Gtk.Image()
	 image.set_from_file("Image/(2).jpg")
	 image.set_pixel_size(20)
	 stack.add_titled(image, "image", "Image1")

	 image = Gtk.Image()
	 image.set_from_file("Image/(1).jpg")
	 image.set_pixel_size(10)
	 stack.add_titled(image, "image", "Image2")

	 stack_switcher = Gtk.StackSwitcher()
	 stack_switcher.set_stack(stack)
	 vbox.pack_start(stack_switcher, True, True, 0)
	 vbox.pack_start(stack, True, True, 0)
win = HeaderBarWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
                           
