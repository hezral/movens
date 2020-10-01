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
from gi.repository import Gtk, Gdk, Gio, Granite, GObject
from constants import AppAttributes


#------------------CLASS-SEPARATOR------------------#

class MovensWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self construct
        self.props.title = AppAttributes.application_name
        self.set_border_width(0)
        self.set_resizable(True)
        
        width = 900
        height = 640
        self.set_size_request(width, height)
        geometry = Gdk.Geometry()
        setattr(geometry, 'min_height', height)
        setattr(geometry, 'min_width', width)
        self.set_geometry_hints(None, geometry, Gdk.WindowHints.MIN_SIZE)




        # stack construct
        stack = Gtk.Stack()
        stack.props.transition_type = Gtk.StackTransitionType.CROSSFADE
        stack.get_style_context().add_class("right-stack")
        # stack.set_size_request(645, -1)

        welcome = WelcomeView()
        unit_editor = UnitEditor()
        stack.add_named(welcome, "welcome")
        stack.add_named(unit_editor, "unit_editor")

        # units listbox construct
        units_listbox = Gtk.ListBox()
        units_listbox.get_style_context().add_class("pane")
        units_listbox.set_activate_on_single_click(True)
        units_listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        units_listbox.set_hexpand(True)
        units_listbox.set_vexpand(True)

        ## add units to the listbox
        # pass

        # sidebar action box
        ## settings button
        settings_button = Gtk.Button(image=Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.MENU))
        settings_button.set_valign(Gtk.Align.CENTER)
        settings_button.set_halign(Gtk.Align.START)
        settings_button.set_always_show_image(True)
        settings_button.set_can_focus(False)
        settings_button.get_style_context().add_class ("flat")
        settings_button.get_style_context().add_class ("font-bold")
        settings_button.get_style_context().add_class ("ql-button")

        ## add units button
        add_units_button = Gtk.Button(image=Gtk.Image.new_from_icon_name("list-add-symbolic", Gtk.IconSize.MENU))
        add_units_button.set_valign(Gtk.Align.CENTER)
        add_units_button.set_halign(Gtk.Align.FILL)
        add_units_button.set_always_show_image(True)
        add_units_button.set_can_focus(False)
        add_units_button.get_style_context().add_class ("flat")
        add_units_button.get_style_context().add_class ("font-bold")
        add_units_button.get_style_context().add_class ("ql-button")

        ## delete units button
        delete_units_button = Gtk.Button(image=Gtk.Image.new_from_icon_name("list-remove-symbolic", Gtk.IconSize.MENU))
        delete_units_button.set_valign(Gtk.Align.CENTER)
        delete_units_button.set_halign(Gtk.Align.FILL)
        delete_units_button.set_always_show_image(True)
        delete_units_button.set_can_focus(False)
        delete_units_button.get_style_context().add_class ("flat")
        delete_units_button.get_style_context().add_class ("font-bold")
        delete_units_button.get_style_context().add_class ("ql-button")

        ## action box construct
        sidebar_action_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        # sidebar_action_box.get_style_context().add_class("bottom-buttons")
        sidebar_action_box.set_margin_end(9)
        sidebar_action_box.set_margin_bottom(6)
        sidebar_action_box.set_margin_top(6)
        sidebar_action_box.set_margin_start(9)
        sidebar_action_box.set_hexpand(True)
        sidebar_action_box.set_halign(Gtk.Align.FILL)
        sidebar_action_box.pack_start(settings_button, False, False, 0)
        sidebar_action_box.pack_end(delete_units_button, False, False, 0)
        sidebar_action_box.pack_end(add_units_button, False, False, 0)
        

        # drag n drop grid construct
        drag_drop_grid = Gtk.Grid()
        drag_drop_grid.set_margin_start(6)
        drag_drop_grid.set_margin_end(6)
        drag_drop_grid.props.height_request = 12

        # motion grid construct
        motion_grid = Gtk.Grid()
        motion_grid.set_margin_start(6)
        motion_grid.set_margin_end(6)
        motion_grid.set_margin_bottom(12)
        motion_grid.props.height_request = 24
        motion_grid.get_style_context().add_class("grid-motion")
        motion_grid_revealer = Gtk.Revealer()
        motion_grid_revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_DOWN)
        motion_grid_revealer.add(motion_grid)

        # drag n drop construct
        # Gtk.drag_dest_set (units_listbox, Gtk.DestDefaults.ALL, TARGET_WORKSPACES, Gdk.DragAction.MOVE);
        # units_listbox.drag_data_received.connect (on_drag_data_received_workspace);

        # Gtk.drag_dest_set (drag_drop_grid, Gtk.DestDefaults.ALL, TARGET_WORKSPACES, Gdk.DragAction.MOVE);
        # drag_drop_grid.drag_data_received.connect (on_drag_data_received_workspace_top);

        # drop_area_grid.drag_motion.connect ((context, x, y, time) => {
        #     motion_area_revealer.reveal_child = true;
        #     return true;
        # });

        # drop_area_grid.drag_leave.connect ((context, time) => {
        #     motion_area_revealer.reveal_child = false;
        # });

        # units listbox scrolled window construct
        units_listbox_scrolled = Gtk.ScrolledWindow()
        units_listbox_scrolled.set_hexpand(True)
        units_listbox_scrolled.set_margin_bottom(6)
        units_listbox_scrolled.add(units_listbox)

        # sidebar construct
        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.get_style_context().add_class("pane")
        #sidebar.get_style_context().add_class("sidebar")
        sidebar.add(drag_drop_grid)
        sidebar.add(motion_grid_revealer)
        sidebar.pack_start(units_listbox_scrolled, True, True, 0)
        sidebar.add(Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL))
        sidebar.pack_end(sidebar_action_box, False, False, 0)
        sidebar.set_size_request(255, -1)

        # main pane construct
        pane = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        pane.get_style_context().add_class("pane")
        pane.pack1(sidebar, False, False)
        pane.pack2(stack, True, False)
        #pane.props.min_position = 255

        # header construct
        left_header = Gtk.HeaderBar()
        left_header.set_decoration_layout("close")
        left_header.set_show_close_button(True)
        left_header.get_style_context().add_class("left-header")
        left_header.get_style_context().add_class("titlebar")
        left_header.get_style_context().add_class("default-decoration")
        left_header.get_style_context().add_class(Gtk.STYLE_CLASS_FLAT)

        gtk_settings = Gtk.Settings.get_default()
        mode_switch = Granite.ModeSwitch.from_icon_name("display-brightness-symbolic", "weather-clear-night-symbolic")
        mode_switch.props.primary_icon_tooltip_text = "Light mode"
        mode_switch.props.secondary_icon_tooltip_text = "Dark mode"
        mode_switch.set_valign(Gtk.Align.CENTER)
        mode_switch.bind_property("active", gtk_settings, "gtk-application-prefer-dark-theme", GObject.BindingFlags.BIDIRECTIONAL)

        

        right_header = Gtk.HeaderBar()
        right_header.set_decoration_layout(":maximize")
        right_header.set_show_close_button(True)
        right_header.get_style_context().add_class("right-header")
        right_header.get_style_context().add_class("titlebar")
        right_header.get_style_context().add_class("default-decoration")
        right_header.get_style_context().add_class(Gtk.STYLE_CLASS_FLAT)
        right_header.set_hexpand(True)
        right_header.pack_end(mode_switch)

        header_paned = Gtk.Paned(orientation=Gtk.Orientation.HORIZONTAL)
        header_paned.pack1(left_header, False, False)
        header_paned.pack2(right_header, True, False)
        #header_paned.props.min_position = 255        
        
        self.get_style_context().add_class("rounded")
        self.set_titlebar(header_paned)
        header_paned.get_style_context().remove_class("titlebar")

        # self construct
        self.add(pane)

        settings = Gio.Settings(schema_id="com.github.hezral.movens")

        settings.bind("pane-position", header_paned, "position", Gio.SettingsBindFlags.DEFAULT)
        settings.bind("pane-position", pane, "position", Gio.SettingsBindFlags.DEFAULT)
        settings.bind ("prefer-dark-style", mode_switch, "active", Gio.SettingsBindFlags.DEFAULT)


#------------------CLASS-SEPARATOR------------------#

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



#------------------CLASS-SEPARATOR------------------#




#------------------CLASS-SEPARATOR------------------#


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


#------------------CLASS-SEPARATOR------------------#


class IconSelector(Gtk.Popover):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pass


#------------------CLASS-SEPARATOR------------------#


class WelcomeView(Gtk.Grid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.settings = Gtk.Settings.get_default()

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


#------------------CLASS-SEPARATOR------------------#


class MovensApp(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set application properties
        self.props.application_id = AppAttributes.application_id
        self.props.flags=Gio.ApplicationFlags.HANDLES_OPEN

        # set theme and css provider
        #Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", False)
        provider = Gtk.CssProvider()
        provider.load_from_path("/home/adi/Work/movens/data/application.css")
        # provider.load_from_resource ("com/github/hezral/movens/application.css")
        Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(), provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        # initialize any objects
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


#------------------CLASS-SEPARATOR------------------#


app = MovensApp()
app.run(sys.argv)