with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'switch: {' in line:
        start = i
        break

for i in range(start, start+40):
    if i < len(lines):
        print(f"{i+1}: {lines[i].strip()}")
