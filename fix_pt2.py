import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace <div class="flex flex-wrap gap-4 justify-center w-full pt-2">
    # with <div class="flex flex-wrap gap-4 justify-center w-full">
    
    content = content.replace('w-full pt-2">', 'w-full">')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed pt-2")
