import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # Header changes
    (r'\.app-header\{[^}]*\}', '.app-header{\n  display:flex;align-items:center;justify-content:space-between;\n  padding:12px 24px;background:var(--surface);color:var(--foreground);flex:none;\n  border-bottom:1px solid var(--border);\n}'),
    (r'\.crumb\{[^}]*\}', '.crumb{font-size:13px;color:var(--ink-secondary);display:flex;align-items:center;gap:6px;margin-left:6px;padding-left:14px;border-left:1px solid var(--border);}'),
    (r'\.crumb b\{[^}]*\}', '.crumb b{color:var(--ink-primary);font-weight:600;}'),
    
    # Toggle switch to blue instead of orange
    (r'\.toggle\.on\{[^}]*\}', '.toggle.on{background:var(--primary);}'),
    
    # AI and User chat bubbles / avatars to match the clean look
    (r'\.chat-head \.ai-avatar\{[^}]*\}', '.chat-head .ai-avatar{width:32px;height:32px;border-radius:9px;background:var(--primary-light);display:flex;align-items:center;justify-content:center;color:#fff;font-size:12px;font-weight:800;}'),
    (r'\.avatar\.ai-avatar\{[^}]*\}', '.avatar.ai-avatar{width:26px;height:26px;border-radius:8px;background:var(--primary-light);flex:none;display:flex;align-items:center;justify-content:center;font-size:9.5px;font-weight:800;color:#fff;}'),
    
    # Change chip primary to blue instead of orange
    (r'\.chip-primary\{[^}]*\}', '.chip-primary{background:var(--primary);color:#fff;}'),
    (r'\.chip-primary:hover\{[^}]*\}', '.chip-primary:hover{background:var(--primary-dark);}'),
    (r'\.chip\{[^}]*\}', '.chip{\n  border:1px solid var(--primary);color:var(--primary);\n  background:#fff;\n  border-radius:999px;padding:8px 13px;font-size:12.5px;font-weight:600;cursor:pointer;\n  transition:background .15s ease, color .15s ease;text-align:left;\n}'),
    (r'\.chip:hover\{[^}]*\}', '.chip:hover{background:var(--surface);}'),
    
    # Change the step active and done colors
    (r'\.step\.done \.dot\{[^}]*\}', '.step.done .dot{background:var(--primary);border-color:var(--primary);color:#fff;}'),
    (r'\.step\.active \.dot\{[^}]*\}', '.step.active .dot{background:var(--accent);border-color:var(--accent);color:#fff;box-shadow:0 0 0 4px rgba(232, 145, 58, 0.12);}'),
    (r'\.step\.done\{[^}]*\}', '.step.done{color:var(--primary);}'),
    (r'\.step\.active\{[^}]*\}', '.step.active{color:var(--accent);}'),
    (r'\.step-line\.done\{[^}]*\}', '.step-line.done{background:var(--primary);}'),
    
    # Rule tag (e.g. DIAGNOSIS)
    (r'\.rule-tag\{[^}]*\}', '.rule-tag{\n  font-size:10.5px;font-weight:700;letter-spacing:0.3px;text-transform:uppercase;color:var(--primary);\n  background:rgba(15, 109, 142, 0.1);border-radius:6px;padding:5px 7px;text-align:center;height:fit-content;\n}')
]

for old, new in replacements:
    html = re.sub(old, new, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
