import re
import os

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # Find all project card containers and wrap them in <a> tags
    # This matches common patterns for project cards in the files

    # 1. index.html patterns
    # Match large item and smaller items in index.html
    # Look for <div> containing an image and h3
    content = re.sub(r'(<div class="md:col-span-(?:8|4) group cursor-pointer(?: md:[^"]+)?"\s*>)(.*?)(</div>\s*</div>)',
                     r'\1<a href="obsidian_pavilion.html">\2\3</a>', content, flags=re.DOTALL)

    # 2. projects.html patterns
    # Match group cursor-pointer and its content
    content = re.sub(r'(<div class="(?:md:col-span-\d+|group) cursor-pointer(?: md:[^"]+)?"\s*>)(.*?)(</div>\s*</div>)',
                     r'\1<a href="obsidian_pavilion.html">\2\3</a>', content, flags=re.DOTALL)

    # Clean up double <a> tags if any were already linked
    content = re.sub(r'<a href="obsidian_pavilion.html">\s*<a href="obsidian_pavilion.html">',
                     r'<a href="obsidian_pavilion.html">', content)
    content = re.sub(r'</a>\s*</a>', r'</a>', content)

    with open(filename, 'w') as f:
        f.write(content)

process_file('index.html')
process_file('projects.html')
