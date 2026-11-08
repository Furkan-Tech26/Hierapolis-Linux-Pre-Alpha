"""
Page 1: Pre-Flight & Hardware Telemetry
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, Gdk
from pages import BasePage, create_section_card, create_button

class WelcomePage(BasePage):
    def __init__(self, installer_window):
        super().__init__(installer_window)
        self.hardware_box = None
        self.hw_grid = None

    def create_widget(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.add_css_class("installer-content")

        header = self.create_page_header(
            "Welcome to Hierapolis Linux",
            "A modern, Anatolian-inspired Linux distribution based on Arch Linux\nwith a custom Wayland desktop environment.",
            "preferences-system-symbolic"
        )

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(16)
        content.set_margin_bottom(32)
        content.set_margin_start(24)
        content.set_margin_end(24)

        # Hardware telemetry card
        self.hardware_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.hardware_box.add_css_class("card")
        self.hardware_box.set_margin_bottom(16)

        hw_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        hw_header.set_margin_bottom(8)

        hw_icon = Gtk.Image.new_from_icon_name("computer-symbolic")
        hw_icon.set_pixel_size(24)
        hw_header.append(Gtk.Image.new_from_icon_name("computer-symbolic"))

        hw_title = Gtk.Label(label="System Telemetry")
        hw_title.add_css_class("section-title")
        hw_header.append(hw_title)
        hw_header.set_halign(Gtk.Align.START)

        hw_desc = Gtk.Label(label="Real-time hardware detection and system telemetry")
        hw_desc.add_css_class("section-desc")
        hw_header.append(hw_desc)
        hw_header.set_halign(Gtk.Align.START)

        self.hardware_box.append(hw_header)

        # Hardware info grid
        self.hw_grid = Gtk.Grid()
        self.hw_grid.set_row_spacing(8)
        self.hw_grid.set_column_spacing(24)
        self.hw_grid.set_margin_top(8)
        self.hardware_box.append(self.hw_grid)

        # Mirrorlist optimization card
        mirror_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        mirror_card.add_css_class("card")
        mirror_card.set_margin_bottom(16)

        mirror_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        mirror_header.set_margin_bottom(8)

        mirror_icon = Gtk.Image.new_from_icon_name("network-server-symbolic")
        mirror_icon.set_pixel_size(24)
        mirror_header.append(Gtk.Image.new_from_icon_name("network-server-symbolic"))

        mirror_title = Gtk.Label(label="Mirrorlist Optimization")
        mirror_title.add_css_class("section-title")
        mirror_header.append(mirror_title)
        mirror_header.set_halign(Gtk.Align.START)

        mirror_desc = Gtk.Label(label="Built-in reflector integration to benchmark and rank the fastest Arch mirrors by country, protocol (HTTPS), and sync age.")
        mirror_desc.add_css_class("section-desc")
        mirror_desc.set_wrap(True)
        mirror_header.append(mirror_desc)
        mirror_header.set_halign(Gtk.Align.START)

        mirror_card.append(mirror_header)

        mirror_btn = Gtk.Button(label="Optimize Mirrorlist Now")
        mirror_btn.add_css_class("btn-primary")
        mirror_header.append(mirror_btn)
        mirror_header.set_halign(Gtk.Align.END)

        # Localization card
        locale_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        locale_card.add_css_class("card")
        locale_card.set_margin_bottom(16)

        locale_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        locale_header.set_margin_bottom(8)

        locale_icon = Gtk.Image.new_from_icon_name("preferences-desktop-locale-symbolic")
        locale_icon.set_pixel_size(24)
        locale_header.append(Gtk.Image.new_from_icon_name("preferences-desktop-locale-symbolic"))

        locale_title = Gtk.Label(label="Localization & Keymap")
        locale_title.add_css_class("section-title")
        locale_header.append(locale_title)
        locale_header.set_halign(Gtk.Align.START)

        locale_desc = Gtk.Label(label="Installer UI language, system locale, keyboard layout, and vconsole keymap.")
        locale_desc.add_css_class("section-desc")
        locale_desc.set_wrap(True)
        locale_header.append(locale_desc)
        locale_header.set_halign(Gtk.Align.START)

        locale_card.append(locale_header)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(16)
        content.set_margin_bottom(32)
        content.set_margin_start(24)
        content.set_margin_end(24)

        content.append(self.hardware_box)
        content.append(mirror_card)
        content.append(locale_card)

        # Action buttons
        action_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        action_box.set_margin_top(16)
        action_box.set_halign(Gtk.Align.END)

        continue_btn = Gtk.Button(label="Continue \u2192")
        continue_btn.add_css_class("btn-primary")
        continue_btn.connect("clicked", lambda b: self.window.on_next_clicked(None))
        action_box.append(continue_btn)

        content.append(action_box)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main_box.add_css_class("installer-content")
        main_box.append(self.create_page_header(
            "Welcome to Hierapolis Linux",
            "A modern, Anatolian-inspired Linux distribution based on Arch Linux\nwith a custom Wayland desktop environment.",
            "preferences-system-symbolic"
        ))
        main_box.append(content)

        self.hardware_box = self.hardware_box
        return main_box

    def update_hardware_info(self, hw_info):
        if not self.hw_grid:
            return

        for child in self.hw_grid.get_children():
            self.hw_grid.remove(child)

        items = [
            ("CPU", hw_info.get("cpu", "Detecting...")),
            ("RAM", hw_info.get("ram", "Detecting...")),
            ("Firmware", hw_info.get("firmware", "Detecting...")),
            ("Secure Boot", hw_info.get("secure_boot", "Detecting...")),
        ]

        disks = hw_info.get("disks", [])
        if disks:
            disk_str = ", ".join([d.get("model", d.get("name", "Unknown")) + " (" + d.get("size", "?") + ")" for d in disks[:3]])
            items.append(("Disks", disk_str))

        for i, (label, value) in enumerate(items):
            label_widget = Gtk.Label(label=label)
            label_widget.add_css_class("hardware-label")
            label_widget.set_halign(Gtk.Align.START)

            value_widget = Gtk.Label(label=str(value))
            value_widget.add_css_class("hardware-value")
            value_widget.set_halign(Gtk.Align.END)
            value_widget.set_selectable(True)

            self.hw_grid.attach(label_widget, 0, i, 1, 1)
            self.hw_grid.attach(value_widget, 1, i, 1, 1)
