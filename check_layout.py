with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if any(cls in line for cls in ['.explore-grid', '#chat-panel', '#right-panel', '.stepper', '.rule-row', '.landing-hero', 'padding']):
        print(f"{i+1}: {line.strip()}")
