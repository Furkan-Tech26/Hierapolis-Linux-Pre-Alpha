#!/usr/bin/env bash
#
# Hierapolis Linux base profile definition for archiso
# Independent distro using pacman + Arch repos + AUR
# "Hierapolis" = badger (Anatolian native), successor to Pardus (leopard)
#

# Profile name and description
profile_name="hierapolis-base"
profile_description="Hierapolis Linux - Minimal base using pacman, Arch repos & AUR"

# Architecture
arch="x86_64"

# ISO settings
iso_name="hierapolis"
iso_label="HIERAPOLIS_$(date +%Y%m)"
iso_publisher="Hierapolis Linux <https://github.com/Furkan-Tech26/Hierapolis-Linux-Pre-Alpha>"
iso_application="Hierapolis Linux Live/Install ISO"
iso_version="$(date +%Y.%m.%d)"

# Installation settings
install_dir="hierapolis"

# Build modes and boot modes (modern archiso syntax)
buildmodes=('iso')
bootmodes=('bios.syslinux' 'uefi.systemd-boot')

# Pacman configuration for the live environment
pacman_conf="pacman.conf"

# Squashfs image settings
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'zstd' '-Xcompression-level' '15' '-b' '1M')

# File permissions (archiso requires this array)
file_permissions=(
  ["/etc/shadow"]="0:0:400"
  ["/etc/gshadow"]="0:0:400"
)

# vim: set ft=sh:
