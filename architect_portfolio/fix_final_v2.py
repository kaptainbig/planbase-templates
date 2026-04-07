import re
import os

files = ['index.html', 'about.html', 'projects.html', 'obsidian_pavilion.html']

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Ensure Logo is a link
    content = re.sub(r'<div class="text-(lg|2xl) font-(bold|serif) tracking-tighter uppercase dark:text-white text-black( manrope)?">',
                     r'<a href="index.html" class="text-\1 font-\2 tracking-tighter uppercase dark:text-white text-black\3">', content)
    content = content.replace('</div>', '</a>', 1) # This is a bit risky but we know the logo is usually the first div in nav

    # 2. Add Hamburger Button if missing
    if 'menu-toggle' not in content:
        # Look for the theme toggle area or end of nav links
        content = content.replace('<div class="flex items-center">',
                                   '<div class="flex items-center gap-4">\n<button class="menu-toggle md:hidden material-symbols-outlined text-black dark:text-white">menu</button>')
        # For obsidian which has a different structure
        if 'menu-toggle' not in content:
            content = content.replace('<div class="flex items-center gap-6">',
                                       '<div class="flex items-center gap-6">\n<button class="menu-toggle md:hidden material-symbols-outlined text-black dark:text-white">menu</button>')

    with open(filename, 'w') as f:
        f.write(content)

for f in files:
    process_file(f)
