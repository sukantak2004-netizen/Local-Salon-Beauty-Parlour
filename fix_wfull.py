import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace w-full with mx-auto in the button containers
    content = content.replace('class="flex flex-wrap gap-4 justify-center w-full"', 'class="flex flex-wrap gap-4 justify-center mx-auto"')
    content = content.replace('class="flex flex-wrap gap-4 justify-center w-full mb-16"', 'class="flex flex-wrap gap-4 justify-center mx-auto mb-16"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed w-full and added mx-auto")
