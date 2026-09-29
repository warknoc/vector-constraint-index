import json, re, html
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
raw = (ROOT / "evaluator" / "vci-config.js").read_text()
C = json.loads(raw[raw.index("{"): raw.rindex("}") + 1])
M = C["meta"]
e = html.escape

def ans_tag(kind):
    return f'<span class="tag tag-{kind}">{e(C["verdicts"][kind]["title"])}</span>'

# ---------- sections ----------
cover = f"""
<section class="cover">
  <div class="docline"><span>OPEN DIAGNOSTIC SPECIFICATION</span><span>{e(M['docRef'])} &middot; v{e(M['version'])}</span></div>
  <h1>The Vector-Constraint Index</h1>
  <p class="sub">A deterministic test of whether a problem is actually being solved</p>
  <p class="byline">{e(M['author'])} &middot; {e(M['date'])} &middot; Spec {e(M['license'])}, code MIT &middot; DOI {e(M['doi'])}</p>

  <blockquote class="shirky">
    <p>&ldquo;Institutions will try to preserve the problem to which they are the solution.&rdquo;</p>
    <cite>Clay Shirky. Named the Shirky Principle by Kevin Kelly, 2010.</cite>
  </blockquote>
  <p class="thesis">The Shirky Principle tells you problem preservation exists. The Vector-Constraint Index tells you where.</p>

  <div class="doctrine">
    <h2>Doctrine</h2>
    <ol>
      <li><b>VCI sets no standard.</b> The problem owner's desired outcome is the standard. VCI tests whether a solver is actually delivering it.</li>
      <li><b>The owner is whoever bears the cost of the problem,</b> not whoever funds the solver. Where the two differ, the owner's outcome wins.</li>
      <li><b>Purpose: certify a genuine attempt.</b> Catching handwaving is the byproduct. An honest solver should pass with nothing to fear.</li>
      <li><b>Function, not label.</b> Calling an effort a study, pilot, partnership, or case study changes which rules apply to it, never whether VCI applies.</li>
      <li><b>Burden of proof is on the solver.</b> Every question is answered Yes, No, or Can't show it. Can't show it counts as No.</li>
      <li><b>Verdicts describe structure, not intent.</b> A failed gate means the claim is not supported, not that anyone is lying (Hanlon's Razor). The structural finding is provable from documents. Intent is not.</li>
      <li><b>Deterministic.</b> The same answers always produce the same verdict. Thresholds and question text are published and versioned.</li>
      <li><b>VCI applies to itself and to the evaluator.</b> The evaluator states their own stake before starting. Section 9 runs VCI on VCI.</li>
    </ol>
  </div>
  <p class="status"><b>Status.</b> {e(M['status'])} See the invitation to falsify, next page.</p>
</section>
"""

invite_sec = """
<section class="invite">
<h2 class="sec"><span>RC</span>An invitation to falsify</h2>
<p class="lede">This specification is published as Release Candidate 3 (RC3).</p>
<p>The core mechanics (the Delgado Vector Law, the closure test, the six vector roles, and kill forks K0 to K6) have been run against five cases with known outcomes: smallpox, the 1955 malaria eradication programme, Guinea worm, polio, and the brown tree snake on Guam. In that run the framework broke one of its own assumptions: the brown tree snake's entry routes had not been counted. The fix is now part of the rules. That run was done by the author with outcomes already known. It is not the blind test that freezes v1.0.</p>
<p>No diagnostic tool is finished until it meets the adversarial world. This specification is published under CC BY 4.0, and the evaluator under the MIT License, so that anyone can try to break it. A gap found is the framework getting stronger.</p>
<ol class="inv">
<li><b>Submit an edge case.</b> If you have a proposal, public program, or contract whose lane the closure test cannot resolve, send the public documents.</li>
<li><b>Report a wrong verdict.</b> If an effort that genuinely ended is marked Problem preserved, or an open-ended effort passes the kill forks unchecked, send the case and the evidence.</li>
<li><b>Meet the standard for change.</b> Any change to the core rules must name the documented case that exposed the failure and state the rule that fixes it. It must also rerun every prior benchmark case and report any verdict that changes, with the reason.</li>
</ol>
<div class="rule"><b>Every accepted break is credited by name in the changelog,</b> unless the finder asks to stay anonymous. The first entry is the author's own: the brown tree snake correction in RC2.</div>
<p><b>Where to send it:</b> open an issue on the project repository, or write to andrew.delgado@crea8or1.com with "VCI break" in the subject.</p>
<p class="thesis">The framework does not ask for trust. It asks to be tested.</p>
</section>
"""

defs = """
<section>
<h2 class="sec"><span>1</span>Definitions</h2>
<p class="lede">If problem and solution stay undefined, a preserver redefines them to fit what they are already doing. Every term here is testable.</p>

<div class="defbox">
<h3>Problem</h3>
<p class="def">A measurable gap between the current state and the state the owner wants, which costs the owner something and persists without intervention.</p>
<table class="grid compact">
<tr><th>Element</th><th>Test</th></tr>
<tr><td>Owner</td><td>Someone bears the cost. Where millions do, the measured harm (incidents, losses, exposures) stands in for them. A body claiming to speak for owners counts only if it does not also fund or run the solver.</td></tr>
<tr><td>Current state</td><td>Measured.</td></tr>
<tr><td>Desired state</td><td>Measurable, and set by the owner.</td></tr>
<tr><td>Cost</td><td>What the gap takes from the owner: money, safety, time, health, trust.</td></tr>
<tr><td>Changeability</td><td>Some intervention could, in principle, close it.</td></tr>
</table>
<p>Missing any element means there is no defined problem yet, and nothing can be claimed as solving it. If no intervention could change the gap, it is a <b>condition</b> to plan around, not a problem to fund. The test cuts both ways: it stops fixes being sold for the unfixable, and it catches a solvable problem relabeled as a condition so nobody expects it to end.</p>
</div>

<div class="defbox">
<h3>Supporting terms</h3>
<table class="grid compact">
<tr><td class="k">Symptom</td><td>The observable effect: outages, bites, breaches, cases.</td></tr>
<tr><td class="k">Agent</td><td>The thing that causes the symptom: the snake, the virus, the attacker, the leak.</td></tr>
<tr><td class="k">Vector</td><td>A distinct route by which the agent reaches, moves through, or re-establishes itself in the owner's space. Defined in full below.</td></tr>
<tr><td class="k">Constraint</td><td>What a set of vectors has to pass through. A Terminal solution interdicts it.</td></tr>
<tr><td class="k">Solver</td><td>Whoever claims to be fixing the problem: contractor, agency, researcher, clinician, charity, vendor, program, or yourself.</td></tr>
<tr><td class="k">Resources</td><td>Whatever the solver asks the owner to keep giving: money, time, votes, trust, attention, authority, patience.</td></tr>
<tr><td class="k">Evaluator</td><td>Whoever runs VCI. States their own stake before starting.</td></tr>
</table>
</div>


<div class="defbox" style="page-break-before:always">
<h3 style="margin-top:0">Vector</h3>
<p class="def">A distinct route by which the problem's agent reaches, moves through, or re-establishes itself in the owner's space.</p>
<div class="rule"><b>Closure test (how N is counted).</b> Two routes are the same vector if one interdiction closes both. They are different vectors if closing one leaves the other open. N is the smallest number of independent closures that would shut every route. Routes that share a constraint collapse into one, so the count cannot be padded. A route left open after a closure is by definition its own vector, so the count cannot be shrunk.</div>
<p>Every run answers all six roles in writing, even when the answer is "none." Leaving a role blank is how routes get missed. The worked column is the case that forced this definition.</p>
<table class="grid compact">
<tr><th>Role</th><th>Question</th><th>Brown tree snake on Guam</th></tr>
<tr><td class="k">Source</td><td>Where does the agent come from, and can it be eliminated?</td><td>Native range in New Guinea and nearby islands. Permanent.</td></tr>
<tr><td class="k">Entry</td><td>How does it get inside the boundary?</td><td>Sea cargo, air cargo and aircraft, vessels. Each port or airfield is a door.</td></tr>
<tr><td class="k">Movement</td><td>How does it move once inside?</td><td>Surface contact. One constraint, covering canopy, ground, culverts, and the waterline.</td></tr>
<tr><td class="k">Regeneration</td><td>How does it replace itself inside?</td><td>Eggs in refuges. This is why a full hatch cycle is the clearance clock.</td></tr>
<tr><td class="k">Induced</td><td>What routes does the intervention itself create?</td><td>Displacement into neighboring ground, answered by directing it toward capture.</td></tr>
<tr><td class="k">Adaptive</td><td>Can it invent new routes?</td><td>No record of it.</td></tr>
</table>
<p>A source is not a vector; it is what feeds them. Whether the source can be eliminated decides whether the doors can ever close. How an agent moves and how it gets in are counted separately: a constraint on movement does not close a door.</p>
<table class="grid compact">
<tr><td class="k">Counted vector</td><td>Backed by a record: interceptions, detections, genetic tracing, incident data.</td></tr>
<tr><td class="k">Suspected vector</td><td>Listed separately with the test that would confirm it, and not counted in N until confirmed. This stops a solver inventing vectors to justify open-ended work, and stops anyone waving off a real one.</td></tr>
<tr><td class="k">Not vectors</td><td>Symptoms (outages, bird losses). The agent itself. Conditions of will: no funding, nobody cares. Neglect is a finding against whoever should be acting, never a vector or a lane.</td></tr>
</table>
</div>
<div class="defbox">
<h3>Solution</h3>
<p class="def">An intervention that moves the measured state to the owner's desired state, is shown to be the cause of that change, holds under real conditions, and ends the solver's necessary involvement apart from defined maintenance.</p>
<table class="grid compact">
<tr><th>Test</th><th>Where VCI checks it</th></tr>
<tr><td>Reaches the owner's outcome</td><td>K2, K6</td></tr>
<tr><td>Proven to be the cause</td><td>Gate 6, reversal</td></tr>
<tr><td>Holds under the conditions that caused the failure</td><td>Gate 5, validation</td></tr>
<tr><td>Has an end</td><td>K5</td></tr>
</table>
</div>
</section>
"""

