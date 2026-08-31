import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_code = """function showAnalysisResults(key){
  renderStepper(3, STATE.completedAnalyses);
  const wrap = h("div");
  wrap.appendChild(h("div","panel-eyebrow","Step 3 · Deep-Dive Analysis"));
  wrap.appendChild(h("div","panel-title", ANALYSIS_META[key].label+" results"));
  wrap.appendChild(h("div","panel-subtitle","Behind the scenes, APLD ran the confirmed rules across the systemic-therapy population within your PsO cohort."));
  wrap.appendChild(analysisTabsBar(key));

  if(key==="switch") wrap.appendChild(switchResultsBlock());
  if(key==="adherence") wrap.appendChild(adherenceResultsBlock());
  if(key==="persistence") wrap.appendChild(persistenceResultsBlock());

  const remaining = ["switch","adherence","persistence"].filter(k=>!STATE.completedAnalyses.includes(k));
  const nextCard = h("div","card");
  if(remaining.length){
    nextCard.innerHTML = '<div class="card-title">What\\'s next?</div><div class="card-sub" style="margin-bottom:14px;">You can look at another analysis on this same cohort, or wrap up with a combined summary.</div>';
    const row = h("div","btn-row");
    remaining.forEach(k=>{
      const b = h("button","btn btn-outline","Run "+ANALYSIS_META[k].label);
      b.onclick = ()=>{ userSay("Let\\'s also look at "+ANALYSIS_META[k].label.toLowerCase()+"."); startAnalysisFlow(k); };
      row.appendChild(b);
    });
    nextCard.appendChild(row);
  } else {
    nextCard.innerHTML = '<div class="card-title">All three analyses complete</div><div class="card-sub" style="margin-bottom:14px;">Switch, adherence, and persistence have all been run on this cohort. Ready for a combined summary tying it back to the original business question?</div>';
    const row = h("div","btn-row");
    const b = h("button","btn btn-tealsolid","Generate combined summary");
    b.onclick = ()=>{ userSay("Generate a combined summary."); showFinalSummary(); };
    row.appendChild(b);
    nextCard.appendChild(row);
  }
  wrap.appendChild(nextCard);
  renderPanel(wrap);

  const s = DATA.switch, a = DATA.adherence, p = DATA.persistence;
  let msg = "";
  if(key==="switch") msg = "Switch analysis is done: <b>"+pct(s.totals.switched, s.totals.population)+"%</b> of patients on a systemic PsO therapy switched classes within 12 months, averaging <b>"+s.totals.avgDaysToSwitch+" days</b> to switch. TNF inhibitors show the highest switch rate; IL-23 inhibitors the lowest.";
  if(key==="adherence") msg = "Adherence analysis is done: mean PDC is <b>"+a.meanPDC+"</b>, with <b>"+a.pctAdherent+"%</b> of patients adherent (PDC ≥0.80). Adherence tracks closely with dosing frequency — less-frequently-dosed IL-23 inhibitors lead.";
  if(key==="persistence") msg = "Persistence analysis is done: median time on therapy is <b>"+p.medianMonths+" months</b>, with <b>"+p.pct12mo+"%</b> of patients still on therapy at 12 months and <b>"+p.pct24mo+"%</b> at 24 months. IL-23 inhibitors again lead; oral systemics trail.";
  aiSay(msg, 1000).then(()=>{
    if(remaining.length){
      setChips(remaining.map((k,i)=>({label:"Run "+ANALYSIS_META[k].label, primary:i===0, onClick: ()=>{ userSay("Let\\'s also look at "+ANALYSIS_META[k].label.toLowerCase()+"."); startAnalysisFlow(k); }})));
      freeTextHandler = ()=> startAnalysisFlow(remaining[0]);
    } else {
      setChips([{label:"Generate combined summary", primary:true, onClick: ()=>{ userSay("Generate a combined summary."); showFinalSummary(); }}]);
      freeTextHandler = ()=> showFinalSummary();
    }
  });
}"""

