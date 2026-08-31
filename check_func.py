with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
match = re.search(r'function rulesEditorCard.*?return card;\n}', html, re.DOTALL)
if match:
    print(match.group(0).encode('cp1252', 'ignore').decode('cp1252'))