ct_rows = "".join(
    f"<tr><td class='k'>{e(v['label'])}</td><td>{e(v['does'])}</td><td>{e(v['end'])}</td></tr>"
    for v in C["claimTypes"].values())
claims = f"""
<section>
<h2 class="sec"><span>2</span>Claim types</h2>
<p class="lede">Most handwaving lives here: selling one of these as another. Every type is legitimate when named honestly. At intake the solver declares a type, and the type sets which tests apply. Only the disguise fails.</p>
<table class="grid">
<tr><th>Claim type</th><th>What it does</th><th>Its honest end</th></tr>
{ct_rows}
</table>
<div class="rule"><b>Mislabeled claim (stop).</b> A mitigation or management effort presented as a solution; research presented as a fix; management sold on a Terminal or Finite problem, or on interior ground of an Inflow problem; a solution claimed against a whole Adaptive or Inflow problem without naming the sub-problem it closes; a pilot renewed with no decision.</div>
<div class="rule"><b>Maintenance rule.</b> Recurring upkeep of a deployed intervention is allowed in any lane when it runs at a fixed interval, at a fixed price, and is measured against a published decay or wear curve. Open-ended advisory, study, or monitoring is not maintenance.</div>
</section>
"""

lane_rows = "".join(
    f"<div class='lane lane-{k}'><h4>{e(v['label'])}</h4><p>{e(v['rule'])}</p></div>"
    for k, v in C["lanes"].items())
