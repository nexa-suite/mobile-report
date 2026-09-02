# Team identity register

## Purpose

This is the commit-ownership intake derived from the canonical prompt. The
current handoff explicitly confirms the five project identities and supplies
their project commit emails. Those emails are recorded as
`OWNER-CONFIRMED PROJECT COMMIT EMAIL`, not as GitHub-verified email evidence.
Identity resolution does not resolve ownership of every diff; each logical
unit still needs an owner review and explicit commit authorization.

| Canonical person | GitHub username | Supplied commit email | Canonical role | Public profile precheck | Legal identity | GitHub/email association | Change ownership |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Sebastián | `spinedo214` | `sebastianpinedo214@gmail.com` | Mobile helper; Principal Report helper | [Profile exists; public display Sebastián Pinedo](https://github.com/spinedo214) | OWNER CONFIRMED BY HANDOFF | OWNER-CONFIRMED PROJECT COMMIT EMAIL | No current reviewed-unit attribution; future research workstream pending |
| Diego | `DiegoS284` | `diego64g284@gmail.com` | Nexa Team Lead; App/Mobile Lead; C4/architecture/implementation evidence | [Profile exists; public display Diego Y. Sandoval](https://github.com/DiegoS284) | OWNER CONFIRMED BY HANDOFF | OWNER-CONFIRMED PROJECT COMMIT EMAIL | Current reviewed technical units authorized |
| Joaquín | `JoaquinBV511` | `joaquinverdebueno@gmail.com` | Report Lead; Mobile helper | [Profile exists; public display Joaquin Verde](https://github.com/JoaquinBV511) | OWNER CONFIRMED BY HANDOFF | OWNER-CONFIRMED PROJECT COMMIT EMAIL | Current reviewed academic units authorized |
| Gino | `R0obxdnt` | `grtdls525gino1@gmail.com` | Mobile helper; Principal Report helper | [Profile exists; no public display name](https://github.com/R0obxdnt) | OWNER CONFIRMED BY HANDOFF | OWNER-CONFIRMED PROJECT COMMIT EMAIL | No current reviewed-unit attribution; future Tactical DDD/UML/DB review pending |
| Gerard | `GerardRojasMancilla` | `U202413142@upc.edu.pe` | Principal Mobile helper; Basic Report helper | [Profile exists; public display Gerard Gianpier Rojas Mancilla](https://github.com/GerardRojasMancilla) | OWNER CONFIRMED BY HANDOFF | OWNER-CONFIRMED PROJECT COMMIT EMAIL | No current reviewed-unit attribution; future Mobile UX evidence review pending |

The canonical prompt does not authorize guessing surnames, student codes or
alternate emails. The academic cover may contain additional working labels,
but they do not replace the owner-confirmed identity registry.

## Current integration approval — 2026-09-02

DiegoS284 (`diego64g284@gmail.com`) and JoaquinBV511
(`joaquinverdebueno@gmail.com`) jointly reviewed the current report handoff and
authorize integration of the current 28-story V1 projection and current diff.

| Decision | State |
| :--- | :--- |
| Human review gate | `APPROVED` |
| Report integration | `28/28 APPROVED` |
| Current attribution | Joaquín for coherent academic/report units; Diego for coherent technical/C4/API/architecture units |
| Individual defense review | `FOLLOW-UP — NOT REQUIRED TO BLOCK INTEGRATION` |
| Historical alias | `ManoJVB10` resolved as Joaquín's previous username; history rewrite prohibited |

This approval does not fabricate individual Gino, Gerard or Sebastián reviews,
does not assign current authorship to absent teammates and does not promote any
report claim to Mobile implementation, Product Acceptance or production
readiness.

The public profile precheck was performed on 2026-09-01 and resolved all five
URLs. The 2026-09-02 handoff explicitly resolved the current identities and
project commit emails. A public display name remains only a precheck; it does
not replace the owner decision or establish ownership of a specific diff.

## Historical commit-author precheck

The following observations were collected read-only on 2026-09-01 with
`git log --all --format='%an <%ae> %h %s'`. They are provenance clues only; a
commit author string, a GitHub `noreply` address or a matching email does not
prove legal identity, account ownership, email association or authorship of a
new report change.

| Repository / observed revision | Author string and email | Relation to supplied identity | Human action still required |
| :--- | :--- | :--- | :--- |
| `report` / `3edeb196800a72a30299987a661e791c8f8fb50d` | `R0obxdnt <168935323+R0obxdnt@users.noreply.github.com>` | Historical author string matches the owner-confirmed Gino username | Gino reviews and explicitly accepts any new report unit assigned to him |
| `report` / `9b88bfb6c8bef82447ae9dbea9a410d908fb977b` | `Joaquín Francisco Verde Bueno <165977453+ManoJVB10@users.noreply.github.com>` | Historical alias; owner resolved `ManoJVB10` as Joaquín's previous username | Use `JoaquinBV511` for new commits; do not rewrite history |
| `api` / `9ff96f387a82ea0570f24b3c4063636d3e4109b8` | `DiegoS284 <diego64g284@gmail.com>` | Historical author matches the owner-confirmed Diego identity | Diego reviews and explicitly accepts any new report unit assigned to him |
| `mobile` / `17fba3184bc85d82a29437e04f20773e9cc775d1` | `DiegoS284 <diego64g284@gmail.com>` | Historical author matches the owner-confirmed Diego identity | Diego confirms whether this repository evidence may be cited by the report |
| `blueprint` / `217d2bf2429d602d5d08771ed88fa0d1de12ba36` | `DiegoS284 <diego64g284@gmail.com>` | Historical author matches the owner-confirmed Diego identity | Diego confirms source citation scope when reviewing the unit |

No Sebastián or Gerard author assignment is inferred from the absence of a
matching row in these observed histories. The handoff resolves their
identities, but not ownership of a specific change.

## Workstream ownership supplied by the canonical prompt

This matrix is a review aid, not a completed story assignment. A person may
support a story without owning its commit. Current integration ownership is
limited to the approved Joaquín/Diego units below; future workstream ownership
requires that person's own review.

| Workstream | Primary owner from prompt | Main scope | Support / coordination |
| :--- | :--- | :--- | :--- |
| Report integration | Joaquín | Coherence, front matter, Chapter II, academic backlog, Strategic DDD, milestones, conclusions and release review | Gino; all leads provide source evidence |
| Research / Needfinding | Sebastián | Research provenance, reusable/new interviews, Physical Operations & Delivery research, Needfinding, personas, sources, bibliography domain research and EventStorming discovery | Joaquín |
| Requirements / Tactical modeling | Gino | User Stories, Acceptance Criteria, Technical/Spike Stories, Product Backlog, Tactical DDD, class diagrams, persistence/database modeling and architecture consistency | Joaquín |
| Technical integration | Diego | Blueprint synchronization, C4/Structurizr, API/backend evidence, Mobile architecture, SCM, implementation/deployment facts and cross-repository consistency | Gino; Gerard |
| Mobile UX / implementation evidence | Gerard | Chapter III Mobile-facing content, interaction/error states, accessibility, Mobile runtime and Sprint execution screenshots/videos when real | Diego |

The table does not assign one lead to each of the 28 stories. That assignment
must be recorded in the story register after the team confirms who can explain
the complete story, its four scenarios, its evidence and its resulting diff.

## Verification protocol

For each person and each proposed commit, record:

1. Use legal name and current GitHub username from the owner-confirmed registry.
2. Use the supplied email as `OWNER-CONFIRMED PROJECT COMMIT EMAIL`; do not label
   it GitHub-verified without separate evidence.
3. Exact branch and files reviewed.
4. Source evidence and scope the person can explain.
5. Explicit acceptance of authorship for that logical unit.

If a real identity mismatch appears, pause and record
`IDENTITY NEEDS HUMAN CONFIRMATION`; do not guess an alternative email. Never
use another person's password, PAT, SSH private key or GPG key. Do not add
`Co-authored-by` trailers to simulate ownership.

## Current decision

All five identity rows are `OWNER CONFIRMED BY HANDOFF`. The 2026-09-02 joint
review authorizes current reviewed integration units under the exact matrix in
[human-commit-gate.md](./human-commit-gate.md). Use one-shot identity only for
Joaquín or Diego according to unit. Gino, Gerard and Sebastián remain eligible
for new meaningful workstreams after their own review; no current unreviewed
diff is attributed to them.
