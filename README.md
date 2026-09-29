# Vector-Constraint Index (VCI)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23039676.svg)](https://doi.org/10.5281/zenodo.23039676)

Latest version, all releases: https://doi.org/10.5281/zenodo.23039676 · This release (v1.0-RC3): https://doi.org/10.5281/zenodo.23039677

> "Institutions will try to preserve the problem to which they are the solution."
> Clay Shirky. Named the Shirky Principle by Kevin Kelly, 2010.

The Shirky Principle tells you problem preservation exists. The Vector-Constraint Index tells you where.

VCI is an open, deterministic test of whether a problem is actually being solved. Run any claim through it: a contractor's quote, a government program, a grant, a treatment plan, a subscription, or your own project. The same answers always give the same verdict.

## An invitation to falsify

This specification is published as **Release Candidate 3 (RC3)**.

The core mechanics (the Delgado Vector Law, the closure test, the six vector roles, and kill forks K0 to K6) have been run against five cases with known outcomes: smallpox, the 1955 malaria eradication programme, Guinea worm, polio, and the brown tree snake on Guam. In that run the framework broke one of its own assumptions: the brown tree snake's entry routes had not been counted. The fix is now part of the rules. That run was done by the author with outcomes already known. It is not the blind test that freezes v1.0.

No diagnostic tool is finished until it meets the adversarial world. This specification is published under CC BY 4.0, and the evaluator under the MIT License, so that anyone can try to break it. A gap found is the framework getting stronger.

1. **Submit an edge case.** If you have a proposal, public program, or contract whose lane the closure test cannot resolve, send the public documents.
2. **Report a wrong verdict.** If an effort that genuinely ended is marked Problem preserved, or an open-ended effort passes the kill forks unchecked, open an issue with the evidence.
3. **Meet the standard for change.** Any change to the core rules must name the documented case that exposed the failure and state the rule that fixes it. It must also rerun every prior benchmark case and report any verdict that changes, with the reason.

**Every accepted break is credited by name in the changelog**, unless the finder asks to stay anonymous. The first entry is the author's own: the brown tree snake correction in RC2.

Open an issue using one of the templates, or write to andrew.delgado@crea8or1.com with "VCI break" in the subject. See `CONTRIBUTING.md`.

The framework does not ask for trust. It asks to be tested. For where it stands today, see `ASSESSMENT.md`; for what comes next, see `ROADMAP.md`.

## What is here

| Path | What it is | License |
|---|---|---|
| `spec/` | The specification, v1.0-RC3 (PDF and HTML) | CC BY 4.0 |
| `evaluator/` | A tap-through evaluator. Open `index.html` in a browser. Questions and thresholds live in `vci-config.js`. | Code MIT; question text CC BY 4.0 |
| `ASSESSMENT.md` | An honest assessment of what is strong and what is not proven yet | |
| `ROADMAP.md` | What comes next, from the blind validation run to v1.0 | |
| `CONTRIBUTING.md` | How to submit a break, and what a rule change must show | |
| `tools/build_spec.py` | Rebuilds the spec from the question file (Python, Playwright) | Code MIT; generated text CC BY 4.0 |

## How it works, in one paragraph

VCI sets no standard: the outcome wanted by whoever bears the cost of the problem is the standard. The problem's vectors (source, entry, movement, regeneration, induced, adaptive) decide its lane: Terminal, Finite, Inflow, or Adaptive. Only Inflow doors and Adaptive problems may be legitimately ongoing, and only under a metric and a sunset review. Six kill forks stop a claim the moment it cannot pass: no measurable outcome, no failure condition written in advance, a failure already hit and patched over, no end state, or success measured on a metric the solver chose. Claims that survive answer a scored gauntlet. Verdicts describe structure, not intent.

## Status

Release candidate. v1.0 freezes after an independent blind validation run: at least 20 historical cases with known outcomes, at least a third of them known failures, scored by two or more evaluators who have not seen the outcomes. See the self-audit in the spec, Section 9.

## Names

Vector-Constraint Index™, VCI™, and Delgado Vector Law™ are trademarks of Creator 1 LLC. The licenses cover the work, not the names. See `TRADEMARKS.md`.

## Cite

Delgado, A. (2026). *The Vector-Constraint Index: A deterministic test of whether a problem is actually being solved* (Version 1.0-RC3). Zenodo. https://doi.org/10.5281/zenodo.23039677

See also `CITATION.cff`.

Author: Andrew Delgado, Creator 1 LLC · andrew.delgado@crea8or1.com
