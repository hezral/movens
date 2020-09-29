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


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from constants import app

class MovensWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.props.title = app.app_name
        self.props.border_width = 0
        self.props.resizable = True
        self.get_style_context().add_class("rounded")
        #self.get_style_context().add_class("flat")
        width = 720
        height = 480
        self.set_default_size(width, height)

        Gtk.Settings.get_default ().gtk_application_prefer_dark_theme = True

        provider = Gtk.CssProvider ()
        provider.load_from_path("/home/adi/Work/movens/data/application.css")
        # provider.load_from_resource ("com/github/hezral/movens/application.css")
        Gtk.StyleContext.add_provider_for_screen (Gdk.Screen.get_default (), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)


        btn_start = Gtk.Button("Start Working")
        btn_start.get_style_context ().add_class ("btn-start")

        btn_pause = Gtk.Button("Take a Break")
        btn_pause.get_style_context ().add_class ("btn-pause")

        btn_stop = Gtk.Button("Stop")
        btn_stop.get_style_context ().add_class ("btn-stop")

        app_label = Gtk.Label ("Actions")
        app_label.get_style_context ().add_class ("h4")
        app_label.props.xalign = 0

        actions_grid = Gtk.Grid ()
        actions_grid.get_style_context ().add_class ("actions-grid")
        actions_grid.props.orientation = Gtk.Orientation.VERTICAL
        actions_grid.props.row_spacing = 12
        actions_grid.props.margin = 12
        actions_grid.add (app_label)
        actions_grid.add (btn_start)
        actions_grid.add (btn_pause)
        actions_grid.add (btn_stop)

        timer_label = Gtk.Label ()
        timer_label.get_style_context ().add_class ("timer-label")
        timer_label.get_style_context ().add_class ("h1")
        timer_label.set_label("00:00")
        timer_label.props.expand = True
        timer_label.props.valign = Gtk.Align.CENTER
        timer_label.props.halign = Gtk.Align.CENTER


        timer_grid = Gtk.Grid ()
        timer_grid.get_style_context ().add_class ("timer-grid")
        timer_grid.attach (timer_label, 0, 0, 3, 1);


        main_grid = Gtk.Grid ()
        main_grid.add (actions_grid)
        main_grid.add (timer_grid)

        actions_header = Gtk.HeaderBar ()
        actions_header.props.decoration_layout = "close:"
        actions_header.props.show_close_button = True
        actions_header.props.title = ("Movens")

        actions_header_context = actions_header.get_style_context ()
        actions_header_context.add_class ("actions-header")
        actions_header_context.add_class ("titlebar")
        actions_header_context.add_class ("default-decoration")
        actions_header_context.add_class (Gtk.STYLE_CLASS_FLAT)

        timer_header = Gtk.HeaderBar ()
        timer_header.props.hexpand = True

        timer_header_context = timer_header.get_style_context ()
        timer_header_context.add_class ("timer-header")
        timer_header_context.add_class ("titlebar")
        timer_header_context.add_class ("default-decoration")
        timer_header_context.add_class (Gtk.STYLE_CLASS_FLAT)

        actions_header_grid = Gtk.Grid()
        actions_header_grid.add(actions_header)
        actions_header_grid.set_size_request(200, -1)

        header_grid = Gtk.Grid ()
        header_grid.add (actions_header_grid)
        header_grid.add (timer_header)

        sizegroup = Gtk.SizeGroup (Gtk.SizeGroupMode.HORIZONTAL)
        sizegroup.add_widget (actions_grid)
        sizegroup.add_widget (actions_header)

        self.add(main_grid)
        self.set_titlebar(header_grid)


win = MovensWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()