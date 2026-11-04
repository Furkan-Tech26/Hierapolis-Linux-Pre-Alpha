# Hierapolis Linux — Build Instructions                                                       
```text                                                                               
      :::    ::: ::::::::::: :::::::::: :::::::::      :::     :::::::::   ::::::::  :::        ::::::::::: :::::::: 
     :+:    :+:     :+:     :+:        :+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:            :+:    :+:    :+: 
    +:+    +:+     +:+     +:+        +:+    +:+  +:+   +:+  +:+    +:+ +:+    +:+ +:+            +:+    +:+         
   +#++:++#++     +#+     +#++:++#   +#++:++#:  +#++:++#++: +#++:++#+  +#+    +:+ +#+            +#+    +#++:++#++   
  +#+    +#+     +#+     +#+        +#+    +#+ +#+     +#+ +#+        +#+    +#+ +#+            +#+           +#+    
 #+#    #+#     #+#     #+#        #+#    #+# #+#     #+# #+#        #+#    #+# #+#            #+#    #+#    #+#     
###    ### ########### ########## ###    ### ###     ### ###         ########  ########## ########### ########       
 ```
> This is the build wiki (kinda) of the Turkish Linux Distrobution, Hierapolis Linux (Comes from the anatolian wild cat Lynx)

---

## Project Structure

```
hierapolis-linux/
├── iso-profiles/
│   ├── base/           # Shared base (all variants)
│   │   ├── profiledef.sh
│   │   ├── pacman.conf  # build-time pacman config ([hierapolis] local repo)
│   │   ├── packages.x86_64
│   │   ├── efiboot/     # UEFI systemd-boot menus
│   │   ├── syslinux/    # BIOS syslinux menu
│   │   └── airootfs/   # Live ISO overlay
│   ├── tty/            # Pure CLI variant (base + extras)
│   ├── xfce/           # XFCE desktop variant
│   └── hierapolis/          # Custom Hierapolis DE variant
├── installer/
│   └── hierapolis-install   # Text-mode installer (packaged by hierapolis-installer)
├── packages/
│   ├── core/           # Custom packages for [hierapolis] repo
│   │   ├── hierapolis-keyring/
│   │   ├── hierapolis-mirrorlist/
│   │   ├── hierapolis-installer/
│   │   ├── hierapolis-desktop-settings/
│   │   ├── hierapolis-artwork/
│   │   ├── hierapolis-calamares/
│   │   └── hierapolis-vpm/
│   └── desktop/        # Custom Hierapolis DE packages
│       ├── hierapolis-shell/
│       ├── hierapolis-settings/
│       ├── hierapolis-theme/
│       ├── hierapolis-session/
│       └── hierapolis-de-meta/
├── docs/
│   └── INSTALL.md
├── build-repo.sh       # Run in VM: builds custom packages → local repo
└── build-iso.sh        # Run in VM: composes profile + builds ISO
```

---

## What to Push to GitHub

Clone this repo into your GitHub page and push everything EXCEPT:
- `iso-profiles/*/work/` — build cache (auto-generated)
- `iso-profiles/*/out/` — ISO output files (auto-generated)
- `*.pkg.tar.zst` — built packages (auto-generated)
- `*-debug-*.pkg.tar.zst` — debug packages

Add this `.gitignore` to the repo root:

```gitignore
# Build artifacts
*.pkg.tar.zst
*-debug-*.pkg.tar.zst
iso-profiles/*/work/
iso-profiles/*/out/
*.sig
*.asc

# Pacman
pkg/
src/

# IDE / OS
.vscode/
.idea/
.DS_Store
Thumbs.db
```

---

## Quick Start (in VMware Arch VM)

```bash
# 1. Install dependencies
sudo pacman -S --needed archiso base-devel git rsync librsvg python-gobject gtk4

# 2. Clone from GitHub
git clone https://github.com/Furkan-Tech26/Hierapolis-Linux-Pre-Alpha.git ~/hierapolis-linux
cd ~/hierapolis-linux

# 3. Build custom packages & create local [hierapolis] repo
sudo ./build-repo.sh

# 4. Build TTY/CLI ISO (minimal, fast)
sudo ./build-iso.sh tty

# 5. Test boot
qemu-system-x86_64 -cdrom iso-profiles/tty/out/hierapolis-*.iso -m 2G -enable-kvm
```

**No more manual SVG→PNG conversion!** The PKGBUILDs now auto-convert SVGs to PNGs during `makepkg` using `rsvg-convert` from the `librsvg` package.

---

## Build Scripts Explained

| Script | Purpose | Run As | When |
|--------|---------|--------|------|
| `build-repo.sh` | Builds all custom packages (core + desktop), creates the local repo (signing optional: `HIERAPOLIS_SIGN_REPO=1`) | user (uses sudo internally) | Once, or after package changes |
| `build-iso.sh` | Composes the variant profile and builds the ISO (base/tty/xfce/hierapolis) | **root** (required by archiso) | Every ISO build |

### CI: GitHub Actions (recommended)

`.github/workflows/build-iso.yml` builds ISOs in an Arch Linux container on GitHub runners:

- **Manual**: Actions → *Build ISO* → *Run workflow* → pick `base` / `tty` / `xfce` / `hierapolis`
- **On tag**: push `v*` tags to build the `hierapolis` ISO

The finished `.iso` is uploaded as a workflow artifact (14-day retention). This is the intended way to get a solid ISO before touching real hardware.

---

## Variants

