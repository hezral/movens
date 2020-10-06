#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

class application_gui:

    def __init__(self):
        self.window = Gtk.Window()

        GObject.signal_new('custom-signal', self.window, GObject.SIGNAL_RUN_LAST, GObject.TYPE_PYOBJECT, (GObject.TYPE_PYOBJECT,))

        self.window.connect('custom-signal', self.custom_signal1_method)

        self.window.emit('custom-signal', 'hello from signal')

        self.window.connect('delete_event', Gtk.main_quit)
        
        self.window.connect('destroy', lambda quit: Gtk.main_quit())

        self.window.show()

    def custom_signal1_method(self, *args):
        print('Custom signal')
        print(args)

application = application_gui()
Gtk.main()
