with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(1340, 1420):
    if i < len(lines):
        print(f"{i+1}: {lines[i].strip()}")