lanes = f"""
<section>
<h2 class="sec"><span>3</span>Lanes: the Delgado Vector Law</h2>
<p class="lede">Whether a problem is allowed to be ongoing depends on three facts: whether its source can be eliminated, how many vectors it has, and whether they share a constraint. This is the part of VCI that separates a legitimately open-ended effort from a solvable problem kept open because it pays. It extends Goldratt's Theory of Constraints (1984) from system throughput to whether a problem can be closed at all.</p>
<div class="law">A problem closes when its source can be eliminated and its routes, both in and around, can be closed: at one shared constraint (Terminal) or one by one (Finite). It is legitimately ongoing only where a permanent source keeps pressing on its doors (Inflow) or where it invents new routes (Adaptive), and even then only under a metric and a sunset review. Some problems have no end. None has no answer.</div>

<div class="tree">
<svg viewBox="0 0 720 300" role="img" aria-label="Lane decision tree">
  <defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#3d5561"/></marker></defs>
  <g font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#12303b">
    <rect x="240" y="6" width="300" height="46" rx="4" fill="#e6eef1" stroke="#3d5561"/>
    <text x="390" y="25" text-anchor="middle" font-weight="700">L1  Can it invent new routes?</text>
    <text x="390" y="42" text-anchor="middle">(thinking adversary, mutation, resistance)</text>
    <line x1="240" y1="29" x2="178" y2="29" stroke="#3d5561" marker-end="url(#ah)"/>
    <text x="209" y="22" font-weight="700" text-anchor="middle">Yes</text>
    <rect x="0" y="8" width="176" height="44" rx="4" fill="#fff4e0" stroke="#a86a14"/>
    <text x="88" y="27" text-anchor="middle" font-weight="700">ADAPTIVE</text>
    <text x="88" y="43" text-anchor="middle">metric and sunset review</text>
    <line x1="390" y1="52" x2="390" y2="102" stroke="#3d5561" marker-end="url(#ah)"/>
    <text x="398" y="82" font-weight="700">No, or can't show it</text>
    <rect x="240" y="104" width="300" height="46" rx="4" fill="#e6eef1" stroke="#3d5561"/>
    <text x="390" y="123" text-anchor="middle" font-weight="700">VS  Is the source permanent and</text>
    <text x="390" y="140" text-anchor="middle" font-weight="700">outside the owner's reach?</text>
    <line x1="240" y1="127" x2="178" y2="127" stroke="#3d5561" marker-end="url(#ah)"/>
    <text x="209" y="120" font-weight="700" text-anchor="middle">Yes</text>
    <rect x="0" y="100" width="176" height="56" rx="4" fill="#fff4e0" stroke="#a86a14"/>
    <text x="88" y="118" text-anchor="middle" font-weight="700">INFLOW</text>
    <text x="88" y="134" text-anchor="middle">interior closes; doors stay</text>
    <text x="88" y="149" text-anchor="middle">on metric and review</text>
    <line x1="390" y1="150" x2="390" y2="200" stroke="#3d5561" marker-end="url(#ah)"/>
    <text x="398" y="180" font-weight="700">No, or can't show it</text>
    <rect x="240" y="202" width="300" height="46" rx="4" fill="#e6eef1" stroke="#3d5561"/>
    <text x="390" y="221" text-anchor="middle" font-weight="700">L2  Do all routes, in and around,</text>
    <text x="390" y="238" text-anchor="middle" font-weight="700">share one physical constraint?</text>
    <line x1="540" y1="216" x2="566" y2="200" stroke="#3d5561" marker-end="url(#ah)"/>
    <line x1="540" y1="236" x2="566" y2="256" stroke="#3d5561" marker-end="url(#ah)"/>
    <text x="548" y="198" font-weight="700">Yes</text>
    <text x="548" y="266" font-weight="700">No</text>
    <rect x="568" y="172" width="146" height="44" rx="4" fill="#e3f1e6" stroke="#2d6a3a"/>
    <text x="641" y="191" text-anchor="middle" font-weight="700">TERMINAL</text>
    <text x="641" y="207" text-anchor="middle">interdict it, closes</text>
    <rect x="568" y="242" width="146" height="44" rx="4" fill="#e3f1e6" stroke="#2d6a3a"/>
    <text x="641" y="261" text-anchor="middle" font-weight="700">FINITE</text>
    <text x="641" y="277" text-anchor="middle">close all N</text>
  </g>
</svg>
</div>
<div class="lanes">{lane_rows}</div>

<h3 style="page-break-before:always;margin-top:0">Decomposition rule</h3>
<p>Large problems fail K2 until they are split, which is correct behavior. Split the problem into sub-problems, assign each its own lane, and judge every claim at the sub-problem level. An Adaptive parent can hold Terminal children. Cybersecurity is Adaptive, but SQL injection as a class closes with parameterized queries, and password theft as a vector closes with hardware keys. Selling ongoing management on a Terminal child is a Mislabeled claim. An Inflow parent splits the same way: the brown tree snake on Guam is an Inflow problem whose interior is a Terminal child, one parcel at a time, and whose doors are the ongoing part. A permanent sentinel is earned at the doors and nowhere else.</p>

<h3>Research lane</h3>
<p>Research is legitimate, and it is not open-ended either: research ends when the question is answered, whichever way it comes out. When the claim type is Research or Pilot, the kill forks test different things.</p>
<table class="grid compact">
<tr><th>Fork</th><th>Solution types</th><th>Research and pilot</th></tr>
<tr><td class="k">K2</td><td>Owner's outcome, measurable, agreed</td><td>The question, plus the decision it will feed</td></tr>
<tr><td class="k">K3</td><td>Failure condition written before the work</td><td>The 'no' result and analysis plan written before data; all results reported (file drawer, Rosenthal, 1979)</td></tr>
<tr><td class="k">K4</td><td>Failure hit, kept going</td><td>Answer came back 'no' and was reframed as promising</td></tr>
<tr><td class="k">K5</td><td>End state</td><td>End date and handoff. Pilot: decision date to scale, change, or kill. Same question asked again, or wider, is perpetual study</td></tr>
<tr><td class="k">K6</td><td>Measured on the owner's outcome</td><td>Answers the original question, not a swapped one</td></tr>
</table>
<p class="note">"Further research needed" is allowed once, and only with a narrower question. A pilot renewed without a decision is rerouted and judged as the claim type it has become. A case study that only documents is not a claim; the moment it asks for continued resources tied to the problem, K0 catches it.</p>
</section>
"""

rules = f"""
<section>
<h2 class="sec"><span>4</span>How to run it</h2>
<div class="cols2">
<div>
<h3>Answer rule</h3>
<p>Every question takes <b>Yes</b>, <b>No</b>, or <b>Can't show it</b>, which counts as No. A few questions allow <b>Does not apply</b>, only under the stated condition. Each question carries an evidence line saying what counts as Yes.</p>
<h3>Stage</h3>
<p><b>{e(C['stages']['before']['label'])}.</b> {e(C['stages']['before']['note'])}</p>
<p><b>{e(C['stages']['after']['label'])}.</b> {e(C['stages']['after']['note'])}</p>
<p class="note">A surgeon does not get to define malpractice after the patient is on the table. The hospital can still demand a proper plan before the next operation.</p>
</div>
<div>
<h3>Newcomer rule</h3>
<p>A solver with no prior offers is flagged <b>No record</b> and skips the track record section without penalty. Otherwise VCI locks out every new solver and protects incumbents, the opposite of its purpose.</p>
<h3>Evaluator stake</h3>
<p>Before starting, the evaluator writes down any stake they hold in the outcome. VCI applies to whoever runs it.</p>
<h3>Scoring</h3>
<p>Kill forks stop the run the moment one cannot be passed. Survivors run the gauntlet:</p>
<table class="grid compact">
<tr><td class="k">0 soft fails</td><td>{ans_tag('GENUINE')}</td></tr>
<tr><td class="k">1 to {C['thresholds']['gapsMaxSoftFails']}</td><td>{ans_tag('GAPS')}</td></tr>
<tr><td class="k">{C['thresholds']['gapsMaxSoftFails']+1} or more</td><td>{ans_tag('UNPROVEN')}</td></tr>
</table>
</div>
</div>
<h3>Run order</h3>
<div class="flow">
<span>K0 Intake</span><i></i><span>K1 Vectors, lane, label</span><i></i><span>K2 Outcome</span><i></i><span>K3 Failure condition</span><i></i><span>K4 Failure already hit</span><i></i><span>K5 End state</span><i></i><span>K6 Same yardstick</span><i></i><span>Gauntlet, Gates 1 to 8</span><i></i><span>Track record</span>
</div>
<p class="note">Most unsupported claims stop within six questions, at K3, K4, or K5. Every stop names what it caught, so the verdict carries a citation instead of an opinion.</p>
</section>
"""

def q_of(f, key="default"):
    q = f["q"]
    return q.get(key) or q.get("default") or next(iter(q.values()))

