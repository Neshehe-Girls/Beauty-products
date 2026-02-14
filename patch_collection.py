#!/usr/bin/env python3
"""
Run this script in the same folder as collection.html to add the Sage & Stitch nav link.
Usage: python3 patch_collection.py
"""
import os, shutil

fname = "collection.html"

if not os.path.exists(fname):
    print(f"ERROR: {fname} not found in current directory.")
    exit(1)

# Backup original
shutil.copy(fname, fname + ".backup")

with open(fname, "r", encoding="utf-8") as f:
    content = f.read()

# The nav ul to find and replace
OLD_NAV = '''        <ul class="nav-menu">
            <li><a href="index.html">Home</a></li>
            <li><a href="collection.html" class="active">Collection</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>'''

NEW_NAV = '''        <ul class="nav-menu">
            <li><a href="index.html">Home</a></li>
            <li><a href="collection.html" class="active">Beauty</a></li>
            <li><a href="sage-stitch.html" style="color:#7C9A6E;font-weight:500">🌿 Sage &amp; Stitch</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>'''

if OLD_NAV in content:
    content = content.replace(OLD_NAV, NEW_NAV)
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print("✅ collection.html updated successfully! Sage & Stitch nav link added.")
    print("   Backup saved as collection.html.backup")
else:
    print("⚠️  Could not find nav pattern. Please add manually:")
    print('   After: <li><a href="collection.html" class="active">Collection</a></li>')
    print('   Add:   <li><a href="sage-stitch.html" style="color:#7C9A6E;font-weight:500">🌿 Sage & Stitch</a></li>')
