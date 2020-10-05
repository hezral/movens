#!/usr/bin/env python
 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
 
window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)
 
overlay = Gtk.Overlay()
window.add(overlay)

unit_icon = Gtk.Image.new_from_icon_name("application-default-icon", Gtk.IconSize.DIALOG)


textview = Gtk.TextView()
textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
textbuffer = textview.get_buffer()
textbuffer.set_text("Welcome to the PyGObject Tutorial\n\nThis guide aims to provide an introduction to using Python and GTK+.\n\nIt includes many sample code files and exercises for building your knowledge of the language.", -1)

overlay.add(unit_icon)
 

status_image = Gtk.Image.new_from_icon_name("user-offline", Gtk.IconSize.MENU)

 

overlay.add_overlay(status_image)
 
overlay.show_all()
 
window.show_all()
 
Gtk.main()