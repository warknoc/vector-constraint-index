// vci-refiner.js : Question Refiner definitions.
// Question text lives in vci-config.js; this file holds only the refinement.
// A refinement tightens how a question is answered. It never changes the question.
window.VCI_REFINER = {

  K3: {
    ref: "forks.K3",
    kind: "Kill fork / Falsification",
    agreement: { metric: "Cohen's kappa", value: null, status: "pending blind run" },
    burdenRule: "Can't show it counts as No",
    tiers: [
      { tier: "A", answer: "yes",
        evidence: "A dated document from before the work (contract, proposal, ticket, protocol, registry) naming a specific, observable result that means failure.",
        flag: null },
      { tier: "B", answer: "no",
        evidence: "A dated pre-work document that names a goal but no failure result (for example, 'reduce outages').",
        reason: "A goal is not a failure condition.",
        flag: null },
      { tier: "C", answer: "no",
        evidence: "A failure condition written after work or spending started.",
        reason: "Late-registered. Stands as No for resources already spent.",
        flag: "LATE_REGISTERED", nextTranche: "allowed" },
      { tier: "D", answer: "cant",
        evidence: "A verbal statement, an after-the-fact email, or 'everyone knew'.",
        reason: "Nothing dated before the work can be shown.",
        flag: "UNVERIFIABLE" },
      { tier: "E", answer: "no",
        evidence: "Nothing.",
        reason: "No record provided.",
        flag: null }
    ],
    variants: {
      research: { tierA: "A dated protocol or registration, filed before data collection, stating the result that means 'no' and the analysis plan." }
    },
    examples: [
      { type: "clear-yes", tier: "A",
        text: "Contractor quote, dated before the job: 'If voltage at terminal B still sags below 11.5 V under load after the swap, the labor is free.'" },
      { type: "clear-no", tier: "B",
        text: "Program plan: 'Success will be measured by continued progress toward reduced incidents.'" },
      { type: "borderline", tier: "A",
        text: "Grant proposal: 'We expect a 20% reduction; results below 5% would suggest the approach needs revision.'",
        ruling: "Yes. A specific threshold (below 5%) was named in advance and tied to a consequence. Soft wording does not change that." }
    ]
  },

  K5: {
    ref: "forks.K5",
    kind: "Kill fork / End state",
    agreement: { metric: "Cohen's kappa", value: null, status: "pending blind run" },
    burdenRule: "Can't show it counts as No",
    tiers: [
      { tier: "A", answer: "yes",
        evidence: "A dated record stating the measurable condition where the solver's necessary involvement ends, in the form the claim type requires (see variants). Scheduled maintenance at a fixed interval and price, measured against a published decay or wear curve, may continue after it.",
        flag: null },
      { tier: "B", answer: "no",
        evidence: "A schedule, budget, or milestone list with no stated condition that ends the work.",
        reason: "A timeline or budget is not an end state. Work can hit every milestone and never finish.",
        flag: null },
      { tier: "C", answer: "no",
        evidence: "An end state first stated after work or spending started.",
        reason: "Late-registered. Stands as No for resources already spent.",
        flag: "LATE_REGISTERED", nextTranche: "allowed" },
      { tier: "D", answer: "cant",
        evidence: "Verbal assurance: 'we'll wrap up when it's fixed' or 'it'll be done when it's done'.",
        reason: "No dated record of what 'done' means.",
        flag: "UNVERIFIABLE" },
      { tier: "E", answer: "no",
        evidence: "Open-ended retainer, advisory, monitoring, or study with no end condition.",
        reason: "Ongoing by default. The Shirky pattern.",
        flag: null }
    ],
    variants: {
      solution:   { tierA: "The owner's K2 outcome reached, stated as the point involvement ends." },
      partial:    { tierA: "The stated fraction of the gap closed, stated as the point this work ends." },
      mitigation: { tierA: "A stated cost reduction plus a dated reassessment." },
      management: { tierA: "A metric for the ongoing work and a dated sunset review where it is cut if the metric has not moved. Inflow lane: the review also checks whether the source still exists." },
      research:   { tierA: "An end date and a named handoff: to a solver, or a declaration that this approach cannot solve it." },
      pilot:      { tierA: "A decision date to scale, change, or kill it." }
    },
    notes: "A stop-loss (for example, 'terminate if the cause is not found within 40 hours') is a failure condition, scored at K3. It is not an end state.",
    examples: [
      { type: "clear-yes", tier: "A",
        text: "Repair SOW: 'Job complete when the unit runs 72 hours under rated load with no fault codes. Final invoice issued at sign-off.'" },
      { type: "clear-no", tier: "B",
        text: "Charter: 'Phase 1 is estimated at 6 weeks and $25,000. Phase 2 scope to be determined.'" },
      { type: "borderline", tier: "A",
        text: "Monitoring contract, adaptive lane: 'Service continues while blocked intrusion attempts exceed 50 per month. Reviewed every 6 months; cancelled if the rate stays below 50 for two consecutive reviews.'",
        ruling: "Yes, for a management claim. It has a metric and a dated sunset review that can end it. The same wording on a Terminal problem would be Mislabeled at K1." }
    ]
  },

  "1.3": {
    ref: "gauntlet.1.3",
    kind: "Gauntlet (soft) / Cause isolation",
    agreement: { metric: "Cohen's kappa", value: null, status: "pending blind run" },
    burdenRule: "Can't show it counts as No",
    tiers: [
      { tier: "A", answer: "yes",
        evidence: "Recorded test data ruling out each named competing cause.",
        flag: null },
      { tier: "B", answer: "no",
        evidence: "A list of plausible causes with no recorded test ruling any of them out.",
        reason: "Naming alternatives is not eliminating them.",
        flag: null },
      { tier: "C", answer: "no",
        evidence: "Elimination tests run after the fix was chosen or installed, to support it.",
        reason: "Tests designed after the answer was picked tend to confirm it.",
        flag: "RETROSPECTIVE_BIAS" },
      { tier: "D", answer: "cant",
        evidence: "An assertion that other causes were checked informally, with nothing recorded.",
        reason: "Unrecorded checks cannot be audited.",
        flag: "UNVERIFIABLE" },
      { tier: "E", answer: "no",
        evidence: "A single-cause fix with no alternatives considered.",
        reason: "No elimination attempted.",
        flag: null }
    ],
    variants: {
      research: { tierA: "Confounders excluded by control conditions or pre-specified tests." }
    },
    examples: [
      { type: "clear-yes", tier: "A",
        text: "Bench log recording voltage drop across three alternative relay paths, each ruled out with measurements, before replacing the board controller." },
      { type: "clear-no", tier: "B",
        text: "Post-incident review: 'Team considered power surge, firmware bug, and a loose connector; swapped the connector.'" },
      { type: "borderline", tier: "A (partial)",
        text: "Timestamped oscilloscope capture showing clean ripple on Rail A. No written report. Two other named causes have no records.",
        ruling: "Rail A counts as ruled out: timestamped instrument data meets the evidence burden without a report. The question still fails until each other named cause has equivalent evidence." }
    ]
  }

};