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

class WelcomeView(Gtk.Grid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.settings = Gtk.Settings.get_default()

        # main icon/logo
        icon = Gtk.Image()
        icon.set_from_icon_name("com.github.hezral.inspektor", Gtk.IconSize.DIALOG)
        icon.set_pixel_size(128)
        icon.set_valign(Gtk.Align.END)
        icon.set_halign(Gtk.Align.CENTER)
        icon.props.margin = 15

        # welcome widget
        welcome_widget = Granite.WidgetsWelcome().new("Movens", AppAttributes.application_description)
        welcome_widget.connect("activated", self.on_welcome_activated)

        # welcome menu
        welcome_widget.append("text-x-readme", "README", "Get started manual")
        welcome_widget.append("preferences-desktop", "Preferences", "Configure Movens the way you want it")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.props.margin = 40
        box.pack_start(icon, False, False, 0)
        box.pack_end(welcome_widget, True, True, 0)

        self.add(box)

        # construct grid
        # self.props.margin = 40
        # self.attach(icon, 0, 1, 1, 1)
        # self.attach(welcome_widget, 0, 2, 1, 1)

    def on_welcome_activated(self, widget, index):
        # add index actions based on menu items in welcome widget
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