| Variant | Profile | Packages | Use Case |
|---------|---------|----------|----------|
| **base** | `iso-profiles/base` | Minimal + installer | Custom builds, servers |
| **tty** | `iso-profiles/tty` | = base | Pure CLI, embedded, rescue |
| **xfce** | `iso-profiles/xfce` | + XFCE | Desktop, text installer |
| **hierapolis** | `iso-profiles/hierapolis` | + Hierapolis DE (glassmorphism) | Full custom DE experience |

---

## Live ISO Features

- **`hierapolis-install`** — Text installer (run as root): disk → LUKS → pacstrap → systemd-boot/GRUB, with an optional Hierapolis DE install
- **`vpm`** — Hierapolis Package Manager (pacman wrapper: `sudo vpm -S fastfetch`)
- **Offline `[hierapolis]` repo** — custom packages are bundled in the ISO (`/opt/hierapolis/repo`)
- **Calamares GUI** — temporarily on hold: Arch dropped `calamares` from its repos, so the ISO ships the text installer until we package Calamares ourselves
- **Turkey-first mirrors** — Veriteknik, Uber, NetCologne, 23media...
- **AUR ready** — install `yay`/`paru` post-install (not shipped in the ISO)

---

## Custom Packages (in `[hierapolis]` repo)

| Package | Contents |
|---------|----------|
| `hierapolis-keyring` | PGP keys for repo signing |
| `hierapolis-mirrorlist` | Turkey-optimized `/etc/pacman.d/mirrorlist` |
| `hierapolis-installer` | `/usr/bin/hierapolis-install` |
| `hierapolis-desktop-settings` | XFCE + LightDM configs |
| `hierapolis-artwork` | Wallpapers, logos, boot splash, GRUB theme, Plymouth |
| `hierapolis-calamares` | Calamares branding + modules (kept for later; not built — `calamares` is no longer in the Arch repos) |
| `hierapolis-vpm` | `/usr/bin/vpm` — pacman wrapper |
| `hierapolis-shell` | Panel + start menu (Hierapolis DE, GTK4 layer-shell) |
| `hierapolis-settings` | Settings application (Hierapolis DE, GTK4/libadwaita) |
| `hierapolis-theme` | Glassmorphism GTK4 theme + wallpapers/icons (Hierapolis DE) |
| `hierapolis-session` | Session integration + labwc config (Hierapolis DE) |
| `hierapolis-de-meta` | Meta-package pulling full Hierapolis DE |

---

## Hierapolis DE (Desktop Environment)

The in-house DE is built on **labwc** (Wayland compositor) with a **GTK4 layer-shell panel** and a **Windows 8.1-style full-screen start menu**.

### Start menu
- **Full-screen live-tile overlay** (Win 8.1 Metro look), optional compact mode
- **Tile sizes**: small, medium, wide, large — right-click any tile to change size
- **Named groups** (Play / Explore / Create / System) with per-group colors
- **Live tiles** with rotating content
- Search filters tiles as you type; Esc closes the menu
- Group buttons filter the grid ("All" shows everything)

### Customization (everything is config-driven)

| File | Purpose |
|------|---------|
| `~/.config/hierapolis-shell/config.json` | App tiles, groups, colors, panel metrics, theme |
| `~/.config/hierapolis-shell/user.css` | Arbitrary GTK4 CSS override (wins over built-in styles) |

**Settings app** (`hierapolis-settings`) has live editors:
- **Appearance** — variant (dark/light/glass), accent color, glass intensity, corner radius, panel height/margin
- **Start Menu** — fullscreen toggle, columns, tile spacing, group add/remove/color, per-tile size/group/live, add/remove app tiles

All changes save immediately to `config.json`; restart `hierapolis-shell` (or log out/in) to apply.

---

## Testing in QEMU (nested KVM works in VMware)

```bash
# CLI/TTY ISO (2G RAM)
qemu-system-x86_64 -cdrom iso-profiles/tty/out/hierapolis-*.iso -m 2G -enable-kvm

# XFCE ISO (4G RAM, GPU accel)
qemu-system-x86_64 -cdrom iso-profiles/xfce/out/hierapolis-xfce-*.iso -m 4G -enable-kvm -display gtk,gl=on

# Hierapolis DE ISO (4G RAM, Wayland)
qemu-system-x86_64 -cdrom iso-profiles/hierapolis/out/hierapolis-de-*.iso -m 4G -enable-kvm -display gtk,gl=on
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `mkarchiso: not found` | `pacman -S archiso` |
| `KVM not supported` | VMware Settings → Processors → **Virtualize Intel VT-x/EPT / AMD-V/RVI** |
| Package missing in `[hierapolis]` | Re-run `build-repo.sh`, check `pacman -Sl hierapolis` |
| `rsvg-convert: not found` | `pacman -S librsvg` (now auto-installed by `build-repo.sh`) |
| Calamares unavailable | Expected for now — `calamares` was removed from the Arch repos; use `hierapolis-install` |
| `vpm: command not found` | Install `hierapolis-vpm` package, or use `pacman` directly |
| `hierapolis-install` not found | It is installed by the `hierapolis-installer` package (`packages/core/hierapolis-installer/hierapolis-install`) |
| GitHub Actions build fails | Ensure `librsvg` and `archiso` are in CI dependencies |

---

## Next Milestones

1. ✅ CLI/TTY bootable ISO (this build)
2. ✅ GRUB glassmorphism theme
3. ✅ SVG→PNG auto-conversion in PKGBUILDs
4. ✅ VPM (Hierapolis Package Manager) wrapper
5. ✅ Custom Hierapolis DE (shell + settings + glassmorphism + labwc session)
6. ✅ CI/CD (GitHub Actions builds ISOs on tag / manual dispatch)
7. 🔲 Real hardware test (USB → laptop) — after the first CI ISO passes (Wish me luck pls)

--
#Am i aura farming chat?
