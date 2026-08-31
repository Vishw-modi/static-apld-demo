import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # 1. Grid gap and width
    (r'\.explore-grid\{flex:1;display:grid;grid-template-columns:392px 1fr;min-height:0;\}', '.explore-grid{flex:1;display:grid;grid-template-columns:420px 1fr;gap:24px;min-height:0;padding-right:24px;}'),
    
    # 2. Right panel padding
    (r'\.panel-inner\{padding:26px 32px 60px;max-width:1180px;margin:0 auto;animation:fadeUp \.32s ease both;\}', '.panel-inner{padding:40px 48px 80px;max-width:1240px;margin:0 auto;animation:fadeUp .32s ease both;}'),
    
    # 3. Card padding and margin
    (r'\.card\{background:var\(--surface\);border:1px solid var\(--border\);border-radius:var\(--radius\);box-shadow:var\(--shadow-sm\);padding:20px 22px;margin-bottom:18px;\}', '.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow-sm);padding:28px 32px;margin-bottom:24px;}'),
    
    # 4. Rule row spacing
    (r'\.rule-row\{display:grid;grid-template-columns:120px 1fr 46px 30px;gap:10px;align-items:flex-start;padding:10px;border:1px solid var\(--border\);border-radius:10px;background:#fcfcfb;\}', '.rule-row{display:grid;grid-template-columns:130px 1fr 46px 30px;gap:16px;align-items:flex-start;padding:16px;border:1px solid var(--border);border-radius:10px;background:#fcfcfb; margin-bottom: 8px;}'),
    
    # 5. Stepper spacing
    (r'\.stepper\{\n  display:flex;align-items:center;gap:0;padding:14px 28px;background:#fff;border-bottom:1px solid var\(--border\);flex:none;\n\}', '.stepper{\n  display:flex;align-items:center;gap:0;padding:20px 40px;background:#fff;border-bottom:1px solid var(--border);flex:none;\n}'),
    
    # 6. Chat messages gap & padding
    (r'#chat-messages\{flex:1;overflow-y:auto;padding:18px;display:flex;flex-direction:column;gap:14px;\}', '#chat-messages{flex:1;overflow-y:auto;padding:24px;display:flex;flex-direction:column;gap:20px;}'),
    
    # 7. Chat head padding
    (r'\.chat-head\{padding:16px 18px;border-bottom:1px solid var\(--border\);display:flex;align-items:center;gap:10px;\}', '.chat-head{padding:20px 24px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;}'),
    
    # 8. App header padding
    (r'\.app-header\{\n  display:flex;align-items:center;justify-content:space-between;\n  padding:12px 24px;background:var\(--surface\);color:var\(--foreground\);flex:none;\n  border-bottom:1px solid var\(--border\);\n\}', '.app-header{\n  display:flex;align-items:center;justify-content:space-between;\n  padding:16px 32px;background:var(--surface);color:var(--foreground);flex:none;\n  border-bottom:1px solid var(--border);\n}')
]

for old, new in replacements:
    html = re.sub(old, new, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
