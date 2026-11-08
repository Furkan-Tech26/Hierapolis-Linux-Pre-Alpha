"""
Page 10: Deployment Summary & Live Execution
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from pages import BasePage, create_button

class SummaryPage(BasePage):
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

        header.append(Gtk.Label(label="Ready to Install"))
        header.append(Gtk.Label(label="Review your configuration and start the installation"))

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.append(Gtk.Box())
        box.append(Gtk.Box())

        return Gtk.Box()
