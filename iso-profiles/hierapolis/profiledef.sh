#!/usr/bin/env bash
#
# Hierapolis Linux DE profile definition for archiso
# Full Hierapolis DE (labwc + GTK4 shell) — composes on top of the base profile
#

profile_name="hierapolis-de"
profile_description="Hierapolis Linux with the in-house Hierapolis DE (Wayland, Win 8.1 start menu)"

arch="x86_64"

iso_name="hierapolis-de"
iso_label="HIERAPOLIS_DE_$(date +%Y%m)"
iso_publisher="Hierapolis Linux <https://github.com/Furkan-Tech26/Hierapolis-Linux-Pre-Alpha>"
iso_application="Hierapolis Linux DE Live/Install ISO"
iso_version="$(date +%Y.%m.%d)"

install_dir="hierapolis"

buildmodes=('iso')
bootmodes=('bios.syslinux' 'uefi.systemd-boot')

pacman_conf="pacman.conf"

airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd' '-Xcompression-level' '15' '-b' '1M')

file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
)

# vim: set ft=sh:
