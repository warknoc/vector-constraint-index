/* Vector-Constraint Index question file. Copyright (c) 2026 Andrew Delgado. Text: CC BY 4.0. Code structure: MIT. Edit thresholds and question text here; the evaluator logic reads this file. */
window.VCI_CONFIG = {
  "meta": {
    "name": "Vector-Constraint Index",
    "short": "VCI",
    "version": "1.0-RC3",
    "docRef": "C1-VCI-SPEC-2026.1",
    "date": "September 29, 2026",
    "author": "Andrew Delgado, Creator 1 LLC",
    "license": "CC BY 4.0",
    "doi": "10.5281/zenodo.23039677",
    "status": "Release candidate. Freezes as v1.0 after an independent blind validation run."
  },
  "thresholds": {
    "genuineMaxSoftFails": 0,
    "gapsMaxSoftFails": 4
  },
  "answers": {
    "yes": "Yes",
    "no": "No",
    "cant": "Can't show it",
    "na": "Does not apply"
  },
  "stages": {
    "before": {
      "label": "Before resources are committed",
      "note": "Escape hatches are open. A solver who fixes a gap now proceeds clean."
    },
    "after": {
      "label": "After resources are committed",
      "note": "Escape hatches are closed for what was already spent. A stop verdict stands for that spend. The solver may resubmit the next tranche as a fresh claim, with this result on record."
    }
  },
  "claimTypes": {
    "solution": {
      "label": "Solution",
      "does": "Closes the gap between the current state and the owner's desired state.",
      "end": "The owner's outcome is reached and the solver's necessary involvement ends, apart from defined maintenance."
    },
    "partial": {
      "label": "Partial solution",
      "does": "Closes a stated, measured part of the gap.",
      "end": "The stated fraction is reached."
    },
    "mitigation": {
      "label": "Mitigation",
      "does": "Reduces what the gap costs the owner. The gap stays open.",
      "end": "A stated cost reduction is reached, then a dated reassessment."
    },
    "management": {
      "label": "Management",
      "does": "Holds an ongoing problem steady: an Adaptive problem, or the doors of an Inflow problem.",
      "end": "A metric plus a dated sunset review where the work is cut if the metric has not moved."
    },
    "research": {
      "label": "Research",
      "does": "Answers a question about the gap.",
      "end": "The answer is delivered, then handed to a solver or the approach is declared unable to solve it."
    },
    "pilot": {
      "label": "Pilot",
      "does": "Tries an approach at small scale to inform a decision.",
      "end": "A decision date: scale it, change it, or kill it."
    }
  },
  "lanes": {
    "terminal": {
      "label": "Terminal",
      "rule": "The source can be eliminated, and every entry and movement route passes through one shared constraint. Interdict the constraint and the problem closes. Terminal means an end exists, not that it is cheap or fast."
    },
    "finite": {
      "label": "Finite",
      "rule": "The source can be eliminated, and the routes are a fixed, countable set with no shared constraint. The problem closes when all N are closed. Progress is counted X of N."
    },
    "inflow": {
      "label": "Inflow",
      "rule": "The agent comes from a permanent source outside the owner's reach, through a finite set of doors. The interior closes like a Terminal or Finite problem. The doors stay ongoing, under a metric and a sunset review tied to the source."
    },
    "adaptive": {
      "label": "Adaptive",
      "rule": "The problem can invent new routes on its own (a thinking adversary, mutation, resistance). Ongoing work is legitimate here, but only with a metric and a sunset review."
    }
  },
  "verdicts": {
    "OUT_OF_SCOPE": {
      "title": "Outside VCI scope",
      "kind": "neutral",
      "principle": "",
      "meaning": "No resources are being spent against a problem someone bears the cost of. Nothing here claims to solve anything, so there is nothing to test."
    },
    "MISLABELED": {
      "title": "Mislabeled claim",
      "kind": "stop",
      "principle": "Delgado Vector Law",
      "meaning": "The claim is sold as one type and delivers another, or ongoing management is sold on a problem that has an end. Every claim type is legitimate when named honestly. The disguise is what fails."
    },
    "NOT_TESTABLE": {
      "title": "Not a testable claim",
      "kind": "stop",
      "principle": "Hypothetico-deductive method",
      "meaning": "There is no measurable outcome the owner agreed to. Nothing can be tested, so nothing can be shown to work."
    },
    "UNFALSIFIABLE": {
      "title": "Unfalsifiable",
      "kind": "stop",
      "principle": "Popper, 1934/1959; Rosenthal, 1979",
      "meaning": "No result was named in advance that would prove the approach wrong, or unwelcome results are not reported. A claim that cannot fail cannot be shown to succeed."
    },
    "PRESERVED": {
      "title": "Problem preserved",
      "kind": "stop",
      "principle": "Shirky Principle; Lakatos, 1970",
      "meaning": "The structure keeps the problem open: no exit condition, a failure already hit and patched over, or phases that never narrow. This verdict describes the structure, not anyone's intent."
    },
    "MOVED_GOALPOSTS": {
      "title": "Moved the goalposts",
      "kind": "stop",
      "principle": "Goodhart, 1975; Campbell, 1976",
      "meaning": "Success is being measured on a metric the solver introduced, not the outcome the owner asked for."
    },
    "GENUINE": {
      "title": "Genuine attempt",
      "kind": "pass",
      "principle": "",
      "meaning": "Passed every kill fork and every gauntlet question. This is a real, testable attempt at the owner's outcome, with a defined end."
    },
    "GAPS": {
      "title": "Credible, with gaps",
      "kind": "gaps",
      "principle": "",
      "meaning": "Passed every kill fork. A few gauntlet questions failed. Push on those before committing more resources."
    },
    "UNPROVEN": {
      "title": "Unproven",
      "kind": "warn",
      "principle": "",
      "meaning": "Passed the kill forks but failed many gauntlet questions. The claim is not yet supported well enough to fund as a solution."
    }
  },
  "intake": {
    "K0": {
      "q": "Are resources being spent or requested while someone bears the cost of the problem?",
      "plain": "Is anyone paying, in money, time, trust, or harm, while this effort goes on?",
      "evidence": "Yes when there is a budget, contract, grant, subscription, program, or ongoing ask of any kind. The label on the effort (study, pilot, case study, partnership) does not matter.",
      "source": "Shirky Principle (Shirky; named by Kelly, 2010)"
    }
  },
  "laneQuestions": {
    "V0": {
      "q": "Are all six vector roles listed: source, entry, movement, regeneration, induced, and adaptive?",
      "plain": "Where does it come from, how does it get in, how does it move, how does it come back, what does the fix itself open up, and can it invent new routes?",
      "evidence": "Yes when each role has a written answer, even if the answer is 'none'. Leaving a role blank is how entry routes get missed.",
      "followup": "Answer all six vector roles in writing: source, entry, movement, regeneration, induced, adaptive.",
      "source": "Delgado Vector Law"
    },
    "VC": {
      "q": "Was the vector count N set with the closure test, with each counted vector backed by a record?",
      "plain": "Routes that one fix closes count as one. A route still open after a fix is its own vector. Each one needs evidence.",
      "evidence": "Yes when N is the smallest number of independent closures that shut every route, and each counted vector has a record (interceptions, detections, genetic tracing, incident data). Suspected vectors are listed separately, with the test that would confirm them, and are not counted.",
      "followup": "Count the vectors with the closure test and show the record behind each one.",
      "source": "Delgado Vector Law; derived from dimensional reduction (Buckingham, 1914)"
    },
    "L1": {
      "q": "Can the problem invent new routes on its own, through a thinking adversary, mutation, or resistance?",
      "plain": "Does the problem fight back and find new routes?",
      "evidence": "Yes only with evidence of new routes appearing over time. A claim that it might adapt, with no record of it, counts as No. A route the intervention itself creates is an Induced vector and must be counted, but it does not make the problem Adaptive.",
      "source": "Delgado Vector Law"
    },
    "VS": {
      "q": "Does the agent come from a permanent source outside the owner's reach, shown by evidence?",
      "plain": "Is there a supply of the problem outside the fence that nobody will ever remove?",
      "evidence": "Yes when the source is shown to be permanent and out of reach: a native population in its home range, another jurisdiction, a natural reservoir. A source is not permanent because nobody has funded removing it. Lack of money or will is a neglect finding, never a vector or a lane.",
      "source": "Delgado Vector Law; reference: smallpox import risk before global eradication"
    },
    "L2": {
      "q": "Do all routes, entry and movement alike, pass through one shared physical constraint?",
      "plain": "Is there one thing every route in and every route around has to go through?",
      "evidence": "Yes when the shared constraint is named and every counted vector, including every entry route, is shown to pass through it. How an agent moves and how it gets in are counted separately: a constraint on movement does not close a door.",
      "source": "Delgado Vector Law; Goldratt, 1984"
    }
  },
  "mislabel": {
    "M1": {
      "q": "Does what the solver will actually deliver match the claim type they named?",
      "plain": "Is it really what they say it is?",
      "evidence": "No when a mitigation or management effort is presented as a solution, when research is presented as a fix, or when a pilot has been renewed without a decision. If it is a pilot renewed without a decision, re-run it as the claim type it has become.",
      "followup": "State which claim type this actually is: solution, partial solution, mitigation, management, research, or pilot.",
      "source": "VCI claim types"
    },
    "M2": {
      "q": "Does the solution name the specific sub-problem it closes completely?",
      "plain": "The whole problem keeps going. Which part does this actually finish?",
      "evidence": "Yes when the claim names a sub-problem with its own Terminal or Finite lane (one class of software flaw, one fenced area, the interior of an island behind its doors). A solution claimed against a whole Adaptive or Inflow problem counts as No.",
      "followup": "Name the sub-problem this closes, and show that sub-problem has an end.",
      "source": "VCI decomposition rule"
    },
    "M3": {
      "q": "Is the ongoing work limited to the doors, with the interior handled as a problem that closes?",
      "plain": "Ongoing work is earned at the doors. Is anything inside the fence being kept open too?",
      "evidence": "No when ongoing management covers interior ground that could be cleared and closed.",
      "followup": "Limit the ongoing work to the doors and state the end state for the interior.",
      "source": "Delgado Vector Law (Inflow lane)"
    }
  },
  "forks": {
    "K2": {
      "title": "Desired outcome",
      "q": {
        "default": "Is the owner's desired outcome stated as a number or clear observable, and has the owner agreed to it?",
        "mitigation": "Is the cost reduction the owner wants stated as a number or clear observable, and has the owner agreed to it?",
        "research": "Is the question stated, together with the decision its answer will feed?",
        "pilot": "Is the decision the pilot will inform stated (scale, change, or kill), with the measurement that will decide it?"
      },
      "plain": "What exactly counts as fixed, and who agreed to that?",
      "evidence": "The owner is whoever bears the cost of the problem, not necessarily whoever funds the solver. Where millions bear the cost, the measured harm (incidents, losses, exposures) stands in for them. A body that claims to speak for owners counts only if it does not also fund or run the solver.",
      "escape": "State the outcome now as a number or observable and have the owner sign off.",
      "followup": "What number or observable, agreed by the people who bear the cost, means this is done?",
      "fail": "NOT_TESTABLE",
      "source": "Hypothetico-deductive method; Heilmeier Catechism"
    },
    "K3": {
      "title": "Failure condition",
      "q": {
        "default": "Was a result that would prove the approach wrong written down before work or resources began?",
        "research": "Were the result that means 'no' and the analysis plan written down before data was collected?"
      },
      "plain": "Before starting, did they say what result means they were wrong?",
      "evidence": "Yes only with a dated record (quote, contract, proposal, ticket, protocol, registry) that predates the work.",
      "escape": "State the failure condition now and agree to be held to it.",
      "followup": "What result would prove this approach wrong, and where is it written down with a date?",
      "fail": "UNFALSIFIABLE",
      "source": "Popper, 1934/1959; pre-registration (Ioannidis, 2005)"
    },
    "K3R": {
      "title": "Full reporting",
      "onlyFor": [
        "research",
        "pilot"
      ],
      "q": {
        "default": "Are all results, positive and negative, reported to the owner?"
      },
      "plain": "Do they share the bad results too?",
      "evidence": "No when only favorable results are published or reported.",
      "escape": null,
      "followup": "Report every result, including the negative ones.",
      "fail": "UNFALSIFIABLE",
      "source": "Rosenthal, 1979 (file drawer problem)"
    },
    "K4": {
      "title": "Failure already hit",
      "q": {
        "default": "Is the effort clear of a failure it already hit? Its stated failure result has not happened, and no prior effort by this solver on this problem, using this approach, hit its failure condition and carried on.",
        "research": "Is the effort clear of a reframed 'no'? The answer has not already come back 'no' and then been presented as promising."
      },
      "plain": "Did they already hit their own wall and keep going with new explanations?",
      "evidence": "No when the failure condition was met and the effort continued with new explanations, new 'hidden issues', or a changed environment that was not predicted in advance.",
      "escape": null,
      "reentry": "A genuinely new approach can re-enter at K2 as a fresh claim, with this failure on its record.",
      "followup": "Your stated failure condition was met. What is different about the new approach, and what is its new failure condition?",
      "fail": "PRESERVED",
      "source": "Lakatos, 1970 (degenerating research programme)"
    },
    "K5": {
      "title": "End state",
      "q": {
        "solution": "Is there a measurable condition where the solver's necessary involvement ends, apart from defined maintenance?",
        "partial": "Is there a measurable condition, the stated fraction of the gap closed, where this work ends?",
        "mitigation": "Is there a stated cost reduction and a dated reassessment?",
        "management": "Is there a metric for the ongoing work and a dated sunset review where it is cut if the metric has not moved? In the Inflow lane, the review also checks whether the source still exists.",
        "research": "Is there an end date and a named handoff: to a solver, or a declaration that this approach cannot solve it?",
        "pilot": "Is there a decision date to scale, change, or kill it?"
      },
      "plain": "When does this end?",
      "evidence": "Defined maintenance (fixed interval, fixed price, measured against a published decay or wear curve) does not count against an end state. Open-ended advisory, study, or monitoring does.",
      "escape": "State the end condition now.",
      "followup": "What measurable condition ends your involvement, and when?",
      "fail": "PRESERVED",
      "source": "Shirky Principle; NASA NPR 7120.5 key decision points"
    },
    "K5R": {
      "title": "Perpetual study",
      "onlyFor": [
        "research"
      ],
      "q": {
        "default": "Is this a new question, or a narrower one than any already answered? (Not the same question asked again, and not a wider one.)"
      },
      "plain": "Are they studying something already studied, just again?",
      "evidence": "'Further research needed' is allowed once, and only with a narrower question.",
      "escape": null,
      "followup": "Which earlier answer does this build on, and how is the question narrower?",
      "fail": "PRESERVED",
      "source": "Lakatos, 1970; Platt, 1964"
    },
    "K6": {
      "title": "Same yardstick",
      "q": {
        "default": "Is success measured on the owner's outcome from K2, not on a metric the solver introduced later?",
        "research": "Does the work answer the original question, not a new one swapped in?"
      },
      "plain": "Are they grading themselves on the thing you asked for?",
      "evidence": "No when the reported success is activity (hours, scans, meetings, reports produced) or a proxy the solver picked, instead of the owner's outcome.",
      "escape": null,
      "followup": "Show the result on the outcome the owner asked for.",
      "fail": "MOVED_GOALPOSTS",
      "source": "Goodhart, 1975; Campbell, 1976"
    }
  },
  "gauntlet": [
    {
      "id": "1.1",
      "gate": "1 Problem definition",
      "q": "Was the owner's outcome measured before work began, to set a baseline?",
      "plain": "What did it look like before they touched it?",
      "evidence": "A dated measurement of the K2 outcome.",
      "followup": "Show the baseline measurement and its date.",
      "source": "Hypothetico-deductive method",
      "na": false
    },
    {
      "id": "1.2",
      "gate": "1 Problem definition",
      "q": "Are two or more competing causes named?",
      "plain": "What else could be causing it?",
      "evidence": "At least two alternatives to the favored cause, in writing.",
      "followup": "What else could explain the problem?",
      "source": "Chamberlin, 1890 (multiple working hypotheses)",
      "na": false,
      "skipFor": [
        "research"
      ]
    },
    {
      "id": "1.3",
      "gate": "1 Problem definition",
      "q": "Was each competing cause ruled out by a test?",
      "plain": "How did they rule the others out?",
      "evidence": "A test or measurement per alternative. 'Experience' does not count.",
      "followup": "Which test ruled out each alternative?",
      "source": "Platt, 1964 (strong inference)",
      "na": false,
      "skipFor": [
        "research"
      ]
    },
    {
      "id": "1.4",
      "gate": "1 Problem definition",
      "q": "Is the current approach stated, with why it falls short?",
      "plain": "How is it done today, and what is wrong with that?",
      "evidence": "A named current method and its measured limit.",
      "followup": "How is this handled today, and where does that fall short?",
      "source": "Heilmeier Catechism",
      "na": false
    },
    {
      "id": "1.5",
      "gate": "1 Problem definition",
      "q": "Is it stated what is new compared with past attempts?",
      "plain": "What is different this time?",
      "evidence": "A specific difference, not 'better' or 'innovative'.",
      "followup": "What is new here compared with what was tried before?",
      "source": "Heilmeier Catechism",
      "na": false
    },
    {
      "id": "1.6",
      "gate": "1 Problem definition",
      "q": "Is the payoff stated: who benefits, and by how much, if it works?",
      "plain": "Who cares, and what changes for them?",
      "evidence": "A named beneficiary and a measurable difference.",
      "followup": "Who benefits if this works, and by how much?",
      "source": "Heilmeier Catechism",
      "na": false
    },
    {
      "id": "2.1",
      "gate": "2 Falsification",
      "q": "Does the solver state what they lose if the failure condition is met?",
      "plain": "What does it cost them to be wrong?",
      "evidence": "A refund, unpaid labor, a performance hold-back, a public result, or similar.",
      "followup": "What do you give up if your failure condition is met?",
      "source": "Taleb, 2018 (skin in the game)",
      "na": false
    },
    {
      "id": "3.1",
      "gate": "3 Boundary",
      "q": "Is the governing variable or constraint named?",
      "plain": "What is the one thing driving the failure?",
      "evidence": "One variable, or a tight group with a reason.",
      "followup": "Which variable actually drives the failure?",
      "source": "Derived from dimensional reduction (Buckingham, 1914)",
      "na": false
    },
    {
      "id": "3.2",
      "gate": "3 Boundary",
      "q": "Are exclusions stated: what the effort deliberately leaves out, and why?",
      "plain": "What are they not touching?",
      "evidence": "A written list of what is out of scope. An untreated route or refuge inside the boundary must appear here with a reason, or it is a neglect finding.",
      "followup": "What is deliberately out of scope, and why?",
      "source": "Derived from dimensional reduction (Buckingham, 1914)",
      "na": false
    },
    {
      "id": "3.3",
      "gate": "3 Boundary",
      "q": "Is it defined where the fix physically or logically stops?",
      "plain": "Where does their fix end?",
      "evidence": "A named part, circuit, area, process, or population.",
      "followup": "Where exactly does the fix stop?",
      "source": "Derived from dimensional reduction (Buckingham, 1914)",
      "na": false
    },
    {
      "id": "3.4",
      "gate": "3 Boundary",
      "q": "Is the scope unchanged since the start, or is each change tied to a named finding?",
      "plain": "Has the job grown, and if so, why?",
      "evidence": "No when scope grew without a finding that required it.",
      "followup": "Which finding required each scope change?",
      "source": "Derived from dimensional reduction (Buckingham, 1914)",
      "na": false
    },
    {
      "id": "4.1",
      "gate": "4 Verification",
      "q": "Is a spec, drawing, protocol, or standard named that the work is built to?",
      "plain": "What were they building it to?",
      "evidence": "A named document. 'Industry best practice' does not count.",
      "followup": "Which spec or standard is this built to?",
      "source": "IEEE Std 1012 (verification)",
      "na": false
    },
    {
      "id": "4.2",
      "gate": "4 Verification",
      "q": "Does measured data show the spec was met?",
      "plain": "Show the numbers, not a signed checklist.",
      "evidence": "Test logs, measurements, inspection records.",
      "followup": "Show the measured data against the spec.",
      "source": "IEEE Std 1012 (verification)",
      "na": false,
      "skipFor": [
        "research"
      ]
    },
    {
      "id": "5.1",
      "gate": "5 Validation",
      "q": "Was it tested under the same conditions that caused the failure?",
      "plain": "Did they test it where it actually breaks?",
      "evidence": "Same load, weather, traffic, population, or use. Bench-only counts as No.",
      "followup": "Test it under the conditions where the failure happens.",
      "source": "IEEE Std 1012 (validation)",
      "na": true,
      "naNote": "Does not apply only if no field results exist yet. Bench results test Gate 4, not Gate 5 or 6."
    },
    {
      "id": "5.2",
      "gate": "5 Validation",
      "q": "Has it run clean for longer than the old interval between failures?",
      "plain": "Has it held longer than it used to last?",
      "evidence": "Clean time measured against the historical failure interval.",
      "followup": "How long has it run clean, compared with how often it used to fail?",
      "source": "IEEE Std 1012 (validation)",
      "na": true,
      "naNote": "Does not apply only if no field results exist yet. Bench results test Gate 4, not Gate 5 or 6.",
      "skipFor": [
        "research"
      ]
    },
    {
      "id": "6.1",
      "gate": "6 Control",
      "q": "Does the failure return with the fix removed and stop with it restored, or is a safe equivalent shown?",
      "plain": "Take it out, does the problem come back? Put it back, does it stop?",
      "evidence": "A reversal test, a control group or area, or a documented reason reversal is unsafe plus the next-best comparison.",
      "followup": "Show that removing the fix brings the failure back, or show a control comparison.",
      "source": "ABAB reversal design (Barlow and Hersen, 1984); Mill, 1843",
      "na": true,
      "naNote": "Does not apply only if no field results exist yet. Bench results test Gate 4, not Gate 5 or 6."
    },
    {
      "id": "6.2",
      "gate": "6 Control",
      "q": "Are other changes made at the same time accounted for?",
      "plain": "Did anything else change that could explain it?",
      "evidence": "A list of concurrent changes and why each is ruled out.",
      "followup": "What else changed at the same time, and how is each ruled out?",
      "source": "Mill, 1843 (method of difference)",
      "na": true,
      "naNote": "Does not apply only if no field results exist yet. Bench results test Gate 4, not Gate 5 or 6."
    },
    {
      "id": "7.1",
      "gate": "7 Progress",
      "q": "Did the last phase eliminate at least one candidate cause or option?",
      "plain": "What is ruled out now that was not before?",
      "evidence": "Named candidates removed. The count of eliminated candidates must rise every phase.",
      "followup": "Which candidate causes did the last phase rule out?",
      "source": "Bayesian confirmation; Platt, 1964",
      "na": true,
      "naNote": "Does not apply to a single-phase effort."
    },
    {
      "id": "7.2",
      "gate": "7 Progress",
      "q": "Did the last round produce a specific finding that changed the plan?",
      "plain": "What did the last round of spending teach them?",
      "evidence": "A named finding. 'We gathered more data' does not count.",
      "followup": "What did the last phase find that changed the plan?",
      "source": "Bayesian confirmation",
      "na": true,
      "naNote": "Does not apply to a single-phase effort."
    },
    {
      "id": "7.3",
      "gate": "7 Progress",
      "q": "Is the next phase narrower than the last?",
      "plain": "Is each step smaller and more targeted?",
      "evidence": "A smaller scope, fewer candidates, or a tighter question.",
      "followup": "How is the next phase narrower than the last one?",
      "source": "Bayesian confirmation",
      "na": true,
      "naNote": "Does not apply to a single-phase effort."
    },
    {
      "id": "7.4",
      "gate": "7 Progress",
      "fatal": "PRESERVED",
      "q": "Has the effort avoided two consecutive phases that eliminated nothing?",
      "plain": "Two rounds in a row with nothing ruled out is a fishing trip.",
      "evidence": "No when two phases in a row ended with no candidate eliminated while uncertainty held or widened. A real discovery collapses old candidates, so honest work passes this.",
      "followup": "Two phases in a row ruled nothing out. What will the next phase eliminate, or when does it stop?",
      "source": "Lakatos, 1970; Bayesian confirmation",
      "na": true,
      "naNote": "Does not apply with fewer than two completed phases."
    },
    {
      "id": "8.1",
      "gate": "8 End state",
      "q": "Is there a date or milestone for reaching the end state?",
      "plain": "When?",
      "evidence": "A calendar date or a dated milestone.",
      "followup": "What is the date or milestone for reaching the end state?",
      "source": "Heilmeier Catechism; NASA NPR 7120.5",
      "na": false
    },
    {
      "id": "8.2",
      "gate": "8 End state",
      "q": "Is the total cost to the end state stated?",
      "plain": "How much, all in?",
      "evidence": "A total, not a monthly rate with no end.",
      "followup": "What is the total cost to reach the end state?",
      "source": "Heilmeier Catechism",
      "na": false
    },
    {
      "id": "8.3",
      "gate": "8 End state",
      "lanes": [
        "finite",
        "inflow"
      ],
      "q": "Are closures counted, X of N vectors closed (or, at Inflow doors, X of N doors covered)?",
      "plain": "How many routes are shut, out of how many?",
      "evidence": "A count against the counted vector list from VC.",
      "followup": "How many of the N vectors are closed so far?",
      "source": "Delgado Vector Law",
      "na": false
    },
    {
      "id": "8.4",
      "gate": "8 End state",
      "q": "If there is recurring maintenance, is it fixed interval, fixed price, and measured against a published decay or wear curve?",
      "plain": "Is the upkeep scheduled and priced, or open-ended?",
      "evidence": "No when recurring work is open-ended advisory, study, or monitoring.",
      "followup": "Put the maintenance on a fixed interval and price, tied to a published decay curve.",
      "source": "VCI maintenance rule",
      "na": true,
      "naNote": "Does not apply when there is no recurring maintenance."
    }
  ],
  "trackRecord": {
    "gate": "T Track record",
    "entry": {
      "q": "Does the solver have prior offers on this problem or similar ones?",
      "plain": "Have they promised this before?",
      "evidence": "A solver with no prior offers is flagged 'No record' and is not penalized. Track record questions are skipped for them.",
      "source": "Reference class forecasting (Kahneman and Tversky, 1979; Flyvbjerg, 2006)"
    },
    "questions": [
      {
        "id": "T1",
        "q": "Are the prior offers listed?",
        "plain": "What did they offer before?",
        "evidence": "Offer, date, and owner for each.",
        "followup": "List your prior offers on this or similar problems.",
        "source": "Reference class forecasting (Flyvbjerg, 2006)",
        "na": false
      },
      {
        "id": "T2",
        "q": "For each prior offer, is the promised result shown next to the measured result?",
        "plain": "What did they promise, and what actually happened?",
        "evidence": "Promised versus delivered, side by side.",
        "followup": "Show what each prior offer promised next to what it delivered.",
        "source": "Reference class forecasting (Flyvbjerg, 2006)",
        "na": false
      },
      {
        "id": "T3",
        "q": "Did most prior offers deliver what they promised?",
        "plain": "Do they usually deliver?",
        "evidence": "More than half delivered the promised result.",
        "followup": "Most prior offers missed. What is different now?",
        "source": "Reference class forecasting (Kahneman and Tversky, 1979)",
        "na": false
      },
      {
        "id": "T4",
        "q": "Did prior work finish within the promised cost and time?",
        "plain": "Were they on budget and on time?",
        "evidence": "Actual versus promised cost and schedule.",
        "followup": "Prior work overran. What makes this estimate more reliable?",
        "source": "Reference class forecasting (Flyvbjerg, 2006)",
        "na": false
      },
      {
        "id": "T5",
        "q": "Did any prior engagement reach its end state and actually end?",
        "plain": "Have they ever finished a job and left?",
        "evidence": "At least one closed engagement.",
        "followup": "Name one engagement you finished and exited.",
        "source": "Shirky Principle",
        "na": false
      }
    ]
  },
  "vectorRoles": [
    {
      "role": "Source",
      "q": "Where does the agent come from, and can it be eliminated?"
    },
    {
      "role": "Entry",
      "q": "How does it get inside the boundary?"
    },
    {
      "role": "Movement",
      "q": "How does it move once inside?"
    },
    {
      "role": "Regeneration",
      "q": "How does it replace itself inside?"
    },
    {
      "role": "Induced",
      "q": "What routes does the intervention itself create?"
    },
    {
      "role": "Adaptive",
      "q": "Can it invent new routes?"
    }
  ]
};