K = C["forks"]
fork_cards = []
fork_cards.append(f"""
<div class="fork">
 <div class="fh"><b>K0</b> Intake <span class="src">{e(C['intake']['K0']['source'])}</span></div>
 <p class="q">{e(C['intake']['K0']['q'])}</p>
 <p class="pl">Plain: {e(C['intake']['K0']['plain'])}</p>
 <p class="ev">Counts as Yes: {e(C['intake']['K0']['evidence'])}</p>
 <p class="out">No: {ans_tag('OUT_OF_SCOPE')} &nbsp; Yes: solver declares a claim type, evaluator states their stake, continue.</p>
</div>""")
L = C["laneQuestions"]; MI = C["mislabel"]
fork_cards.append(f"""
<div class="fork">
 <div class="fh"><b>K1</b> Vectors, lane, and label <span class="src">Delgado Vector Law</span></div>
 <p class="q"><b>V0</b> {e(L['V0']['q'])} <span class="soft">soft</span></p>
 <p class="q"><b>VC</b> {e(L['VC']['q'])} <span class="soft">soft</span></p>
 <p class="q"><b>L1</b> {e(L['L1']['q'])} <br><span class="ev">{e(L['L1']['evidence'])}</span></p>
 <p class="q"><b>VS</b> {e(L['VS']['q'])} <br><span class="ev">{e(L['VS']['evidence'])}</span></p>
 <p class="q"><b>L2</b> {e(L['L2']['q'])}</p>
 <p class="q"><b>M1</b> {e(MI['M1']['q'])}</p>
 <p class="q"><b>M2</b> (Solution or partial solution in the Adaptive or Inflow lane) {e(MI['M2']['q'])}</p>
 <p class="q"><b>M3</b> (Management in the Inflow lane) {e(MI['M3']['q'])}</p>
 <p class="out">Management in a Terminal or Finite lane, or No on M1, M2, or M3: {ans_tag('MISLABELED')} &nbsp; Escape before commitment: relabel honestly and continue.</p>
</div>""")
for fid in ["K2", "K3", "K3R", "K4", "K5", "K5R", "K6"]:
    f = K[fid]
    variants = ""
    if len(f["q"]) > 1:
        variants = "<ul class='var'>" + "".join(
            f"<li><b>{e(C['claimTypes'][k]['label'] if k in C['claimTypes'] else 'Default')}:</b> {e(v)}</li>"
            for k, v in f["q"].items() if k != "default") + "</ul>"
    only = ""
    if f.get("onlyFor"):
        only = " <span class='soft'>" + e(", ".join(C['claimTypes'][x]['label'] for x in f['onlyFor'])) + " only</span>"
    esc = f"Escape before commitment: {e(f['escape'])}" if f.get("escape") else "No escape hatch."
    if f.get("reentry"):
        esc += " " + e(f["reentry"])
    fork_cards.append(f"""
<div class="fork">
 <div class="fh"><b>{fid}</b> {e(f['title'])}{only} <span class="src">{e(f['source'])}</span></div>
 <p class="q">{e(q_of(f))}</p>{variants}
 <p class="pl">Plain: {e(f['plain'])}</p>
 <p class="ev">Evidence: {e(f['evidence'])}</p>
 <p class="out">Fail: {ans_tag(f['fail'])} &nbsp; {esc}</p>
</div>""")
forks = f"""
<section>
<h2 class="sec"><span>5</span>Kill forks</h2>
<p class="lede">Some forks already tell the whole story. If the solver cannot get past one, the other questions do not matter. Each fork ends the run with a named verdict.</p>
{''.join(fork_cards)}
</section>
"""

rows = []
cur = None
for g in C["gauntlet"]:
    if g["gate"] != cur:
        cur = g["gate"]
        rows.append(f"<tr class='gh'><td colspan='3'>Gate {e(cur)}</td></tr>")
    flags = []
    if g.get("fatal"): flags.append("<span class='fatal'>Fatal: Problem preserved</span>")
    if g.get("na"): flags.append(f"<span class='soft'>{e(g.get('naNote','N/A allowed'))}</span>")
    if g.get("lanes"): flags.append("<span class='soft'>" + e(", ".join(C['lanes'][x]['label'] for x in g['lanes'])) + " lane only</span>")
    if g.get("skipFor"): flags.append("<span class='soft'>Skipped for " + e(", ".join(C['claimTypes'][x]['label'] for x in g['skipFor'])) + "</span>")
    rows.append(f"""<tr><td class="id">{e(g['id'])}</td><td><div class="gq">{e(g['q'])}</div><div class="pl">Plain: {e(g['plain'])}</div><div class="ev">Yes means: {e(g['evidence'])}</div>{' '.join(flags)}</td><td class="src2">{e(g['source'])}</td></tr>""")
TR = C["trackRecord"]
rows.append(f"<tr class='gh'><td colspan='3'>Track record</td></tr>")
rows.append(f"""<tr><td class="id">T0</td><td><div class="gq">{e(TR['entry']['q'])}</div><div class="ev">{e(TR['entry']['evidence'])}</div></td><td class="src2">{e(TR['entry']['source'])}</td></tr>""")
for t in TR["questions"]:
    rows.append(f"""<tr><td class="id">{e(t['id'])}</td><td><div class="gq">{e(t['q'])}</div><div class="pl">Plain: {e(t['plain'])}</div><div class="ev">Yes means: {e(t['evidence'])}</div></td><td class="src2">{e(t['source'])}</td></tr>""")
gauntlet = f"""
<section>
<h2 class="sec"><span>6</span>The gauntlet</h2>
<p class="lede">Claims that survive the kill forks answer every remaining question. Each No is a soft fail and comes with the follow-up question to put to the solver. Question 7.4 is the one fatal item: two consecutive phases that eliminate nothing.</p>
<table class="gt">
<tr><th>ID</th><th>Question</th><th>Basis</th></tr>
{''.join(rows)}
</table>
</section>
"""

domains = """
<section>
<h2 class="sec"><span>7</span>Across every arena</h2>
<p class="lede">The gates never depended on a vendor. They test any claim that a problem is being solved, whoever makes it and whatever they ask for.</p>
<table class="grid">
<tr><th>Arena</th><th>K3 asked there</th><th>K5 asked there</th></tr>
<tr><td class="k">Government program</td><td>What result would show this program failed?</td><td>When does the program sunset if it works?</td></tr>
<tr><td class="k">Research grant</td><td>What finding would kill the hypothesis?</td><td>What result ends the study, and who gets the answer?</td></tr>
<tr><td class="k">Medical treatment</td><td>What outcome means this is not working?</td><td>When do we stop or switch?</td></tr>
<tr><td class="k">Nonprofit or charity</td><td>What number shows the problem is not shrinking?</td><td>What does "problem solved, we close" look like?</td></tr>
<tr><td class="k">Software or subscription</td><td>What would prove the tool is not solving it?</td><td>When is it fixed so I can cancel?</td></tr>
<tr><td class="k">Public safety</td><td>What figure would show the approach failed?</td><td>What level ends the surge?</td></tr>
<tr><td class="k">Contractor or repair</td><td>If this part is swapped and the fault stays, what then?</td><td>When is the job done and the invoice final?</td></tr>
<tr><td class="k">Your own project</td><td>What test result would prove my design wrong?</td><td>What is the ship condition?</td></tr>
</table>
<h3>The three-question short form</h3>
<ol class="short">
<li>What result would prove your work wrong, and did you write it down before starting?</li>
<li>Can you show the failure with your fix out, and gone with it in?</li>
<li>What is the measurable condition where your involvement ends?</li>
</ol>
<p class="note">Anyone who is actually trying to solve the problem answers all three without strain. A problem that can invent new vectors answers the third with a metric and a sunset review.</p>
</section>
"""

