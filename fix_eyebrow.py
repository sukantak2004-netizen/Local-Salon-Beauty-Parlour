import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to find the eyebrow div inside the hero section and add mx-auto to its class list.
    # The hero eyebrow usually looks like:
    # <div class="eyebrow mb-6" style="display: inline-flex;">...</div>
    # or <div class="eyebrow mb-8" style="display: inline-flex;">...</div>
    # Let's just find the first eyebrow in the file (which is in the hero section) and add mx-auto if it's not there.
    
    # A robust way is to just replace all instances of <div class="eyebrow inside the hero section,
    # but maybe just adding mx-auto to the very first eyebrow is enough.
    
    # Let's find <div class="eyebrow and replace it with <div class="eyebrow mx-auto for the first occurrence only.
    # Wait, some pages already have <div class="eyebrow mx-auto justify-center">Our Commitment</div> in other sections.
    # So let's replace the first one if it doesn't have mx-auto.
    
    first_eyebrow = re.search(r'<div class="eyebrow[^>]*>', content)
    if first_eyebrow:
        match = first_eyebrow.group(0)
        if 'mx-auto' not in match:
            new_match = match.replace('class="eyebrow', 'class="eyebrow mx-auto')
            content = content.replace(match, new_match, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Eyebrows centered")
