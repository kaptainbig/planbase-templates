import re
filename = 'obsidian_pavilion.html'
with open(filename, 'r') as f:
    content = f.read()

# Fix Nav Links (they were still #)
content = content.replace('href=\"#\">Home</a>', 'href=\"index.html\">Home</a>')
content = content.replace('href=\"#\">Projects</a>', 'href=\"projects.html\">Projects</a>')
content = content.replace('href=\"#\">About</a>', 'href=\"about.html\">About</a>')

# Add the missing theme toggle button
if 'theme-toggle' not in content:
    content = content.replace('<div class=\"flex items-center gap-6\">',
                               '<div class=\"flex items-center gap-6\">\n<button class=\"theme-toggle material-symbols-outlined text-black dark:text-white hover:opacity-70 transition-opacity\">contrast</button>')
    # If the above doesn't match, try finding the menu button
    if 'theme-toggle' not in content:
        content = content.replace('<span class=\"material-symbols-outlined\" data-icon=\"menu\">menu</span>',
                                   '<button class=\"theme-toggle material-symbols-outlined text-black dark:text-white hover:opacity-70 transition-opacity mr-4\">contrast</button>\n<span class=\"material-symbols-outlined dark:text-white\" data-icon=\"menu\">menu</span>')

with open(filename, 'w') as f:
    f.write(content)
