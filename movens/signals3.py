#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject


class MovensWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        GObject.signal_new("print-this", GObject.TYPE_OBJECT, GObject.SIGNAL_RUN_LAST, GObject.TYPE_BOOLEAN, [GObject.TYPE_STRING])

        self.button = Gtk.Button.new_with_label("Emit signals")
        self.button.connect("clicked", self.emit_signals)

        self.frame = Gtk.Frame.new("Some frame")
        self.frame.add(self.button)
        self.add(self.frame)

        self.connect("print-this", self.got_it)
        self.show_all()
        Gtk.main()

    def got_it(self, widget, string):
        print(string)
        return False

    def emit_signals(self, *args):
        print("Emitting signals..")
        self.button.emit("print-this", "I was emitted from the button")
        self.frame.emit("print-this", "I was emitted from the frame")
        self.emit("print-this", "I was emitted from the window")

application = MovensWindow()
Gtk.main()