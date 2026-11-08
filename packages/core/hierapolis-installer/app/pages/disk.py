"""
Page 5: Dedicated Disk & Filesystem Layout
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from pages import BasePage

class DiskPage(BasePage):
    def __init__(self, installer_window):
        super().__init__(installer_window)

    def create_widget(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.add_css_class("installer-content")

        header = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        header.set_margin_top(24)
        header.set_margin_bottom(8)
        header.set_margin_start(24)
        header.set_margin_end(24)

        title = Gtk.Label(label="Dedicated Disk & Filesystem Layout")
        header.append(title)

        subtitle = Gtk.Label(label="Configure disk partitioning, filesystem, and encryption")
        header.append(subtitle)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.append(Gtk.Box())
        box.append(Gtk.Box())

        return Gtk.Box()
