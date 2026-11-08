"""
Page 2: Target Media & Architecture Mode
"""
import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw
from pages import BasePage, create_section_card, create_button

class TargetMediaPage(BasePage):
    def __init__(self, installer_window):
        super().__init__(installer_window)
        self.deployment_mode = "bare_metal"
        self.arch_mode = "x86_64"

    def create_widget(self):
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.add_css_class("installer-content")

        header = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        header.set_margin_top(24)
        header.set_margin_bottom(8)
        header.set_margin_start(24)
        header.set_margin_end(24)

        title = Gtk.Label(label="Target Media & Architecture Mode")
        header.append(title)

        subtitle = Gtk.Label(label="Choose how and where Hierapolis will be deployed")
        header.append(subtitle)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.append(header)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(16)
        content.set_margin_bottom(32)
        content.set_margin_start(24)
        content.set_margin_end(24)

        # Deployment Mode Card
        deploy_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        deploy_card.add_css_class("card")

        deploy_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        deploy_header.set_margin_bottom(8)

        deploy_icon = Gtk.Image.new_from_icon_name("drive-harddisk-symbolic")
        deploy_icon.set_pixel_size(24)

        deploy_title = Gtk.Label(label="Deployment Mode")
        deploy_title.add_css_class("section-title")
        deploy_header.append(deploy_title)
        deploy_header.set_halign(Gtk.Align.START)

        deploy_desc = Gtk.Label(label="Choose how Hierapolis will be deployed")
        deploy_desc.add_css_class("section-desc")
        deploy_header.append(deploy_desc)
        deploy_header.set_halign(Gtk.Align.START)

        mode_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        mode_box.set_margin_top(8)

        self.bare_metal_radio = Gtk.CheckButton(label="Direct Bare-Metal Install")
        self.bare_metal_radio.set_active(True)
        self.portable_radio = Gtk.CheckButton(label="Custom Portable Media")
        self.portable_radio.set_active(False)

        mode_box.append(Gtk.CheckButton(label="Direct Bare-Metal Install"))
        mode_box.append(Gtk.CheckButton(label="Custom Portable Media"))

        mode_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        mode_card.add_css_class("card")
        mode_card.append(deploy_header)
        mode_card.append(mode_box)

        # Architecture Mode Card
        arch_card = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        arch_card.add_css_class("card")

        arch_header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        arch_icon = Gtk.Image.new_from_icon_name("cpu-symbolic")
        arch_title = Gtk.Label(label="CPU Architecture & Optimization")
        arch_title.add_css_class("section-title")
        arch_header.append(arch_icon)
        arch_header.append(arch_title)
        arch_header.set_halign(Gtk.Align.START)

        arch_desc = Gtk.Label(label="CPU microcode, architecture optimizations, and repository selection")
        arch_desc.add_css_class("section-desc")
        arch_header.append(arch_desc)
        arch_header.set_halign(Gtk.Align.START)

        arch_card.append(arch_header)

        # CPU Microcode
        microcode_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        microcode_box.set_margin_top(8)

        microcode_label = Gtk.Label(label="CPU Microcode & Optimization")
        microcode_label.add_css_class("section-title")

        microcode_combo = Gtk.DropDown.new_from_strings([
            "Auto-detect (recommended)",
            "Intel (intel-ucode)",
            "AMD (amd-ucode)",
            "None (skip microcode)"
        ])
        microcode_combo.set_selected(0)
        microcode_combo.add_css_class("dropdown")
        microcode_combo.set_hexpand(True)

        arch_opt_combo = Gtk.DropDown.new_from_strings([
            "Standard x86_64 (compatible with all 64-bit CPUs)",
            "x86-64-v3 (AVX2, requires Haswell+ / Zen 2+)",
            "x86-64-v4 (AVX-512, requires Skylake-X / Zen 4+)",
            "CachyOS / ALHP optimized repos"
        ])
        arch_opt_combo.set_selected(0)
        arch_opt_combo.add_css_class("dropdown")
        arch_opt_combo.set_hexpand(True)

        opt_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        opt_box.append(Gtk.Label(label="CPU Microcode:", xalign=0))
        opt_box.append(microcode_combo)
        opt_box.append(Gtk.Label(label="Architecture Optimization:", xalign=0))
        opt_box.append(arch_opt_combo)

        # Add all cards to content
        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=24)
        content.set_margin_top(16)
        content.set_margin_bottom(32)
        content.set_margin_start(24)
        content.set_margin_end(24)

        header = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        header.set_margin_top(24)
        header.set_margin_bottom(8)
        header.set_margin_start(24)
        header.set_margin_end(24)

        title = Gtk.Label(label="Target Media & Architecture Mode")
        header.append(title)

        subtitle = Gtk.Label(label="Choose how and where Hierapolis will be deployed")
        header.append(subtitle)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        box.append(header)
        box.append(Gtk.Box())
        box.append(Gtk.Box())

        return Gtk.Box()
