#!/bin/bash
# Rename Hierapolis -> Hierapolis
# Run from repo root

set -euo pipefail

REPO_ROOT="/home/BabaPro2433/hierapolis-git"
cd "$REPO_ROOT"

echo "=== Starting Hierapolis -> Hierapolis rename ==="

# ============================================================
# PHASE 1: Rename directories (deepest first to avoid path issues)
# ============================================================
echo "=== Phase 1: Renaming directories ==="

# Array of directory renames (deepest first)
dirs=(
    "packages/core/hierapolis-calamares/branding/hierapolis"
    "packages/core/hierapolis-artwork"
    "packages/core/hierapolis-calamares"
    "packages/core/hierapolis-desktop-settings"
    "packages/core/hierapolis-installer"
    "packages/core/hierapolis-keyring"
    "packages/core/hierapolis-mirrorlist"
    "packages/core/hierapolis-vpm"
    "packages/desktop/hierapolis-de-meta"
    "packages/desktop/hierapolis-session"
    "packages/desktop/hierapolis-settings"
    "packages/desktop/hierapolis-shell"
    "packages/desktop/hierapolis-theme"
    "iso-profiles/hierapolis"
)

for dir in "${dirs[@]}"; do
    if [[ -d "$dir" ]]; then
        new_dir="${dir//hierapolis/hierapolis}"
        new_dir="${new_dir//Hierapolis/Hierapolis}"
        echo "  $dir -> $new_dir"
        mkdir -p "$(dirname "$new_dir")"
        mv "$dir" "$new_dir"
    fi
done

# ============================================================
# PHASE 2: Rename files
# ============================================================
echo "=== Phase 2: Renaming files ==="

# Find all files with hierapolis/Hierapolis in name (excluding .git)
find . -type f -not -path "./.git/*" | while IFS= read -r file; do
    basename=$(basename "$file")
    dirname=$(dirname "$file")
    
    new_basename="${basename//hierapolis/hierapolis}"
    new_basename="${new_basename//Hierapolis/Hierapolis}"
    
    if [[ "$basename" != "$new_basename" ]]; then
        new_path="$dirname/$new_basename"
        echo "  $file -> $new_path"
        mv "$file" "$new_path"
    fi
done

# ============================================================
# PHASE 3: Update file contents
# ============================================================
echo "=== Phase 3: Updating file contents ==="

# Case-sensitive replacements:
# Hierapolis -> Hierapolis
# hierapolis -> hierapolis  
# HIERAPOLIS -> HIERAPOLIS
# Hierapolis -> Hierapolis (if any remain)

# Find all text files (exclude binary, .git, build outputs)
find . -type f -not -path "./.git/*" \
    -not -path "*/work/*" \
    -not -path "*/out/*" \
    -not -name "*.pkg.tar.zst" \
    -not -name "*.sig" \
    -not -name "*.pyc" \
    -not -name "*.o" \
    -not -name "*.so" \
    -not -name "*.a" \
    -not -name "*.iso" \
    -not -name "*.img" \
    -not -name "*.vmdk" \
    | while IFS= read -r file; do
    
    # Skip binary files
    if file "$file" | grep -q "text\|empty\|script"; then
        # Use sed with multiple replacements
        sed -i \
            -e 's/Hierapolis Linux/Hierapolis Linux/g' \
            -e 's/Hierapolis Linux/Hierapolis Linux/g' \
            -e 's/Hierapolis/Hierapolis/g' \
            -e 's/hierapolis/hierapolis/g' \
            -e 's/HIERAPOLIS/HIERAPOLIS/g' \
            -e 's/Hierapolis/Hierapolis/g' \
            "$file"
    fi
done

# ============================================================
# PHASE 4: Special fixes
# ============================================================
echo "=== Phase 4: Special fixes ==="

# Fix package names in PKGBUILDs and .install files
find . -type f \( -name "PKGBUILD" -o -name "*.install" \) -not -path "./.git/*" | while IFS= read -r file; do
    sed -i \
        -e 's/pkgname=hierapolis-/pkgname=hierapolis-/g' \
        -e 's/pkgname="hierapolis-/pkgname="hierapolis-/g' \
        -e 's/depends=(\(.*\)hierapolis-/depends=(\1hierapolis-/g' \
        -e 's/makedepends=(\(.*\)hierapolis-/makedepends=(\1hierapolis-/g' \
        -e 's/optdepends=(\(.*\)hierapolis-/optdepends=(\1hierapolis-/g' \
        -e 's/provides=(\(.*\)hierapolis-/provides=(\1hierapolis-/g' \
        -e 's/conflicts=(\(.*\)hierapolis-/conflicts=(\1hierapolis-/g' \
        -e 's/replaces=(\(.*\)hierapolis-/replaces=(\1hierapolis-/g' \
        "$file"
done

# Fix .desktop files
find . -name "*.desktop" -not -path "./.git/*" | while IFS= read -r file; do
    sed -i \
        -e 's/Name=Hierapolis/Name=Hierapolis/g' \
        -e 's/Comment=Hierapolis/Comment=Hierapolis/g' \
        -e 's/Exec=hierapolis/Exec=hierapolis/g' \
        -e 's/Icon=hierapolis/Icon=hierapolis/g' \
        "$file"
done

# Fix specific config paths
find . -type f -not -path "./.git/*" | xargs grep -l "/etc/hierapolis" 2>/dev/null | while IFS= read -r file; do
    sed -i 's|/etc/hierapolis|/etc/hierapolis|g' "$file"
done

find . -type f -not -path "./.git/*" | xargs grep -l "/usr/share/hierapolis" 2>/dev/null | while IFS= read -r file; do
    sed -i 's|/usr/share/hierapolis|/usr/share/hierapolis|g' "$file"
done

find . -type f -not -path "./.git/*" | xargs grep -l "/usr/bin/hierapolis" 2>/dev/null | while IFS= read -r file; do
    sed -i 's|/usr/bin/hierapolis|/usr/bin/hierapolis|g' "$file"
done

# Fix systemd service names
find . -type f -not -path "./.git/*" | xargs grep -l "hierapolis-" 2>/dev/null | while IFS= read -r file; do
    sed -i 's/hierapolis-/hierapolis-/g' "$file"
done

# Fix git repo references in scripts
find . -name "*.sh" -not -path "./.git/*" | while IFS= read -r file; do
    sed -i 's|Hierapolis-Linux|Hierapolis-Linux|g' "$file"
    sed -i 's|hierapolis-linux|hierapolis-linux|g' "$file"
done

# Fix GitHub repo references
find . -type f -not -path "./.git/*" | xargs grep -l "Furkan-Tech26/Hierapolis-Linux" 2>/dev/null | while IFS= read -r file; do
    sed -i 's|Furkan-Tech26/Hierapolis-Linux|Furkan-Tech26/Hierapolis-Linux|g' "$file"
done

# Fix iso-profiles references
find ./iso-profiles -type f -not -path "./.git/*" | while IFS= read -r file; do
    sed -i 's|iso-profiles/hierapolis|iso-profiles/hierapolis|g' "$file"
    sed -i 's|profile-hierapolis|profile-hierapolis|g' "$file"
    sed -i 's|work-hierapolis|work-hierapolis|g' "$file"
done

echo "=== Rename complete ==="
echo "Run: git status to see changes"