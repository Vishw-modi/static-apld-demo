with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'header-right' in line or 'app-header' in line or 'LIVE DEMO' in line or 'btn-home' in line:
        print(f"{i+1}: {line.strip()}")
