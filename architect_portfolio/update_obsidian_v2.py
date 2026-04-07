import re
filename = 'obsidian_pavilion.html'
with open(filename, 'r') as f:
    content = f.read()

# Force the toggle button insertion
if 'theme-toggle' not in content:
    content = content.replace('<span class=\"material-symbols-outlined text-black dark:text-white\" data-icon=\"menu\">menu</span>',
                               '<button class=\"theme-toggle material-symbols-outlined text-black dark:text-white hover:opacity-70 transition-opacity mr-4\">contrast</button>\n<span class=\"material-symbols-outlined text-black dark:text-white\" data-icon=\"menu\">menu</span>')

with open(filename, 'w') as f:
    f.write(content)
