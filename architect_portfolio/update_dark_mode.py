import os
import re

files = ['index.html', 'about.html', 'projects.html']

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Scripts
    if 'theme-init.js' not in content:
        content = content.replace('<head>', '<head>\n<script src="theme-init.js"></script>')
    if 'theme-toggle.js' not in content:
        content = content.replace('</body>', '<script src="theme-toggle.js"></script>\n</body>')

    # HTML class
    content = content.replace('<html class="light"', '<html')

    # Body
    if 'dark:bg-black' not in content:
        content = content.replace('<body class="', '<body class="dark:bg-black dark:text-white ')

    # Nav
    content = content.replace('bg-[#f9f9f9]/90 backdrop-blur-xl', 'bg-[#f9f9f9]/90 dark:bg-black/80 backdrop-blur-xl')

    # Toggle button update
    content = content.replace('<span class="material-symbols-outlined" data-icon="contrast">contrast</span>',
                               '<span class="theme-toggle material-symbols-outlined cursor-pointer hover:opacity-70 transition-opacity" data-icon="contrast">contrast</span>')

    # Nav links newsreader
    content = content.replace('text-neutral-500 hover:text-black transition-colors duration-300 font-serif font-medium tracking-tight newsreader',
                               'text-neutral-500 dark:text-neutral-400 hover:text-black dark:hover:text-white transition-colors duration-300 font-serif font-medium tracking-tight newsreader')

    # Active links
    content = content.replace('text-black border-b-2 border-black', 'text-black dark:text-white border-b-2 border-black dark:border-white')

    # Global text colors
    content = content.replace('text-primary', 'text-primary dark:text-white')
    content = content.replace('text-on-surface', 'text-on-surface dark:text-white')
    content = content.replace('text-secondary', 'text-secondary dark:text-neutral-400')
    content = content.replace('text-outline', 'text-outline dark:text-neutral-500')

    # Sections
    content = content.replace('bg-surface-container-low', 'bg-surface-container-low dark:bg-neutral-900')
    content = content.replace('bg-surface-container-highest', 'bg-surface-container-highest dark:bg-neutral-800')
    content = content.replace('bg-surface-container', 'bg-surface-container dark:bg-neutral-800')

    # Hamburger menu
    content = content.replace('text-black">menu', 'text-black dark:text-white">menu')
    content = content.replace('data-icon="menu">menu</span>', 'data-icon="menu" class="dark:text-white">menu</span>')

    with open(filename, 'w') as f:
        f.write(content)

for f in files:
    process_file(f)
