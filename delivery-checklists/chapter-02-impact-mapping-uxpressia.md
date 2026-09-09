# Chapter II — UXPressia Impact Mapping Completion Guide

## Purpose

Use this guide to convert the professor-facing basis in
`report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.2-impact-mapping.md`
into a final, evidence-backed UXPressia map. This file is operational guidance;
it is not report content and must not be exported to the PDF.

## Inputs that must exist first

For each validated User Persona, collect only fields supported by evidence:

- [ ] Supporting interview participant IDs.
- [ ] Research segment.
- [ ] Role.
- [ ] Demographics supported by actual evidence.
- [ ] Context and background.
- [ ] Goals.
- [ ] Frustrations.
- [ ] Observable behaviors.
- [ ] Devices.
- [ ] Channels.
- [ ] Needs.
- [ ] Quote, only when actually obtained.
- [ ] Evidence source.

No invented names, demographics, quotes, baselines, targets or dates.

## User Persona completion checklist

Complete one or more evidence-backed Personas for each research segment:

### Field & Warehouse Operations

- [ ] Persona maps to actual research participants.
- [ ] Warehouse and Dispatch responsibilities remain distinguishable.
- [ ] Physical work, handoffs, evidence and connectivity are supported by evidence.

### Delivery Workforce

- [ ] Persona maps to actual Driver / Delivery Operator evidence.
- [ ] Delivery attempt, outcome, POD and discrepancy work are distinguished.
- [ ] Navigation and location assumptions have explicit evidence or remain hypotheses.

### B2B Buyers

- [ ] Persona maps to actual Customer Buyer / B2B Buyer evidence.
- [ ] Buyer Relationship remains distinct from Customer Account and Human Identity.
- [ ] Receipt, discrepancy and commercial behaviors are supported separately.

Business Operations Manager remains a transversal role unless Needfinding evidence
justifies a separate Persona.

## SMART Business Goal worksheet

Complete one worksheet for each final goal:

| Element | Evidence-backed answer |
| :--- | :--- |
| Specific | What business result changes? |
| Measurable | Which observable metric measures that result? |
| Baseline | What is the measured starting point? |
| Target | What measured result is desired? |
| Achievable | Why is the target defensible? |
| Relevant | Which validated business problem or outcome does it address? |
| Time-bound | By when is the target expected? |
| Evidence source | Which interview, dataset, experiment or decision supports baseline and target? |

If no baseline exists, write `RESEARCH REQUIRED` in the working worksheet. Do not
guess a baseline or target.

## Recommended goal design process

1. [ ] Start from validated business problem and Lean UX outcomes.
2. [ ] Select several measurable business outcomes.
3. [ ] Establish the actual baseline.
4. [ ] Define the target.
5. [ ] Define the time window.
6. [ ] Confirm relevance with Personas and project objective.
7. [ ] Validate with the team.
8. [ ] Declare the goal SMART only after all fields have evidence.

## Impact Mapping construction process in UXPressia

For every Business Goal:

1. [ ] Create the Goal.
2. [ ] Add relevant Persona or Personas.
3. [ ] For each Persona, identify behavioral Impact(s).
4. [ ] For each Impact, identify Deliverable(s).
5. [ ] For each Deliverable, associate the approved User Stories.
6. [ ] Paste the full story wording, preserving `Como ... deseo ... para ...`.
7. [ ] Verify the chain reads logically: Goal -> Persona -> Behavior -> Deliverable -> Story.

## Quality questions

For every Impact:

- [ ] Is this a behavior change?
- [ ] Could the behavior be observed or asked about in research?
- [ ] Is it accidentally a feature, screen, API or implementation detail?

For every Deliverable:

- [ ] Can the digital product provoke or support the Impact?
- [ ] Is it a deliverable rather than a business outcome?
- [ ] Does it preserve server and Bounded Context authority?

For every Story:

- [ ] Does it actually implement or support the Deliverable?
- [ ] Is the full `Como ... deseo ... para ...` wording present?
- [ ] Does its Acceptance Criteria remain in 2.4.1 rather than being duplicated here?

## Screenshot evidence

The final evidence must show:

- [ ] Complete Impact Map.
- [ ] Goal, Persona, Impact, Deliverable and Story visible.
- [ ] Readable at report scale.
- [ ] No critical content cropped.
- [ ] No private browser, account or workspace data exposed.

## Public link

Record the real value only after publication:

```text
UXPressia public URL: <TO BE COMPLETED BY HUMAN>
```

Do not insert a guessed URL.

## Report insertion checklist

When the map is complete:

1. [ ] Export or capture the final Impact Map.
2. [ ] Place the actual evidence asset under the approved Chapter II asset path.
3. [ ] Update `2.4.2-impact-mapping.md` with the final evidence.
4. [ ] Replace provisional outcome wording only where the evidence supports it.
5. [ ] Include the actual public URL, if available and required.
6. [ ] Validate local Markdown links.
7. [ ] Review PDF readability.
8. [ ] Preserve evidence provenance outside `report/assets/**`.

## Final rubric gate

Do not call 2.4.2 final until all answers are `YES`:

| Gate | YES / NO |
| :--- | :---: |
| Several SMART Business Goals |  |
| Validated User Personas |  |
| Persona -> Goal mapping |  |
| Behavioral Impacts |  |
| Deliverables |  |
| Full User Story text |  |
| UXPressia capture |  |
| Public or evidence link |  |
