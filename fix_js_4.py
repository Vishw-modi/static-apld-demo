with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if 'actionsWrap.innerHTML =' in lines[i]:
        lines[i] = '  actionsWrap.innerHTML = \n'
    if '  ;' in lines[i]:
        lines[i] = '  ;\n'

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
