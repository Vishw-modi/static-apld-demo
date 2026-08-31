with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if any(keyword in line for keyword in ['confirm', 'Confirm', 'Run Analysis', 'modal', 'overlay']):
        print(f"{i+1}: {line.strip()}")
