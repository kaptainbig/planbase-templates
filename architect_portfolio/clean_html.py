import os
import re

files = ['index.html', 'about.html', 'projects.html']

def clean_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Fix double classes
    content = re.sub(r'(dark:text-white\s*){2,}', 'dark:text-white ', content)
    content = re.sub(r'(dark:text-neutral-400\s*){2,}', 'dark:text-neutral-400 ', content)

    # Fix multiple class attributes on menu span
    content = content.replace('<span class="material-symbols-outlined" data-icon="menu" class="dark:text-white">',
                              '<span class="material-symbols-outlined dark:text-white" data-icon="menu">')

    # Ensure hero section is responsive
    content = content.replace('h-[921px]', 'h-auto md:h-[921px] py-20 md:py-0')

    with open(filename, 'w') as f:
        f.write(content)

for f in files:
    clean_file(f)
