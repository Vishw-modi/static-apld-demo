import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_str = "actionsWrap.innerHTML = \n    <div"
good_str = "actionsWrap.innerHTML = \n    <div"
html = html.replace(bad_str, good_str)

bad_str2 = "    </div>\n  ;\n  wrap.appendChild(actionsWrap);"
good_str2 = "    </div>\n  ;\n  wrap.appendChild(actionsWrap);"
html = html.replace(bad_str2, good_str2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
