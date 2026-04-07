import re
filename = 'obsidian_pavilion.html'
with open(filename, 'r') as f:
    content = f.read()

# Replace the specific block
content = re.sub(r'<div class="flex items-center">.*?<span class="material-symbols-outlined text-black dark:text-white" data-icon="menu">menu</span>.*?</div>',
                 '<div class="flex items-center">\n<button class="theme-toggle material-symbols-outlined text-black dark:text-white hover:opacity-70 transition-opacity mr-4">contrast</button>\n<span class="material-symbols-outlined text-black dark:text-white" data-icon="menu">menu</span>\n</div>',
                 content, flags=re.DOTALL)

with open(filename, 'w') as f:
    f.write(content)
