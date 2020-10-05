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

class UnitEditor(Gtk.Box):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # icon
        unit_icon = UnitIcon()
        #unit_icon.connect("changed", self.on_icon_changed)
        
        # name label
        unit_name_label = Gtk.Label("Name")
        unit_name_label.get_style_context().add_class("h4")
        unit_name_label.set_halign(Gtk.Align.START)

        # name entry
        unit_name_entry = Gtk.Entry()
        unit_name_entry.set_placeholder_text("Enter Name")
        unit_name_entry.get_style_context().add_class("h2")
        unit_name_entry.set_valign(Gtk.Align.START)
        #unit_name_entry.connect("changed", self.on_entry_changed)

        # name header entry construct
        unit_name_header = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        unit_name_header.add(unit_name_label)
        unit_name_header.add(unit_name_entry)
        
        # name box
        unit_name_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        unit_name_box.set_hexpand(True)
        unit_name_box.add(unit_name_header)
        
        # unit header
        unit_header_grid = Gtk.Grid()
        unit_header_grid.set_column_spacing(12)
        unit_header_grid.set_row_spacing(6)
        unit_header_grid.props.margin = 12
        unit_header_grid.attach(unit_icon, 0, 0, 1, 1)
        unit_header_grid.attach(unit_name_box, 1, 0, 1, 1)

        # delete button
        delete_button = Gtk.Button(label="Delete")
        delete_button.get_style_context().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        delete_button.connect("clicked", self.on_item_delete)

        # copy button
        copy_button = Gtk.Button(label="Copy")
        copy_button.connect("clicked", self.on_item_copy)

        # action box construct
        sidebar_action_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        sidebar_action_box.props.margin = 6
        sidebar_action_box.pack_start(copy_button, False, False, 0)
        sidebar_action_box.pack_end(delete_button, False, False, 0)

        # toast
        toast = Granite.WidgetsToast.new("")

        # self construct
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(12)
        self.set_margin_top(12)
        self.set_margin_bottom(12)
        self.set_margin_left(12)
        self.set_margin_right(12)
        self.get_style_context().add_class("item-editor")
        self.pack_start(unit_header_grid, False, False, 0)
        self.pack_end(sidebar_action_box, False, False, 0)

    def on_item_copy(self, event, item):
        pass

    def on_item_delete(self, event, item):
        pass

    def on_icon_changed(self, event, icon):
        pass

    def on_entry_changed(self, event, name):
        pass


class UnitIcon(Gtk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # button construct
        self.get_style_context().add_class("icon-selector-button")
        self.connect("clicked", self.do_clicked)
        self.set_valign(Gtk.Align.START)

        # default icon
        icon = Gtk.Image()
        icon.set_from_icon_name("image-missing", Gtk.IconSize.DIALOG)
        icon.set_pixel_size(64)
        # set button image
        self.set_image(icon)

        # icon selector
        self.icon_selector = IconSelector()
        #self.icon_selector.connect("selected", self.on_set_icon)
        #self.icon_selector.connect("selected_file", self.on_set_icon)


    def on_clicked(self, event):
        self.icon_selector.set_relative_to(self)
        self.icon_selector.show_all()
        self.icon_selector.popup()
        pass

    def on_set_icon(self, event, returnitem):
        
        if returnitem is None:
            pass
        elif returnitem is None:
            pass
        elif returnitem is None:
            pass
        else:
            pass

        self.icon_selector.popdown()

        pass

class IconSelector(Gtk.Popover):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pass