validation = """
<section>
<h2 class="sec"><span>8</span>Validation against history</h2>
<p class="lede">A test that has not been tested is a claim. These cases have known outcomes. VCI was run on each as the claim stood at launch, and the verdict was compared with what happened.</p>
<div class="limit"><b>Limitation, stated up front.</b> This run was done by the author with outcomes already known. It checks that VCI routes real cases consistently. It is not the blind test. The blind test (Section 9) is what freezes v1.0.</div>

<div class="case">
<div class="ch"><b>Smallpox</b> WHO Intensified Eradication Programme, 1967 to 1980 <span class="res ok">Consistent</span></div>
<table class="grid compact">
<tr><td class="k">Lane</td><td>Terminal. Humans were the only host: no animal reservoir, no latent or persistent human infection. One host is one constraint.</td></tr>
<tr><td class="k">Claim</td><td>Solution. Outcome: zero cases worldwide. Ring vaccination narrowed each phase to cases and contacts (Gate 7).</td></tr>
<tr><td class="k">VCI verdict</td><td>Genuine attempt.</td></tr>
<tr><td class="k">Outcome</td><td>Last natural case in Somalia, 1977. Eradication declared at the 33rd World Health Assembly, May 8, 1980. Still the only human disease eradicated.</td></tr>
</table>
</div>

<div class="case">
<div class="ch"><b>Malaria</b> WHO Global Malaria Eradication Programme, 1955 to 1969 <span class="res ok">Consistent</span></div>
<table class="grid compact">
<tr><td class="k">Lane</td><td>Adaptive. Mosquito resistance to DDT was already emerging at launch and was used as the argument for launching quickly. Chloroquine resistance was confirmed in 1960.</td></tr>
<tr><td class="k">Claim</td><td>Solution: time-limited global eradication, largely through indoor residual spraying.</td></tr>
<tr><td class="k">VCI verdict</td><td>Mislabeled claim at K1 (M2). A solution claimed against a whole Adaptive problem without naming the sub-problems it closes.</td></tr>
<tr><td class="k">Outcome</td><td>Discontinued in 1969; eradication abandoned in favor of control. It did eliminate malaria in many temperate regions, consistent with the decomposition rule: Terminal children closed, the Adaptive parent did not.</td></tr>
</table>
</div>

<div class="case">
<div class="ch"><b>Guinea worm</b> Guinea Worm Eradication Program, 1986 to present <span class="res ok">Consistent</span></div>
<table class="grid compact">
<tr><td class="k">Lane</td><td>At launch, Terminal: infection came through drinking water carrying infected water fleas. In 2012 infections in dogs were confirmed, which changed the vector list. Re-run: Finite (human and animal hosts, drinking water, undercooked aquatic animals).</td></tr>
<tr><td class="k">Claim</td><td>Solution. Outcome: zero human and animal infections, certified country by country.</td></tr>
<tr><td class="k">VCI verdict</td><td>Genuine attempt, end not yet reached. When the dog finding widened the problem, the program answered with targeted studies of dog behavior and water use and a new diagnostic for dogs, which narrows (Gate 7). This case tests the false-alarm guard: long duration alone must not read as preservation.</td></tr>
<tr><td class="k">Outcome</td><td>Human cases fell from an estimated 3.5 million (1986) to 10 provisional cases in 2025. 200 countries certified free. Animal infections rose slightly in 2025, driven by Cameroon and Angola, while Chad cut animal infections 47%.</td></tr>
</table>
</div>

<div class="case">
<div class="ch"><b>Polio</b> Global Polio Eradication Initiative, 1988 to present <span class="res ok">Consistent</span></div>
<table class="grid compact">
<tr><td class="k">Lane</td><td>Finite: three wild poliovirus types, human hosts only. The oral vaccine can revert and circulate (cVDPV), an intervention that created its own vector, which VCI now requires to be counted (changelog item 10).</td></tr>
<tr><td class="k">Claim</td><td>Solution, with closures countable X of N.</td></tr>
<tr><td class="k">VCI verdict</td><td>Credible, with gaps. Passes the kill forks and counts closures. Fails T4: the 2000 target was missed, and later deadlines in 2012 and 2015 were missed.</td></tr>
<tr><td class="k">Outcome</td><td>Wild types 2 and 3 certified eradicated in 2015 and 2019: 2 of 3 closed. Type 1 remains endemic in Afghanistan and Pakistan. 143 cVDPV cases were reported in 2025 as of September 17. Current targets: type 1 certification by 2027, cVDPV2 elimination by 2029.</td></tr>
</table>
</div>

<div class="case">
<div class="ch"><b>Brown tree snake</b> Guam, Habitat Management Unit 2011 to present, and island-wide <span class="res part">Reclassified</span></div>
<table class="grid compact">
<tr><td class="k">First pass</td><td>Filed as Terminal on movement alone: every move is a surface contact. That pass counted how the snake moves and never counted how it gets in. Corrected in RC2 (changelog item 13).</td></tr>
<tr><td class="k">Lane</td><td>Inflow. Source: a native population in New Guinea and nearby islands, permanent. Entry: ports, airfield, vessels, a finite set of doors. Movement: one constraint, surface contact, including culverts and the waterline. Interior parcels are Terminal children; the doors are the ongoing part.</td></tr>
<tr><td class="k">Claims</td><td>The HMU: partial solution on a Terminal child, a 55 ha block ringed by 3.6 km of snake barrier fence, with aerial acetaminophen bait. Cargo and port interdiction: management at the doors, legitimate in this lane with a metric and a review.</td></tr>
<tr><td class="k">VCI verdict</td><td>HMU passes as a partial solution with a measurable end, a snake-free unit. Interdiction passes as door management. An island-wide effort needs an interior end state; ongoing management sold on interior ground would be Mislabeled (M3).</td></tr>
<tr><td class="k">Outcome</td><td>Managers reported in 2023 that snakes inside the HMU were increasingly hard to find. The Navy reports the last live snake to escape Guam was in 2006. Barriers have been built; any claim that none exist is false and should not be repeated.</td></tr>
</table>
</div>

<table class="grid compact score">
<tr><th>Case</th><th>VCI verdict</th><th>Actual</th><th>Agreement</th></tr>
<tr><td>Smallpox</td><td>Genuine attempt</td><td>Eradicated 1980</td><td>Yes</td></tr>
<tr><td>Malaria GMEP</td><td>Mislabeled claim</td><td>Abandoned 1969</td><td>Yes</td></tr>
<tr><td>Guinea worm</td><td>Genuine attempt, open</td><td>10 human cases, 2025</td><td>Yes</td></tr>
<tr><td>Polio</td><td>Credible, with gaps</td><td>2 of 3 closed, dates missed</td><td>Yes</td></tr>
<tr><td>Guam, Inflow</td><td>HMU passes; doors ongoing</td><td>Snakes declining in unit</td><td>Yes, island-wide open</td></tr>
</table>
<p class="note">Negative controls are thin: only the malaria programme is a known failure in this set. The blind run needs more known failures so VCI's accuracy is shown in both directions.</p>
</section>
"""

self_audit = f"""
<section>
<h2 class="sec"><span>9</span>Self-audit: VCI run on VCI</h2>
<p class="lede">The first principle is that you must not fool yourself, and you are the easiest person to fool (Feynman, 1974). A tool that demands falsification from everyone else and has none itself gets thrown out on sight.</p>
<table class="grid">
<tr><td class="k">Claim type</td><td>Solution: a test that identifies genuine attempts.</td></tr>
<tr><td class="k">Lane</td><td>Finite. The routes a problem-solving claim can dodge are enumerated in the kill forks and gauntlet. New dodges are added through the changelog.</td></tr>
<tr><td class="k">K2 outcome</td><td>Two evaluators who do not know each other, given the same evidence, reach the same verdict, and verdicts predict how efforts turn out.</td></tr>
<tr><td class="k">K3 failure conditions</td><td>VCI is wrong, and gets revised, if any of these occur: (1) efforts known to have succeeded are stopped at a kill fork; (2) efforts known to have failed or been preserved pass as Genuine attempts; (3) independent evaluators given the same evidence disagree on the verdict in more than 1 case in 10.</td></tr>
<tr><td class="k">K5 end state</td><td>v1.0 freezes after one blind run: at least 20 historical cases with known outcomes, at least a third of them known failures, scored by at least two evaluators who have not seen the outcomes. After that, changes happen only through numbered versions.</td></tr>
<tr><td class="k">K6 yardstick</td><td>Measured on evaluator agreement and verdict-outcome agreement, the K2 outcome.</td></tr>
<tr><td class="k">Evaluator stake</td><td>The author holds IP he pitches with VCI scorecards. That is why the blind run uses outside evaluators.</td></tr>
<tr><td class="k">Current verdict</td><td>{ans_tag('GAPS')} Fails 5.1 (not yet tested blind, under the conditions where it would fail) and 6.1 (no control comparison yet). Both close with the blind run.</td></tr>
</table>
</section>
"""

