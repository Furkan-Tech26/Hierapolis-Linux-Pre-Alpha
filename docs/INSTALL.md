# Hierapolis Linux Installation Guide

## Quick Start (from Live ISO)

```bash
# Boot Hierapolis Linux ISO (base, tty, or xfce variant)
# At the live prompt, run:
sudo hierapolis-install
```

That's it. Follow the prompts.

---

## What `hierapolis-install` Does

| Step | Description |
|------|-------------|
| **Disk Selection** | Lists available disks (`lsblk`), you pick target |
| **Partitioning** | GPT: 512M ESP + rest for root (optional LUKS encryption) |
| **Formatting** | ESP → FAT32, Root → ext4 (or LUKS+ext4) |
| **Base Install** | `pacstrap` downloads Arch packages; `[hierapolis]` packages come from the bundled offline repo |
| **Configuration** | Hostname, users, passwords, locale, timezone, keymap, network |
| **Desktop** | Optional Hierapolis DE (labwc + shell) from the bundled repo |
| **Bootloader** | systemd-boot (UEFI) or GRUB (UEFI/BIOS) |
| **Finish** | Ready to `reboot` |

---

## Requirements

| Requirement | Details |
|-------------|---------|
| **RAM** | 2 GB minimum (4 GB recommended) |
| **Disk** | 20 GB minimum (50 GB+ for desktop) |
| **CPU** | x86_64 (UEFI or BIOS) |
| **Internet** | **Required** — Arch packages are downloaded during install; only the `[hierapolis]` repo is offline |

---

## Step-by-Step Walkthrough

### 1. Boot the ISO
- Ventoy / Rufus / `dd` the ISO to USB
- Boot UEFI (preferred) or BIOS
- Select "Hierapolis Linux" from bootloader
- Login: `root` (no password)

### 2. Run Installer
```bash
sudo hierapolis-install
```

### 3. Disk Selection
```
Available disks:
NAME        SIZE TYPE MODEL
sda        238G disk Samsung SSD 860
nvme0n1    477G disk Samsung 970 EVO

Select target disk (e.g., sda, nvme0n1): nvme0n1
```

### 4. Partitioning
```
Use LUKS encryption for root? [y/N]: y
```
- **No**: ESP (512M) + ext4 root
- **Yes**: ESP (512M) + LUKS2 + ext4 root (prompts for passphrase)

### 5. User Setup
```
Hostname [hierapolis]: my-laptop
Username [twinboi]: furkan
Root password: ********
User password: ********
Timezone [Europe/Istanbul]:
Locale [en_US.UTF-8]:
Keymap [trq]: us
```

### 6. Installation
```
[OK] Partitions created
[OK] Filesystems formatted
[OK] Base system installed
[OK] FSTAB generated
[OK] System configured
[OK] Bootloader installed
```

### 7. Reboot
```bash
reboot
```

---

## Post-Install

### First Boot
- Remove USB
- Select "Hierapolis Linux" in systemd-boot
- Login as your user

### Enable AUR (install a helper first)
```bash
sudo pacman -S --needed base-devel git
git clone https://aur.archlinux.org/yay.git /tmp/yay
(cd /tmp/yay && makepkg -si)

yay -S visual-studio-code-bin
yay -S spotify
```

### Update Mirrors (Turkey-first)
```bash
sudo reflector --country Turkey,Germany,Netherlands --age 12 --protocol https --sort rate --save /etc/pacman.d/mirrorlist
```

### Install Desktop (if using base/tty ISO)
```bash
# XFCE
sudo pacman -S xfce4 xfce4-goodies lightdm lightdm-gtk-greeter network-manager-applet
sudo systemctl enable lightdm

# Or KDE Plasma
sudo pacman -S plasma konsole dolphin firefox sddm
sudo systemctl enable sddm

# Or GNOME
sudo pacman -S gnome gnome-tweaks
sudo systemctl enable gdm
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Not running in Hierapolis Linux live ISO" | You must boot the ISO, not run from another distro |
| "Must run as root" | Use `sudo hierapolis-install` |
| No internet during install | The installer requires network access for Arch packages; configure Wi-Fi with `nmtui` and retry |
| Boot fails (black screen) | Try `nomodeset` kernel param: edit systemd-boot entry at boot |
| LUKS not unlocking | Check `cryptdevice=` in `/boot/loader/entries/hierapolis.conf` matches PARTUUID |

---

## Manual Install (Arch-style)

If you prefer manual control:

```bash
# 1. Partition
cfdisk /dev/nvme0n1  # ESP + root

# 2. Format
mkfs.fat -F32 /dev/nvme0n1p1
mkfs.ext4 /dev/nvme0n1p2

# 3. Mount
mount /dev/nvme0n1p2 /mnt
mount --mkdir /dev/nvme0n1p1 /mnt/boot

# 4. Install
pacstrap -K /mnt base linux linux-firmware systemd networkmanager \
  grub efibootmgr sudo vim hierapolis-keyring hierapolis-mirrorlist

# 5. Configure
genfstab -U /mnt >> /mnt/etc/fstab
arch-chroot /mnt
# ... set locale, hostname, users, mkinitcpio, bootctl ...

# 6. Reboot
exit && reboot
```

---

## Dual Boot with Windows

**Not supported by the text installer yet.** `hierapolis-install` currently wipes the
entire selected disk (`wipefs -a` + `sgdisk -Z`), including any existing ESP and
Windows installation. Do not select a disk that contains data you want to keep.

For dual-boot, use the manual Arch-style install below and create a separate
root partition alongside Windows, reusing the existing ESP without formatting
it. Automated dual-boot partitioning is a planned milestone.

---

## Support

- **Issues**: https://github.com/Furkan-Tech26/Hierapolis-Linux-Pre-Alpha/issues
- **Wiki**: https://github.com/Furkan-Tech26/Hierapolis-Linux-Pre-Alpha/wiki
- **Matrix**: `#hierapolis-linux:matrix.org`