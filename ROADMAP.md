# Roadmap

Zenodo holds snapshots. Each version freezes VCI as it stood on its release date. This repository is the living copy between snapshots.

## 1. Blind validation run (freezes v1.0)
At least 20 historical cases with known outcomes, at least a third of them known failures, scored independently by two or more evaluators who have not seen the outcomes.

## 2. Agreement score per question
Each question gets a published agreement score (Cohen's kappa) from the blind run, so anyone can see which questions are solid and which are still being tightened.

## 3. Evidence tiers (RC4, open specification)
A standard for what counts as Yes at each question: a dated document from before the work counts; a document written after the work is late-registered; a verbal claim is Can't show it. When evaluators cannot agree, the burden rule decides: Can't show it counts as No. Questions with low agreement are fixed first.

## 4. Question Refiner and the VCI Evaluator's Handbook
The Question Refiner turns each question into evidence tiers with worked rulings: one clear Yes, one clear No, and one borderline case with its ruling. A draft for three benchmark questions (K3, K5, 1.3) is public in `evaluator/vci-refiner.js`. The complete library, covering every question with cross-domain precedents, is the VCI Evaluator's Handbook, with evaluator training for consistent audits.

## Ongoing
Every accepted break is credited in `CHANGELOG.md` and folded into the next snapshot. See `CONTRIBUTING.md`.