objections = [
 ("Who made you a standard?", "Nobody, and VCI claims no standard. The problem owner's outcome is the standard. An owner who wants VCI to govern their own resources adopts it with the clause in Section 11."),
 ("This is just the Heilmeier Catechism.", "VCI builds on it and credits it. Heilmeier asks a solver to describe the plan. VCI tests whether the plan can be proven wrong, whether the fix is shown to be the cause, and whether the problem is allowed to be ongoing at all."),
 ("Real problems are complicated.", "Complexity is allowed. The decomposition rule splits the problem and judges each part. Every part still ends at an outcome, an answer, a decision, or a sunset review."),
 ("Some problems never end.", "Then they are Adaptive and ongoing work is legitimate, under a metric and a sunset review. What fails is a problem with an end being sold as one without."),
 ("Fixing it revealed hidden issues.", "That happens honestly. It passes when each new issue comes with its own evidence (3.4) and its own failure condition. It fails when a stated failure condition was hit and the effort carried on (K4)."),
 ("We are a study, a pilot, a case study.", "Function, not label. Research ends at an answer, a pilot at a decision, and a case study is not a claim until it asks for continued resources."),
 ("Terminal means you expect it done by Friday.", "Terminal means an end exists. It says nothing about cost or speed. Smallpox was Terminal and took thirteen years of the intensified programme."),
 ("Your own product needs maintenance.", "Fixed interval, fixed price, measured against a published decay curve is maintenance and is allowed in every lane. Open-ended advisory is not."),
 ("This will kill new ideas.", "The newcomer rule removes track record penalties, the Research lane gives early work its own honest end, and every escape hatch is open before commitment."),
 ("Escape hatches are a get-out-of-jail card.", "They close once resources are committed. The verdict on what was spent stands. The hatch only lets the next tranche start as a fresh, pre-registered claim."),
 ("Honest discovery can widen uncertainty.", "It can, and it still eliminates something. The measure is candidates eliminated, which must rise every phase. Two consecutive phases eliminating nothing is the fatal item 7.4."),
 ("The funder decides what success is.", "The owner is whoever bears the cost. Where the funder is also the preserver, the owner's outcome wins. Where owners are diffuse, the measured harm stands in for them."),
 ("This is an accusation.", "Verdicts describe structure, not intent. 'No exit condition and revenue tied to the problem staying open' is provable from documents. Motive is not claimed."),
 ("The evaluator has an agenda.", "The evaluator states their stake before starting. VCI applies to whoever runs it, including its author (Section 9)."),
 ("Metrics can be gamed.", "K6 ties success to the owner's outcome from K2. A metric the solver chose later does not count."),
 ("You called the brown tree snake single-vector.", "The first pass counted how it moves and not how it gets in. Counting both, with the closure test, puts it in the Inflow lane. The correction came from the framework's own flagship case and is logged in the changelog, which is how VCI is supposed to behave when it is wrong."),
 ("Nobody will fund fixing the culverts, so it is ongoing.", "Neglect is not a lane. An untreated route inside the boundary is still closable. It is reported as a neglect finding against whoever should act, never used to justify open-ended work."),
 ("Your thresholds are arbitrary.", "They are published, sit in one config file, and change only through a numbered version with the objection that caused the change."),
]
obj_html = "".join(f"<div class='obj'><p class='oq'>{e(q)}</p><p>{e(a)}</p></div>" for q, a in objections)
objs = f"""
<section>
<h2 class="sec"><span>10</span>Known objections</h2>
<p class="lede">Every attack found so far, with its answer. A critic who finds their objection already answered stops attacking the tool and starts answering the questions.</p>
<div class="objs">{obj_html}</div>
</section>
"""

adoption = f"""
<section>
<h2 class="sec"><span>11</span>Adoption clause</h2>
<p class="lede">VCI claims no authority. An owner putting up their own resources can give it theirs. This is where directive language belongs.</p>
<div class="clause">
<p><b>[Owner]</b> evaluates every proposal, renewal, and phase request under the Vector-Constraint Index, version <b>{e(M['version'])}</b> ({e(M['docRef'])}).</p>
<p>Proposals must answer kill forks K0 through K6 in writing before resources are committed. A proposal that stops at a kill fork is returned without award. A renewal or next phase is evaluated after commitment, and a stop verdict on resources already spent is recorded.</p>
<p>Our desired outcome for this effort is: <span class="blank"></span></p>
<p>Signed for the owner: <span class="blank short"></span> &nbsp; Date: <span class="blank short"></span></p>
</div>

<h3>Promise ledger sheet</h3>
<p>Log every offer when it is made, and log the result when it lands. Over time this builds the record that T1 to T5 draw from, and it makes pre-registration public instead of relying on the solver's own paperwork.</p>
<table class="ledger">
<tr><th>Offer</th><th>Date made</th><th>K2 outcome promised</th><th>K3 failure condition</th><th>K5 end state</th><th>Cost and time promised</th><th>Result delivered</th><th>Cost and time actual</th><th>Ended?</th></tr>
{''.join('<tr>' + '<td></td>'*9 + '</tr>' for _ in range(6))}
</table>
</section>
"""

