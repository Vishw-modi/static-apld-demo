with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'category:' in line and 'text:' in line:
        print(f"{i+1}: {line.strip()}")
        break
