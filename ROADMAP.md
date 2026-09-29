# Roadmap

Zenodo holds snapshots. Each version freezes VCI as it stood on its release date. This repository is the living copy between snapshots.

## 1. Blind validation run (freezes v1.0)
At least 20 historical cases with known outcomes, at least a third of them known failures, scored independently by two or more evaluators who have not seen the outcomes.

## 2. Agreement score per question
Each question gets a published agreement score (Cohen's kappa) from the blind run, so anyone can see which questions are solid and which are still being tightened.

## 3. Evidence tiers (RC4, open specification)
A standard for what counts as Yes at each question: a dated document from before the work counts; a document written after the work is late-registered; a verbal claim is Can't show it. When evaluators cannot agree, the burden rule decides: Can't show it counts as No. Questions with low agreement are fixed first.

## 4. VCI Evaluator's Handbook (add-on)
A worked-examples library for the questions that need it most (one clear Yes, one clear No, one borderline case with its ruling), plus evaluator training for consistent audits.

## Ongoing
Every accepted break is credited in `CHANGELOG.md` and folded into the next snapshot. See `CONTRIBUTING.md`.
