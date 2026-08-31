import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('(activeRules)=> confirmCohortRules(activeRules)', '(activeRules)=> runCohortAnalysis(1)')
html = html.replace('(activeRules)=> confirmAnalysisRules(key, activeRules)', '(activeRules)=> runAnalysis(key)')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