refs = """
<section>
<h2 class="sec"><span>12</span>Foundations and changelog</h2>
<div class="cols2">
<div>
<h3>Built on</h3>
<ul class="refs">
<li>Shirky, C. Stated by Shirky; named the Shirky Principle by K. Kelly, <i>The Technium</i>, April 2010.</li>
<li>Popper, K. <i>Logik der Forschung</i>, 1934; <i>The Logic of Scientific Discovery</i>, 1959.</li>
<li>Lakatos, I. Falsification and the methodology of scientific research programmes, 1970.</li>
<li>Chamberlin, T. C. The method of multiple working hypotheses, 1890.</li>
<li>Platt, J. R. Strong inference. <i>Science</i>, 1964.</li>
<li>Heilmeier, G. The Heilmeier Catechism, DARPA, 1970s.</li>
<li>Buckingham, E. On physically similar systems. <i>Physical Review</i>, 1914.</li>
<li>Goldratt, E. M. <i>The Goal</i>, 1984.</li>
<li>IEEE Std 1012, System, Software, and Hardware Verification and Validation.</li>
<li>Barlow, D. H. and Hersen, M. <i>Single Case Experimental Designs</i>, 2nd ed., 1984.</li>
<li>Mill, J. S. <i>A System of Logic</i>, 1843.</li>
<li>NASA NPR 7120.5, Program and Project Management Requirements (key decision points).</li>
<li>Goodhart, C. 1975; Campbell, D. T. Assessing the impact of planned social change, 1976.</li>
<li>Kahneman, D. and Tversky, A. Intuitive prediction, 1979; Flyvbjerg, B. From Nobel Prize to project management, 2006.</li>
<li>Rosenthal, R. The file drawer problem and tolerance for null results, 1979.</li>
<li>Ioannidis, J. P. A. Why most published research findings are false, 2005.</li>
<li>Taleb, N. N. <i>Skin in the Game</i>, 2018.</li>
<li>Feynman, R. P. Cargo cult science, Caltech commencement, 1974.</li>
</ul>
<h3>Related tools</h3>
<p class="small">Sagan's baloney detection kit (<i>The Demon-Haunted World</i>, 1995) tests claims about the world; Bergstrom and West (<i>Calling Bullshit</i>, 2020) test data claims; Frankfurt (<i>On Bullshit</i>, 1986) defines the indifference to truth VCI detects in outcomes; Brandolini's law explains why a ready-made test is needed. VCI is the version for claims that a problem is being solved. Case data in Section 8: WHO; CDC <i>MMWR</i>; The Carter Center; GPEI and the WHO Polio IHR Emergency Committee; <i>PLoS Medicine</i> (Najera et al., 2011); Joint Region Marianas and USGS.</p>
</div>
<div>
<h3>Changelog</h3>
<p class="small">Each change names the objection that caused it. A framework that gets stronger when it is hit is a progressive programme in Lakatos's sense.</p>
<ol class="log" style="font-size:8.1pt">
<li>Verification and validation now cite IEEE Std 1012 for both. ASME V&amp;V 10 and 20 are domain standards (solid mechanics; fluids and heat transfer), each covering both.</li>
<li>Control test cites the ABAB reversal design and Mill's method of difference.</li>
<li>Maintenance rule added so hardware with scheduled upkeep is not misread as preservation.</li>
<li>K1 assigns the lane and checks the label; it no longer kills Adaptive problems outright.</li>
<li>Claim types and the Mislabeled verdict added after the relabeling dodge was found.</li>
<li>Research lane added, with perpetual study, file drawer, and permanent pilot rules.</li>
<li>Escape hatches limited to before commitment.</li>
<li>Gate 7 measured by candidates eliminated; two empty phases in a row made fatal.</li>
<li>Decomposition, proxy owner, evaluator stake, and "Terminal is not cheap" added after the four-problem stress test (brown tree snake, cyber attacks, digital privacy, AI).</li>
<li>Intervention-created vectors must be counted, after the polio cVDPV case.</li>
<li>Owner defined as whoever bears the cost, after the funder-as-preserver case.</li>
<li>Verdict language set to structure, not intent.</li>
<li><b>RC2.</b> Vector defined, with six roles and the closure test, after the brown tree snake case: its entry routes had not been counted.</li>
<li><b>RC2.</b> Inflow lane added for a permanent source outside the owner's reach; management at the doors only (M3).</li>
<li><b>RC2.</b> Neglect ruled out as a vector or lane.</li>
<li><b>RC2.</b> Gates 5 and 6 may be marked as not applying only when no field results exist; bench results belong to Gate 4.</li>
<li><b>RC3.</b> Licensing split set: method open, product layer closed, names reserved.</li>
</ol>
<h3>License</h3>
<p class="small">See Licensing and names. Contact: andrew.delgado@crea8or1.com</p>
</div>
</div>
<div class="licbox">
<h3 style="margin-top:0">Licensing and names</h3>
<table class="grid compact">
<tr><td class="k">This specification</td><td>Creative Commons Attribution 4.0 International (CC BY 4.0). Anyone may use, copy, adapt, and share it, commercially or not, with credit to Andrew Delgado and a note of any changes. Full terms: creativecommons.org/licenses/by/4.0</td></tr>
<tr><td class="k">The free evaluator code</td><td>MIT License. Anyone may use, copy, change, and distribute the code, provided the copyright notice stays with it. Provided as is, without warranty.</td></tr>
<tr><td class="k">Names</td><td>Vector-Constraint Index&trade;, VCI&trade;, and Delgado Vector Law&trade; are trademarks of Creator 1 LLC. Neither license grants rights to these names. A modified version may not be called the Vector-Constraint Index or VCI, or carry a VCI version number. Only versions published by the author at the canonical source carry a version number. Accurate statements such as "based on the Vector-Constraint Index v1.0" are welcome.</td></tr>
<tr><td class="k">Not covered</td><td>The Promise Ledger, teardowns, deep dives, audit reports, and any paid tools are separate works under ordinary copyright. They are not licensed under CC BY or MIT.</td></tr>
</table>
<p class="small">&copy; 2026 Andrew Delgado. Cite as: Delgado, A. (2026). The Vector-Constraint Index: A deterministic test of whether a problem is actually being solved (Version 1.0-RC3). Zenodo. https://doi.org/{e(M['doi'])}</p>
</div>
</section>
"""

