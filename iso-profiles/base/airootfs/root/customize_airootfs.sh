#!/usr/bin/env bash
# Hierapolis Linux — runs inside the ISO root after pacstrap (archiso).
# Keep it idempotent and non-interactive.

set -euo pipefail

# Live medium: root is passwordless (see /etc/shadow in airootfs)
passwd -d root

# Locales declared in /etc/locale.gen
locale-gen

# Timezone
ln -sf /usr/share/zoneinfo/UTC /etc/localtime

# Pacman keyring (archlinux-keyring is in the package list)
pacman-key --init
pacman-key --populate archlinux

# Regenerate the initramfs so the archiso hook drop-in is guaranteed to be
# picked up even if the kernel package's install hook ran before it existed.
mkinitcpio -P

# Make sure the live environment can use the bundled [hierapolis] repo even if a
# package reinstalled /etc/pacman.conf during pacstrap.
cat > /etc/pacman.d/mirrorlist-core <<'EOF'
# Hierapolis Linux [hierapolis] repository — bundled inside the live ISO
Server = file:///opt/hierapolis/repo
EOF

# Write the final live pacman.conf explicitly. pacstrap may have replaced the
# airootfs copy with the stock one (which would drop multilib and [hierapolis]), so
# do not depend on which file survived.
cat > /etc/pacman.conf <<'EOF'
#
# /etc/pacman.conf — Hierapolis Linux live medium
#

[options]
Architecture = auto
Color
ParallelDownloads = 8
CheckSpace
SigLevel    = Required DatabaseOptional
LocalFileSigLevel = Optional

[core]
Include = /etc/pacman.d/mirrorlist

[extra]
Include = /etc/pacman.d/mirrorlist

[multilib]
Include = /etc/pacman.d/mirrorlist

[hierapolis]
SigLevel = Optional TrustAll
Include = /etc/pacman.d/mirrorlist-core
EOF

# Network on the live medium
systemctl enable NetworkManager.service
