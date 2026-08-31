# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_html = """
<div id="confirm-modal-overlay" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center;">
  <div class="confirm-modal" style="background:#fff; border-radius:12px; width:600px; max-width:90vw; padding:24px; box-shadow:0 10px 25px rgba(0,0,0,0.2);">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:20px;">
      <div style="display:flex; gap:12px; align-items:center;">
        <div style="width:40px; height:40px; border-radius:8px; background:#fff2e5; display:flex; align-items:center; justify-content:center; color:var(--accent);">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
        </div>
        <div>
          <h2 style="margin:0; font-size:18px; color:var(--navy-900);">Confirm &amp; Run Analysis</h2>
          <div style="font-size:13px; color:var(--ink-secondary); margin-top:2px;">Patient Cohort &bull; McKesson Compile</div>
        </div>
      </div>
      <button id="close-modal-btn" style="background:transparent; border:none; cursor:pointer; font-size:20px; color:var(--ink-muted);">&times;</button>
    </div>
    
    <div style="border-top:1px solid var(--border); padding-top:20px;">
      <div style="font-weight:600; font-size:14px; margin-bottom:12px; color:var(--ink-primary);">Active Business Rules (<span id="modal-rule-count">0</span>)</div>
      
      <div style="border:1px solid var(--border); border-radius:8px; overflow:hidden;">
        <table style="width:100%; border-collapse:collapse;">
          <thead style="background:#f9fafb;">
            <tr>
              <th style="text-align:left; padding:12px; font-size:13px; font-weight:600; color:var(--ink-primary); border-bottom:1px solid var(--border);">Parameter</th>
              <th style="text-align:left; padding:12px; font-size:13px; font-weight:600; color:var(--ink-primary); border-bottom:1px solid var(--border);">Value</th>
            </tr>
          </thead>
          <tbody id="modal-rule-tbody">
          </tbody>
        </table>
      </div>
    </div>
    
    <div style="display:flex; justify-content:flex-end; gap:12px; margin-top:24px; padding-top:24px; border-top:1px solid var(--border);">
      <button id="cancel-modal-btn" class="btn btn-ghost" style="color:var(--ink-secondary);">Go Back</button>
      <button id="confirm-modal-btn" class="btn" style="background:#2e8555; color:#fff; display:flex; align-items:center; gap:6px;">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
        Run Analysis
      </button>
    </div>
  </div>
</div>
</body>
"""

html = html.replace('</body>', modal_html)

old_js = "confirmBtn.onclick = ()=> onConfirm(rulesArr.filter(r=>r.active));"

new_js = """
  confirmBtn.onclick = ()=> {
    const activeRules = rulesArr.filter(r=>r.active);
    const overlay = document.getElementById('confirm-modal-overlay');
    const tbody = document.getElementById('modal-rule-tbody');
    const count = document.getElementById('modal-rule-count');
    
    tbody.innerHTML = '';
    count.textContent = activeRules.length;
    
    activeRules.forEach(r => {
        const tr = document.createElement('tr');
        const tdParam = document.createElement('td');
        tdParam.style.cssText = "padding:12px; font-size:13px; color:var(--ink-primary); font-weight:600; border-bottom:1px solid var(--border);";
        tdParam.textContent = r.category;
        const tdValue = document.createElement('td');
        tdValue.style.cssText = "padding:12px; font-size:13px; color:var(--ink-secondary); border-bottom:1px solid var(--border);";
        tdValue.textContent = r.text;
        tr.appendChild(tdParam);
        tr.appendChild(tdValue);
        tbody.appendChild(tr);
    });
    
    overlay.style.display = 'flex';
    
    const closeHandler = () => { overlay.style.display = 'none'; };
    document.getElementById('close-modal-btn').onclick = closeHandler;
    document.getElementById('cancel-modal-btn').onclick = closeHandler;
    
    document.getElementById('confirm-modal-btn').onclick = () => {
        overlay.style.display = 'none';
        onConfirm(activeRules);
    };
  };
"""

html = html.replace(old_js, new_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
