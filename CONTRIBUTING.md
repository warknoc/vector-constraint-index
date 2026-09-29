# Breaking VCI

VCI gets stronger every time someone finds a gap. This page explains how to report one and what a fix has to show.

## Three kinds of report

**1. Edge case.** A real proposal, public program, or contract whose lane the closure test cannot resolve, or where the six vector roles do not fit. Use the *Edge case* issue template.

**2. Wrong verdict.** VCI marks an effort that genuinely ended as Problem preserved (a false alarm), or an open-ended effort passes the kill forks (a miss). Use the *Wrong verdict* issue template.

**3. Rule change.** A proposed change to the core rules. Use the *Rule change* issue template.

## Evidence rules

- Public documents only: contracts, budgets, audits, inspector general or GAO reports, published papers, press releases.
- Programs, agencies, organizations, and products. No private individuals.
- Quote the part of the source that answers the question at issue.
- State any stake you hold in the case.

## The standard for change

A change to the core rules is accepted only if it:

1. Names the documented case that exposed the failure.
2. States the rule that fixes it, in the spec's own terms.
3. Reruns every prior benchmark case and reports any verdict that changes, with the reason.

A change that alters a prior verdict is not rejected for that reason. RC2 changed the brown tree snake's lane, and that change was correct. It is rejected only if the new verdict is not supported by the evidence.

## Credit

Every accepted break is credited by name in `CHANGELOG.md`, unless you ask to stay anonymous.

## Licensing of contributions

Text contributed to the specification is contributed under CC BY 4.0. Code contributed to the evaluator or tools is contributed under the MIT License. Contributions do not transfer any rights to the names Vector-Constraint Index, VCI, or Delgado Vector Law. See `TRADEMARKS.md`.

Contact: andrew.delgado@crea8or1.com, subject line "VCI break".
