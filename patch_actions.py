# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_code = """  const card = h("div","card");
  card.innerHTML = '<div class="card-title">Confirmed cohort</div><div class="card-sub" style="margin-bottom:0;"><b>'+fmt(finalCohort.kpis.total)+'</b> plaque psoriasis patients, indexed Jan 2023–Dec 2025, ready for downstream analysis.</div>';
  wrap.appendChild(card);
  renderPanel(wrap);"""

new_code = """  const card = h("div","card");
  card.innerHTML = '<div class="card-title">Confirmed cohort</div><div class="card-sub" style="margin-bottom:0;"><b>'+fmt(finalCohort.kpis.total)+'</b> plaque psoriasis patients, indexed Jan 2023–Dec 2025, ready for downstream analysis.</div>';
  wrap.appendChild(card);
  
  const actionsWrap = h("div");
  actionsWrap.style.marginTop = "24px";
  actionsWrap.innerHTML = 
    <div style="font-weight:600; font-size:14px; margin-bottom:12px; color:var(--ink-primary);">Available Analyses</div>
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;">
      <div class="card" id="btn-start-switch" style="cursor:pointer; margin-bottom:0; padding:20px; transition:all 0.2s; border:1px solid var(--border);">
        <div style="font-weight:700; font-size:14.5px; color:var(--navy-900); margin-bottom:4px;">Switch Analysis</div>
        <div style="font-size:13px; color:var(--ink-secondary); line-height:1.5; margin-bottom:12px;">Track patient switching between therapies</div>
        <div style="color:var(--teal-600); font-size:13px; font-weight:600; display:flex; align-items:center; gap:4px;">Configure &amp; Run &rarr;</div>
      </div>
      <div class="card" id="btn-start-adherence" style="cursor:pointer; margin-bottom:0; padding:20px; transition:all 0.2s; border:1px solid var(--border);">
        <div style="font-weight:700; font-size:14.5px; color:var(--navy-900); margin-bottom:4px;">Adherence Analysis</div>
        <div style="font-size:13px; color:var(--ink-secondary); line-height:1.5; margin-bottom:12px;">Measure how consistently patients take therapy</div>
        <div style="color:var(--teal-600); font-size:13px; font-weight:600; display:flex; align-items:center; gap:4px;">Configure &amp; Run &rarr;</div>
      </div>
      <div class="card" id="btn-start-persistence" style="cursor:pointer; margin-bottom:0; padding:20px; transition:all 0.2s; border:1px solid var(--border);">
        <div style="font-weight:700; font-size:14.5px; color:var(--navy-900); margin-bottom:4px;">Persistence Analysis</div>
        <div style="font-size:13px; color:var(--ink-secondary); line-height:1.5; margin-bottom:12px;">Understand how long patients stay on therapy</div>
        <div style="color:var(--teal-600); font-size:13px; font-weight:600; display:flex; align-items:center; gap:4px;">Configure &amp; Run &rarr;</div>
      </div>
    </div>
  ;
  wrap.appendChild(actionsWrap);
  renderPanel(wrap);
  
  document.getElementById('btn-start-switch').addEventListener('mouseenter', function() { this.style.borderColor = 'var(--teal-600)'; this.style.boxShadow = '0 4px 12px rgba(0,0,0,0.05)'; });
  document.getElementById('btn-start-switch').addEventListener('mouseleave', function() { this.style.borderColor = 'var(--border)'; this.style.boxShadow = 'var(--shadow-sm)'; });
  document.getElementById('btn-start-switch').onclick = () => { userSay("Let's start with switch analysis."); startAnalysisFlow("switch"); };
  
  document.getElementById('btn-start-adherence').addEventListener('mouseenter', function() { this.style.borderColor = 'var(--teal-600)'; this.style.boxShadow = '0 4px 12px rgba(0,0,0,0.05)'; });
  document.getElementById('btn-start-adherence').addEventListener('mouseleave', function() { this.style.borderColor = 'var(--border)'; this.style.boxShadow = 'var(--shadow-sm)'; });
  document.getElementById('btn-start-adherence').onclick = () => { userSay("Let's start with adherence analysis."); startAnalysisFlow("adherence"); };
  
  document.getElementById('btn-start-persistence').addEventListener('mouseenter', function() { this.style.borderColor = 'var(--teal-600)'; this.style.boxShadow = '0 4px 12px rgba(0,0,0,0.05)'; });
  document.getElementById('btn-start-persistence').addEventListener('mouseleave', function() { this.style.borderColor = 'var(--border)'; this.style.boxShadow = 'var(--shadow-sm)'; });
  document.getElementById('btn-start-persistence').onclick = () => { userSay("Let's start with persistence analysis."); startAnalysisFlow("persistence"); };"""

html = html.replace(old_code, new_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
