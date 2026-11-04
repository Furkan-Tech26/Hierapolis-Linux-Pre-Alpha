# Hierapolis Linux — root login shell on the live medium
#
# tty1 auto-logs in as root (see the getty@tty1 override) and this profile
# starts the Hierapolis desktop straight away, so the live ISO boots into the DE
# instead of a bare prompt.
#
# The desktop is started as a child, never with exec: if labwc or hierapolis-shell
# fails, its output stays on the console and this shell remains available for
# recovery. Set HIERAPOLIS_NO_DE=1 to skip the autostart at boot.
#
# The guard is /run/archiso rather than its bootmnt subdirectory: with
# copytoram=auto archiso unmounts that mountpoint after copying the image to
# RAM, so a check for it would silently disable the desktop on roomy machines.

if [ -z "${HIERAPOLIS_LIVE_TRIED:-}" ] &&
   [ -z "${HIERAPOLIS_NO_DE:-}" ] &&
   [ -d /run/archiso ] &&
   [ "$(tty 2>/dev/null)" = "/dev/tty1" ] &&
   command -v hierapolis-session >/dev/null 2>&1; then
    export HIERAPOLIS_LIVE_TRIED=1
    printf '\nStarting the Hierapolis desktop (labwc)…\n\n'
    hierapolis-session
    status=$?
    printf '\nThe Hierapolis desktop session has ended (status %s).\n' "$status"
    printf 'Start it again with:  hierapolis-session\n'
    printf 'Install the system with:  hierapolis-install\n\n'
fi

# Normal login-shell behaviour.
[ -f "$HOME/.bashrc" ] && . "$HOME/.bashrc"
