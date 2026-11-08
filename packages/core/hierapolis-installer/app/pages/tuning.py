"""
Page 9: System Tuning, Network & Security
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from pages import BasePage

class TuningPage(BasePage):
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

        header.append(Gtk.Label(label="System Tuning, Network & Security"))
        header.append(Gtk.Label(label="Performance tuning, network configuration, and security hardening"))

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.append(Gtk.Box())
        box.append(Gtk.Box())

        return Gtk.Box()
