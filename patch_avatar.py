import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add user avatar CSS
css_insertion = '.avatar.user-avatar{width:26px;height:26px;border-radius:50%;background:rgba(232, 145, 58, 0.15);flex:none;display:flex;align-items:center;justify-content:center;font-size:10.5px;font-weight:700;color:var(--accent-dark);}\n'
html = html.replace('.avatar.ai-avatar{', css_insertion + '.avatar.ai-avatar{')

# Add user avatar to JS
old_js = 'div.innerHTML = \'<div class="bubble">\'+html+\'</div>\';'
new_js = 'div.innerHTML = \'<div class="bubble">\'+html+\'</div><div class="avatar user-avatar">U</div>\';'
html = html.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
