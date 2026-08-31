import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the links
html = re.sub(r'<a href="#">Product</a>\s*<a href="#">Data Coverage</a>\s*<a href="#">Security</a>', '', html)

# Increase logo size
html = html.replace('style="height: 38px;', 'style="height: 80px;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
