import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change DY to U
html = html.replace('<div class="avatar-badge">DY</div>', '<div class="avatar-badge">U</div>')

# Change logo size in landing page
html = html.replace('<div class="brand-lockup">\n      <img src="Tredence_KMK_Logo-removebg-preview.png" alt="Tredence KMK Logo" style="height: 80px; object-fit: contain;">\n    </div>', '<div class="brand-lockup">\n      <img src="Tredence_KMK_Logo-removebg-preview.png" alt="Tredence KMK Logo" style="height: 55px; object-fit: contain;">\n    </div>')

# Change logo size in explore header
html = html.replace('<div class="brand-lockup" id="btn-home">\n        <img src="Tredence_KMK_Logo-removebg-preview.png" alt="Tredence KMK Logo" style="height: 80px; object-fit: contain;">\n      </div>', '<div class="brand-lockup" id="btn-home">\n        <img src="Tredence_KMK_Logo-removebg-preview.png" alt="Tredence KMK Logo" style="height: 35px; object-fit: contain;">\n      </div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
