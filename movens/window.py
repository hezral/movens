#!/usr/bin/env python3

'''
   Copyright 2020 Adi Hezral (hezral@gmail.com) (https://github.com/hezral)

   This file is part of Movens.

    Movens is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Movens is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Movens.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Gio, Granite
from constants import AppAttributes

class MovensWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # main window properties
        self.props.title = AppAttributes.application_name
        self.props.border_width = 0
        self.props.resizable = True
        self.get_style_context().add_class("rounded")
        width = 900
        height = 640
        self.set_size_request(width, height)
        geometry = Gdk.Geometry()
        setattr(geometry, 'min_height', height)
        setattr(geometry, 'min_width', width)
        self.set_geometry_hints(None, geometry, Gdk.WindowHints.MIN_SIZE)

        # stack container
        stack = Gtk.Stack()
        stack.props.transition_type = Gtk.StackTransitionType.CROSSFADE
        stack.get_style_context().add_class("right-stack")

        welcome = Welcome()
        stack.add_named(welcome, "welcome")
        self.add(stack)



class Welcome(Gtk.Grid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # main icon/logo
        icon = Gtk.Image()
        icon.set_from_icon_name("system-os-installer", Gtk.IconSize.DIALOG)
        icon.set_pixel_size(96)
        icon.props.margin = 15

        # welcome widget
        welcome_widget = Granite.WidgetsWelcome().new("Movens", AppAttributes.application_description)
        welcome_widget.connect("activated", self.on_welcome_activated)

        # welcome menu
        welcome_widget.append("text-x-readme", "README", "Get started manual")
        welcome_widget.append("preferences-desktop", "Preferences", "Configure Movens the way you want it")

        # construct grid
        self.props.margin = 40
        self.attach(icon, 0, 1, 1, 1)
        self.attach(welcome_widget, 0, 2, 1, 1)


    def on_welcome_activated(self, widget, index):
        if index == 0:
            # Use GTK Dark theme
            if self.settings.get_property("gtk-application-prefer-dark-theme") == True:
                self.settings.set_property("gtk-application-prefer-dark-theme", False)
            else:
                self.settings.set_property("gtk-application-prefer-dark-theme", True)
        elif index == 1:
            # Open terminal
            try:
                pass
            except:
                print('Terminal Not Found!')





class MovensApp(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set application properties
        self.props.application_id = AppAttributes.application_id
        self.props.flags=Gio.ApplicationFlags.HANDLES_OPEN

        # set theme and css provider
        Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", False)
        provider = Gtk.CssProvider ()
        provider.load_from_path("/home/adi/Work/movens/data/application.css")
        # provider.load_from_resource ("com/github/hezral/movens/application.css")
        Gtk.StyleContext.add_provider_for_screen (Gdk.Screen.get_default (), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_activate(self):
        # We only allow a single window and raise any existing ones
        if self.window is None:
            # Windows are associated with the application 
            # when the last one is closed the application shuts down
            self.window = MovensWindow(application=self)
            self.add_window(self.window)
            self.window.show_all()

app = MovensApp()
app.run(sys.argv)