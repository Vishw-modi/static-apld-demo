import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'actionsWrap\.innerHTML\s*=\s*\n\s*<div', 'actionsWrap.innerHTML = \\n    <div', html)
html = re.sub(r'    </div>\n\s*;\n\s*wrap\.appendChild\(actionsWrap\);', '    </div>\\n  ;\\n  wrap.appendChild(actionsWrap);', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
