import re

with open('pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The grid for memberships: <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
content = content.replace('grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto', 'grid-cols-1 lg:grid-cols-3 gap-6 max-w-5xl mx-auto')

with open('pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
