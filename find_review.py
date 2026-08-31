with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'Review & run' in line or 'step1' in line or 'Confirmed business rules' in line:
        print(f"{i+1}: {line.strip()}")
