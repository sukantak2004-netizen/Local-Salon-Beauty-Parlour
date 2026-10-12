import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('justify-start hero-bg', 'justify-center lg:justify-start hero-bg')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated flex alignment")
