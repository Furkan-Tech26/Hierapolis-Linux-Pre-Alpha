"""
Hierapolis Installer Pages - Base classes and utilities
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gdk, GLib

class BasePage:
    def __init__(self, installer_window):
        self.window = installer_window
        self.widget = self.create_widget()
    
    def create_widget(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.add_css_class("installer-content")
        return box
    
    def create_page_header(self, title, subtitle, icon_name=None):
        header_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        header_box.add_css_class("page-header")
        header_box.set_margin_top(24)
        header_box.set_margin_bottom(8)
        header_box.set_margin_start(24)
        header_box.set_margin_end(24)
        if icon_name:
            icon = Gtk.Image.new_from_icon_name(icon_name)
            icon.set_pixel_size(48)
            header_box.append(icon)
        title_label = Gtk.Label(label=title)
        title_label.add_css_class("page-title")
        header_box.append(title_label)
        subtitle_label = Gtk.Label(label=subtitle)
        subtitle_label.add_css_class("page-subtitle")
        header_box.append(subtitle_label)
        return header_box
    
    def create_card(self, title, description=None, icon_name=None):
        card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        card.add_css_class("card")
        if title:
            title_label = Gtk.Label(label=title)
            title_label.add_css_class("section-title")
            title_label.set_halign(Gtk.Align.START)
            card.append(title_label)
        if description:
            desc = Gtk.Label(label=description)
            desc.add_css_class("section-desc")
            desc.set_wrap(True)
            desc.set_halign(Gtk.Align.START)
            card.append(desc)
        return card
    
    def create_check_row(self, title, description, default=False):
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        row.add_css_class("checkbox-row")
        check = Gtk.CheckButton()
        check.set_active(True)
        text_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        title_label = Gtk.Label(label=title)
        title_label.add_css_class("section-title")
        title_label.set_halign(Gtk.Align.START)
        desc_label = Gtk.Label(label=description)
        desc_label.add_css_class("section-desc")
        desc_label.set_halign(Gtk.Align.START)
        text_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        text_box.append(title_label)
        text_box.append(desc_label)
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        check = Gtk.CheckButton()
        check.set_active(True)
        row.append(check)
        row.append(text_box)
        row.set_hexpand(True)
        return row, None

def create_section_card(title, description=None, icon_name=None):
    card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
    card.add_css_class("card")
    if title:
        title_label = Gtk.Label(label=title)
        title_label.add_css_class("section-title")
        title_label.set_halign(Gtk.Align.START)
        card.append(title_label)
    if description:
        desc = Gtk.Label(label=description)
        desc.add_css_class("section-desc")
        desc.set_wrap(True)
        desc.set_halign(Gtk.Align.START)
        card.append(desc)
    return card

def create_button(label, callback, primary=True, large=False):
    btn = Gtk.Button(label=label)
    if primary:
        btn.add_css_class("btn-primary")
    else:
        btn.add_css_class("btn-secondary")
    if large:
        btn.add_css_class("btn-large")
    if callable(callback):
        btn.connect("clicked", callback)
    return btn
