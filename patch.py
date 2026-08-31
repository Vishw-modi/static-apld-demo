import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'<div class="brand-lockup">.*?</div>\s*</div>', 
    '<div class="brand-lockup">\n      <img src="Tredence_KMK_Logo-removebg-preview.png" alt="Tredence KMK Logo" style="height: 38px; object-fit: contain;">\n    </div>', html, flags=re.DOTALL)

html = re.sub(r'<div class="brand-lockup" id="btn-home">.*?</div>\s*</div>', 
    '<div class="brand-lockup" id="btn-home">\n        <img src="Tredence_KMK_Logo-removebg-preview.png" alt="Tredence KMK Logo" style="height: 38px; object-fit: contain;">\n      </div>', html, flags=re.DOTALL)

replacements = [
    (r'#view-landing\{[^}]*\}', '#view-landing{\n  min-height:100vh;\n  display:flex;\n  flex-direction:column;\n  background: var(--page);\n  color: var(--foreground);\n}'),
    (r'\.landing-nav-links a\{[^}]*\}', '.landing-nav-links a{color:var(--ink-secondary);text-decoration:none;font-size:14px;}'),
    (r'\.pill-tag\{[^}]*\}', '.pill-tag{\n  font-size:11px;letter-spacing:0.5px;text-transform:uppercase;\n  background:var(--teal-100);border:1px solid var(--teal-600);\n  padding:4px 10px;border-radius:999px;color:var(--teal-700);\n}'),
    (r'\.landing-eyebrow\{[^}]*\}', '.landing-eyebrow{display:inline-flex;align-items:center;gap:8px;background:var(--teal-050);border:1px solid var(--teal-100);padding:6px 12px;border-radius:999px;font-size:12.5px;color:var(--teal-700);margin-bottom:22px;}'),
    (r'\.landing-hero h1\{[^}]*\}', '.landing-hero h1{font-size:46px;line-height:1.12;margin:0 0 18px;font-weight:750;letter-spacing:-0.5px; color: var(--navy-900);}'),
    (r'\.landing-hero h1 em\{[^}]*\}', '.landing-hero h1 em{font-style:normal;color:var(--teal-600);}'),
    (r'\.landing-hero p\.lead\{[^}]*\}', '.landing-hero p.lead{font-size:17px;line-height:1.6;color:var(--ink-secondary);max-width:540px;margin:0 0 30px;}'),
    (r'\.btn-secondary\{[^}]*\}', '.btn-secondary{background:#fff;color:var(--ink-primary);border:1px solid var(--border-strong);}'),
    (r'\.btn-secondary:hover\{[^}]*\}', '.btn-secondary:hover{background:var(--surface);}'),
    (r'\.landing-visual\{[^}]*\}', '.landing-visual{\n  background:var(--surface);\n  border:1px solid var(--border);\n  border-radius:18px;padding:22px;backdrop-filter: blur(6px);\n  box-shadow: var(--shadow-md);\n}'),
    (r'\.landing-visual \.vwin-bar span\{[^}]*\}', '.landing-visual .vwin-bar span{width:9px;height:9px;border-radius:50%;background:var(--border-strong);}'),
    (r'\.mini-bubble\{[^}]*\}', '.mini-bubble{background:var(--page);border:1px solid var(--border);padding:10px 13px;border-radius:12px;font-size:12.5px;color:var(--ink-primary);line-height:1.45;}'),
    (r'\.mini-bubble\.me\{[^}]*\}', '.mini-bubble.me{background:var(--teal-050);margin-left:36px;border-color:var(--teal-100);}'),
    (r'\.mini-stat\{[^}]*\}', '.mini-stat{background:var(--page);border:1px solid var(--border);border-radius:10px;padding:10px 12px;}'),
    (r'\.mini-stat b\{[^}]*\}', '.mini-stat b{display:block;font-size:18px;color:var(--ink-primary);}'),
    (r'\.mini-stat span\{[^}]*\}', '.mini-stat span{font-size:10.5px;color:var(--ink-secondary);text-transform:uppercase;letter-spacing:0.4px;}'),
    (r'\.landing-foot\{[^}]*\}', '.landing-foot{padding:16px 40px;text-align:center;font-size:12px;color:var(--ink-muted);}'),
    (r'\.module-tile\{[^}]*\}', '.module-tile{\n  border:1px solid var(--border);background:var(--surface);\n  border-radius:10px;padding:10px 14px;font-size:12.5px;color:var(--ink-secondary);\n}'),
    (r'\.module-tile\.active\{[^}]*\}', '.module-tile.active{border-color:var(--teal-500);background:var(--teal-050);color:var(--teal-700);}')
]

for old, new in replacements:
    html = re.sub(old, new, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