css = """
@page { size: Letter; margin: 0.62in 0.66in 0.7in 0.66in; }
:root { --ink:#12303b; --teal:#1f5f6e; --line:#c9d6db; --muted:#5a6d74; --paper:#ffffff; --wash:#eef3f5;
  --stop:#a3261c; --pass:#2d6a3a; --gaps:#8a5a00; --warn:#b3561c; }
* { box-sizing:border-box; }
body { font-family:"Bitstream Charter", Charter, Georgia, serif; font-size:10.1pt; line-height:1.42; color:var(--ink); background:var(--paper); margin:0; }
h1,h2,h3,h4,.docline,.fh,.tag,th,.flow span,.gh td,.ch,.res { font-family:"Liberation Sans", Arial, sans-serif; }
section { page-break-before:always; }
section.cover { page-break-before:auto; }
.docline { display:flex; justify-content:space-between; font-size:8pt; letter-spacing:.12em; color:var(--muted); border-bottom:2px solid var(--ink); padding-bottom:6px; }
h1 { font-size:31pt; line-height:1.05; margin:26px 0 6px; letter-spacing:-.01em; }
.sub { font-size:13.5pt; color:var(--teal); margin:0 0 6px; font-style:italic; }
.byline { font-family:"Liberation Sans", Arial, sans-serif; font-size:8.8pt; color:var(--muted); margin:0 0 20px; }
.shirky { margin:0; padding:14px 18px; background:var(--wash); border-left:4px solid var(--ink); }
.shirky p { font-size:14pt; margin:0 0 4px; }
.shirky cite { font-size:8.8pt; color:var(--muted); font-style:normal; font-family:"Liberation Sans", Arial, sans-serif; }
.thesis { font-size:12pt; font-weight:bold; margin:12px 0 18px; }
.doctrine h2 { font-size:11pt; text-transform:uppercase; letter-spacing:.1em; margin:0 0 6px; }
.doctrine ol { margin:0; padding-left:20px; }
.doctrine li { margin:0 0 5px; }
.status { font-size:9pt; color:var(--muted); border-top:1px solid var(--line); padding-top:8px; margin-top:14px; }
h2.sec { font-size:17pt; margin:0 0 6px; display:flex; align-items:baseline; gap:10px; border-bottom:2px solid var(--ink); padding-bottom:5px; }
h2.sec span { font-size:10pt; color:#fff; background:var(--ink); padding:2px 7px; border-radius:2px; }
h3 { font-size:11pt; margin:14px 0 5px; color:var(--teal); }
.lede { font-size:10.6pt; color:#2a454f; margin:6px 0 12px; }
.note, .small { font-size:8.9pt; color:var(--muted); }
.def { font-size:11pt; font-style:italic; margin:4px 0 8px; }
.defbox { margin-bottom:12px; }
.defbox h3 { margin-top:6px; }
table { border-collapse:collapse; width:100%; }
table.grid td, table.grid th { border:1px solid var(--line); padding:5px 7px; vertical-align:top; text-align:left; }
table.grid th { background:var(--wash); font-size:8.6pt; text-transform:uppercase; letter-spacing:.06em; }
table.compact td, table.compact th { padding:3.5px 6px; font-size:9.2pt; }
td.k { font-family:"Liberation Sans", Arial, sans-serif; font-weight:bold; font-size:8.9pt; width:21%; }
.rule { border:1px solid var(--line); border-left:4px solid var(--teal); padding:7px 10px; margin:10px 0; font-size:9.5pt; }
.law { font-size:11.2pt; font-weight:bold; background:var(--wash); padding:10px 14px; border-left:4px solid var(--teal); margin:8px 0 10px; }
.tree svg { width:100%; height:auto; max-height:290px; }
.tree { text-align:center; }
.lanes { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin:6px 0 4px; }
.lane { border:1px solid var(--line); padding:6px 8px; font-size:8.6pt; }
.lane h4 { margin:0 0 3px; font-size:9.5pt; text-transform:uppercase; letter-spacing:.08em; }
.lane p { margin:0; }
.lane-adaptive, .lane-inflow { border-top:3px solid #a86a14; } .lane-terminal, .lane-finite { border-top:3px solid #2d6a3a; }
.cols2 { display:grid; grid-template-columns:1fr 1fr; gap:22px; }
.flow { display:flex; flex-wrap:wrap; align-items:center; gap:6px; margin:4px 0 8px; }
.flow span { font-size:8.5pt; background:var(--ink); color:#fff; padding:4px 7px; border-radius:2px; }
.flow i { width:10px; height:2px; background:var(--ink); display:inline-block; }
.tag { display:inline-block; font-size:7.8pt; font-weight:bold; text-transform:uppercase; letter-spacing:.06em; padding:1px 6px; border-radius:2px; color:#fff; }
.tag-MISLABELED,.tag-NOT_TESTABLE,.tag-UNFALSIFIABLE,.tag-PRESERVED,.tag-MOVED_GOALPOSTS { background:var(--stop); }
.tag-GENUINE { background:var(--pass); } .tag-GAPS { background:var(--gaps); } .tag-UNPROVEN { background:var(--warn); } .tag-OUT_OF_SCOPE { background:var(--muted); }
.fork { border:1px solid var(--line); margin:0 0 8px; page-break-inside:avoid; }
.fh { background:var(--ink); color:#fff; padding:4px 9px; font-size:9.6pt; display:flex; gap:8px; align-items:baseline; }
.fh .src { margin-left:auto; font-size:7.6pt; font-weight:normal; opacity:.85; }
.fork p { margin:4px 9px; }
.fork .q { font-size:10pt; }
.pl { font-style:italic; color:#2a454f; font-size:9pt; }
.ev { color:var(--muted); font-size:8.7pt; }
.out { font-size:9pt; border-top:1px dashed var(--line); padding-top:4px; }
ul.var { margin:2px 9px 2px 28px; padding:0; font-size:9pt; }
.soft { font-family:"Liberation Sans", Arial, sans-serif; font-size:7.5pt; background:var(--wash); color:var(--muted); padding:1px 5px; border-radius:2px; white-space:nowrap; }
.fatal { font-family:"Liberation Sans", Arial, sans-serif; font-size:7.5pt; background:var(--stop); color:#fff; padding:1px 5px; border-radius:2px; }
table.gt td, table.gt th { border-bottom:1px solid var(--line); padding:4px 6px; vertical-align:top; text-align:left; }
table.gt th { font-size:8pt; text-transform:uppercase; letter-spacing:.06em; border-bottom:2px solid var(--ink); }
table.gt tr { page-break-inside:avoid; }
tr.gh td { background:var(--wash); font-weight:bold; font-size:8.8pt; text-transform:uppercase; letter-spacing:.06em; padding-top:6px; }
td.id { font-family:"DejaVu Sans Mono", monospace; font-size:8.5pt; width:34px; color:var(--teal); font-weight:bold; }
.gq { font-size:9.6pt; }
td.src2 { font-size:8pt; color:var(--muted); width:24%; }
ol.short li { font-size:11pt; margin-bottom:4px; }
.limit { border:1px solid var(--gaps); background:#fbf5e8; padding:7px 10px; font-size:9.2pt; margin-bottom:10px; }
.case { margin-bottom:9px; page-break-inside:avoid; }
.ch { font-size:9.6pt; background:var(--wash); padding:4px 8px; display:flex; gap:8px; align-items:baseline; border:1px solid var(--line); border-bottom:none; }
.ch b { font-size:10.5pt; }
.res { margin-left:auto; font-size:7.6pt; font-weight:bold; text-transform:uppercase; padding:1px 6px; border-radius:2px; color:#fff; }
.res.ok { background:var(--pass); } .res.part { background:var(--gaps); }
table.score { margin-top:6px; }
.objs { columns:2; column-gap:20px; }
.obj { break-inside:avoid; margin-bottom:8px; }
.obj p { margin:0; font-size:9.2pt; }
.obj .oq { font-family:"Liberation Sans", Arial, sans-serif; font-weight:bold; font-size:9.3pt; color:var(--teal); }
ol.inv li { margin-bottom:8px; font-size:10.4pt; }
.invite p { font-size:10.6pt; }
.licbox { margin-top:12px; page-break-inside:avoid; }
.clause { border:2px solid var(--ink); padding:10px 14px; font-size:10.3pt; }
.clause p { margin:0 0 8px; }
.blank { display:inline-block; border-bottom:1px solid var(--ink); width:100%; height:14px; }
.blank.short { width:170px; }
table.ledger th, table.ledger td { border:1px solid var(--ink); font-size:7.4pt; padding:3px; vertical-align:top; }
table.ledger th { background:var(--wash); font-family:"Liberation Sans", Arial, sans-serif; }
table.ledger td { height:44px; }
ul.refs { padding-left:14px; margin:0; font-size:8.5pt; } ul.refs li { margin-bottom:2px; }
ol.log { padding-left:16px; margin:0; font-size:8.5pt; } ol.log li { margin-bottom:2px; }
"""

doc = f"<!doctype html><html><head><meta charset='utf-8'><title>Vector-Constraint Index</title><style>{css}</style></head><body>{cover}{invite_sec}{defs}{claims}{lanes}{rules}{forks}{gauntlet}{domains}{validation}{self_audit}{objs}{adoption}{refs}</body></html>"

bad = re.findall("[\u2013\u2014]", doc)
assert not bad, f"dashes found: {len(bad)}"
(ROOT / "spec" / "vci_spec.html").write_text(doc)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((ROOT / "spec" / "vci_spec.html").as_uri())
    pg.wait_for_timeout(400)
    foot = f"<div style='font-family:Liberation Sans,Arial;font-size:7px;color:#5a6d74;width:100%;padding:0 0.66in;display:flex;justify-content:space-between'><span>Vector-Constraint Index &middot; {M['docRef']} &middot; v{M['version']} &middot; CC BY 4.0 &middot; doi.org/{M['doi']}</span><span>Page <span class='pageNumber'></span> of <span class='totalPages'></span></span></div>"
    pg.pdf(path=str(ROOT / "spec" / "Vector-Constraint_Index_VCI_v1.0-RC3.pdf"), format="Letter", print_background=True,
           display_header_footer=True, header_template="<div></div>", footer_template=foot,
           margin={"top": "0.62in", "bottom": "0.7in", "left": "0.66in", "right": "0.66in"})
    b.close()
print("ok")
