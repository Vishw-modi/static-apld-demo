with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if 'actionsWrap.innerHTML = \n' in lines[i]:
        lines[i] = lines[i].replace('actionsWrap.innerHTML = \n', 'actionsWrap.innerHTML = \n')
    if '    </div>\n' in lines[i] and '  ;\n' in lines[i+1]:
        lines[i+1] = lines[i+1].replace('  ;\n', '  ;\n')

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