new_code = """function showAnalysisResults(key, runNum = 1, noAi = false){
  renderStepper(3, STATE.completedAnalyses);
  const wrap = h("div");
  wrap.appendChild(h("div","panel-eyebrow","Step 3 · Deep-Dive Analysis"));
  wrap.appendChild(h("div","panel-title", ANALYSIS_META[key].label+" results"));
  wrap.appendChild(h("div","panel-subtitle","Behind the scenes, APLD ran the confirmed rules across the systemic-therapy population within your PsO cohort."));
  wrap.appendChild(analysisTabsBar(key));

  if(key==="switch") wrap.appendChild(switchResultsBlock());
  if(key==="adherence") wrap.appendChild(adherenceResultsBlock());
  if(key==="persistence") wrap.appendChild(persistenceResultsBlock());

  if (key === "switch" && runNum === 1) {
    const callout = h("div","callout");
    callout.innerHTML = 
      '<div class="callout-head"><div class="callout-icon">!</div><b>A few edge cases worth a look</b></div>'+
      '<ul>'+
      '<li><b>4,200 patients (4.2%)</b> had a switch claim but reversed back to index therapy within 30 days — likely a transient trial/pharmacy issue rather than a true switch.</li>'+
      '<li><b>3,100 patients (3.1%)</b> show a gap of &gt;90 days before the new therapy claim — might be a discontinuation followed by a restart, rather than a direct switch.</li>'+
      '<li><b>2,800 patients (2.8%)</b> had concurrent claims for both therapies for &gt;60 days — might be combination therapy rather than a clear switch.</li>'+
      '</ul>'+
      '<div class="btn-row">'+
      '<button class="btn btn-tealsolid" id="btn-switch-accept-tighten">Apply suggested tightening & re-run</button>'+
      '<button class="link-btn" id="btn-switch-manual">Adjust rules myself</button>'+
      '<button class="link-btn" id="btn-switch-keep-asis">Keep as-is, continue</button>'+
      '</div>';
    wrap.appendChild(callout);
  } else if (key === "switch" && runNum === 2) {
    const callout = h("div","callout teal");
    callout.innerHTML =
      '<div class="callout-head"><div class="callout-icon">✓</div><b>This looks like a clean, analysis-ready switch population</b></div>'+
      '<div style="font-size:13px;color:var(--ink-secondary);line-height:1.6;margin-bottom:14px;">Tightening the switch rules removed transient trial claims and combination therapies, giving a much clearer picture of true therapy switching.</div>'+
      '<div class="btn-row"><button class="btn btn-tealsolid" id="btn-switch-accept-cohort">Accept this analysis & continue</button></div>';
    wrap.appendChild(callout);
  }

  const remaining = ["switch","adherence","persistence"].filter(k=>!STATE.completedAnalyses.includes(k));
  
  if (!(key === "switch" && runNum === 1) && !(key === "switch" && runNum === 2 && !STATE.completedAnalyses.includes("switch"))) {
      const nextCard = h("div","card");
      if(remaining.length){
        nextCard.innerHTML = '<div class="card-title">What\\'s next?</div><div class="card-sub" style="margin-bottom:14px;">You can look at another analysis on this same cohort, or wrap up with a combined summary.</div>';
        const row = h("div","btn-row");
        remaining.forEach(k=>{
          const b = h("button","btn btn-outline","Run "+ANALYSIS_META[k].label);
          b.onclick = ()=>{ userSay("Let\\'s also look at "+ANALYSIS_META[k].label.toLowerCase()+"."); startAnalysisFlow(k); };
          row.appendChild(b);
        });
        nextCard.appendChild(row);
      } else {
        nextCard.innerHTML = '<div class="card-title">All three analyses complete</div><div class="card-sub" style="margin-bottom:14px;">Switch, adherence, and persistence have all been run on this cohort. Ready for a combined summary tying it back to the original business question?</div>';
        const row = h("div","btn-row");
        const b = h("button","btn btn-tealsolid","Generate combined summary");
        b.onclick = ()=>{ userSay("Generate a combined summary."); showFinalSummary(); };
        row.appendChild(b);
        nextCard.appendChild(row);
      }
      wrap.appendChild(nextCard);
  }
  
  renderPanel(wrap);
  
  if (noAi) return;

  if (key === "switch" && runNum === 1) {
    document.getElementById("btn-switch-accept-tighten").onclick = () => acceptSwitchTightening();
    document.getElementById("btn-switch-manual").onclick = () => { renderPanel(analysisRulesPanel(key, ANALYSIS_META[key].rules())); toast("Manual editing re-opened — adjust and confirm to re-run."); };
    document.getElementById("btn-switch-keep-asis").onclick = () => proceedAfterSwitchRun1();
    
    const s = DATA.switch;
    let msg = "Switch analysis is done: <b>"+pct(s.totals.switched, s.totals.population)+"%</b> of patients switched. However, I noticed a few edge cases (like transient 30-day trial claims or combination therapy). Want me to tighten the switch definitions and re-run?";
    aiSay(msg, 1000).then(()=>{
        setChips([
           {label:"Apply suggested tightening & re-run", primary:true, onClick: acceptSwitchTightening},
           {label:"Keep as-is, continue", muted:true, onClick: proceedAfterSwitchRun1}
        ]);
        freeTextHandler = acceptSwitchTightening;
    });
  } else if (key === "switch" && runNum === 2 && !STATE.completedAnalyses.includes("switch")) {
    document.getElementById("btn-switch-accept-cohort").onclick = () => proceedAfterSwitchRun1(true);
    const s = DATA.switch;
    let msg = "The refined switch analysis is ready. We removed the edge cases to get a much cleaner view of switching behavior.";
    aiSay(msg, 1000).then(()=>{
        setChips([
           {label:"Accept this analysis & continue", primary:true, onClick: ()=> proceedAfterSwitchRun1(true)}
        ]);
        freeTextHandler = ()=> proceedAfterSwitchRun1(true);
    });
  } else {
      const s = DATA.switch, a = DATA.adherence, p = DATA.persistence;
      let msg = "";
      if(key==="switch") msg = "Switch analysis is done: <b>"+pct(s.totals.switched, s.totals.population)+"%</b> of patients on a systemic PsO therapy switched classes within 12 months, averaging <b>"+s.totals.avgDaysToSwitch+" days</b> to switch. TNF inhibitors show the highest switch rate; IL-23 inhibitors the lowest.";
      if(key==="adherence") msg = "Adherence analysis is done: mean PDC is <b>"+a.meanPDC+"</b>, with <b>"+a.pctAdherent+"%</b> of patients adherent (PDC ≥0.80). Adherence tracks closely with dosing frequency — less-frequently-dosed IL-23 inhibitors lead.";
      if(key==="persistence") msg = "Persistence analysis is done: median time on therapy is <b>"+p.medianMonths+" months</b>, with <b>"+p.pct12mo+"%</b> of patients still on therapy at 12 months and <b>"+p.pct24mo+"%</b> at 24 months. IL-23 inhibitors again lead; oral systemics trail.";
      aiSay(msg, 1000).then(()=>{
        if(remaining.length){
          setChips(remaining.map((k,i)=>({label:"Run "+ANALYSIS_META[k].label, primary:i===0, onClick: ()=>{ userSay("Let\\'s also look at "+ANALYSIS_META[k].label.toLowerCase()+"."); startAnalysisFlow(k); }})));
          freeTextHandler = ()=> startAnalysisFlow(remaining[0]);
        } else {
          setChips([{label:"Generate combined summary", primary:true, onClick: ()=>{ userSay("Generate a combined summary."); showFinalSummary(); }}]);
          freeTextHandler = ()=> showFinalSummary();
        }
      });
  }
}

async function acceptSwitchTightening() {
  setChips([]); freeTextHandler = null;
  userSay("Apply the suggested tightening and re-run.");
  
  const s = DATA.switch;
  s.totals.switched -= 1200;
  s.totals.remained += 900;
  s.totals.discontinued += 300;
  s.totals.pctMoaSwitch += 3;
  
  await runAnalysis("switch", 2);
}

function proceedAfterSwitchRun1(isRun2 = false) {
  setChips([]); freeTextHandler = null;
  if (!isRun2) userSay("Keep as-is and continue.");
  else userSay("Accept this analysis and continue.");
  
  if(!STATE.completedAnalyses.includes("switch")) STATE.completedAnalyses.push("switch");
  
  showAnalysisResults("switch", 3, true);
  
  const remaining = ["switch","adherence","persistence"].filter(k=>!STATE.completedAnalyses.includes(k));
  let msg = "Got it. Switch analysis is locked in. What would you like to explore next?";
  if (remaining.length === 0) msg = "Got it. All three analyses are complete. Ready for a combined summary?";
  
  aiSay(msg, 900).then(()=>{
      if(remaining.length){
          setChips(remaining.map((k,i)=>({label:"Run "+ANALYSIS_META[k].label, primary:i===0, onClick: ()=>{ userSay("Let\\'s also look at "+ANALYSIS_META[k].label.toLowerCase()+"."); startAnalysisFlow(k); }})));
          freeTextHandler = ()=> startAnalysisFlow(remaining[0]);
      } else {
          setChips([{label:"Generate combined summary", primary:true, onClick: ()=>{ userSay("Generate a combined summary."); showFinalSummary(); }}]);
          freeTextHandler = ()=> showFinalSummary();
      }
  });
}"""

html = html.replace(old_code, new_code)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
