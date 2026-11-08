"""
Page 3: Kernel & Low-Level Stack
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from pages import BasePage, create_section_card, create_button

class KernelPage(BasePage):
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

        title = Gtk.Label(label="Kernel & Low-Level Stack")
        header.append(title)

        subtitle = Gtk.Label(label="Select kernels and configure the low-level boot stack")
        header.append(subtitle)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.append(header)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(16)
        content.set_margin_bottom(32)
        content.set_margin_start(24)
        content.set_margin_end(24)

        # Kernel Selection Card
        kernel_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        kernel_card.add_css_class("card")

        kernel_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        kernel_header.set_margin_bottom(8)

        kernel_icon = Gtk.Image.new_from_icon_name("drive-harddisk-system-symbolic")
        kernel_icon.set_pixel_size(24)

        kernel_title = Gtk.Label(label="Kernel Selection (Multi-select supported)")
        kernel_title.add_css_class("section-title")
        kernel_header.append(kernel_title)
        kernel_header.set_halign(Gtk.Align.START)

        kernel_desc = Gtk.Label(label="Select one or more kernels. Multiple kernels can be installed side-by-side.")
        kernel_desc.add_css_class("section-desc")
        kernel_header.append(kernel_desc)
        kernel_header.set_halign(Gtk.Align.START)

        kernel_card.append(kernel_header)

        # Kernel checkboxes
        kernels = [
            ("linux", "Vanilla Arch latest", "Latest stable kernel from Arch repositories", True),
            ("linux-lts", "Long-Term Support", "Long-term support kernel for stability", False),
            ("linux-zen", "Zen (Desktop & Gaming)", "Optimized for desktop responsiveness and gaming", True),
            ("linux-hardened", "Hardened (Security)", "Security-focused kernel with additional hardening", False),
            ("linux-cachyos", "CachyOS (BORE Scheduler)", "Custom BORE scheduler builds for responsiveness", False),
        ]

        self.kernel_checks = {}
        for pkg, title, desc, default in kernels:
            row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
            row.add_css_class("checkbox-row")

            check = Gtk.CheckButton()
            check.set_active(True)

            text_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
            title_label = Gtk.Label(label=title)
            title_label.add_css_class("section-title")
            title_label.set_halign(Gtk.Align.START)

            desc_label = Gtk.Label(label=desc)
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

            content.append(row)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(16)
        content.set_margin_bottom(32)
        content.set_margin_start(24)
        content.set_margin_end(24)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        main_box.append(Gtk.Box())
        main_box.append(Gtk.Box())

        return Gtk.Box()
