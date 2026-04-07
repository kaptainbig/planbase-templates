import re
import os

files = ['index.html', 'about.html', 'projects.html', 'obsidian_pavilion.html']

mobile_menu_html = """
<!-- Mobile Menu Overlay -->
<div id="mobile-menu" class="fixed inset-0 z-[100] bg-surface dark:bg-black translate-x-full transition-transform duration-500 ease-in-out md:hidden">
    <div class="flex justify-between items-center px-8 py-6 border-b border-outline-variant/10">
        <div class="text-lg font-bold tracking-tighter uppercase dark:text-white text-black manrope">MENU</div>
        <button class="menu-close material-symbols-outlined text-black dark:text-white text-3xl">close</button>
    </div>
    <nav class="flex flex-col gap-8 p-12 items-center text-center">
        <a class="text-2xl newsreader dark:text-white" href="index.html">Home</a>
        <a class="text-2xl newsreader dark:text-white" href="projects.html">Projects</a>
        <a class="text-2xl newsreader dark:text-white" href="about.html">About</a>
        <a class="text-2xl newsreader dark:text-white" href="about.html">Contact</a>
        <div class="mt-12">
            <button class="theme-toggle material-symbols-outlined text-black dark:text-white text-4xl">contrast</button>
        </div>
    </nav>
</div>
"""

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Add mobile-menu.js script
    if 'mobile-menu.js' not in content:
        content = content.replace('</body>', '<script src="mobile-menu.js"></script>\n</body>')

    # 2. Add Mobile Menu HTML after opening body
    if 'id="mobile-menu"' not in content:
        content = re.sub(r'(<body.*?>)', r'\1' + mobile_menu_html, content, flags=re.DOTALL)

    # 3. Update Logos to link to Home
    content = content.replace('<div class="text-lg font-bold tracking-tighter uppercase dark:text-white text-black manrope">ARCHITECTS MONOLITH</div>',
                               '<a href="index.html" class="text-lg font-bold tracking-tighter uppercase dark:text-white text-black manrope">ARCHITECTS MONOLITH</a>')
    content = content.replace('<div class="text-2xl font-serif tracking-tighter text-black dark:text-white uppercase">STUDIO</div>',
                               '<a href="index.html" class="text-2xl font-serif tracking-tighter text-black dark:text-white uppercase">STUDIO</a>')

    # 4. Update Hamburger Button to be functional
    content = content.replace('data-icon="menu">menu</span>', 'class="menu-toggle cursor-pointer dark:text-white" data-icon="menu">menu</span>')
    content = content.replace('<button class="md:hidden">', '<button class="menu-toggle md:hidden">')

    with open(filename, 'w') as f:
        f.write(content)

for f in files:
    process_file(f)
