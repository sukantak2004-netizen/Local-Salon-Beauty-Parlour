import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix .::after
    content = content.replace('.::after {', '.grain::after {')
    content = content.replace("html[data-theme='dark'] .::after {", "html[data-theme='dark'] .grain::after {")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed")
