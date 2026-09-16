# Contributing

## Contribution model

mobile-report uses Docs-as-Code. Propose focused changes against develop through
a descriptive feature branch, normally feature/<area>. Keep each change
attributable to its author and use the configured signed-commit workflow with
Conventional Commits.

## Evidence and report quality

- State only what the cited source supports; do not fabricate claims, evidence,
  quotes, screenshots or validation results.
- Keep relative links valid and use descriptive italicized titles for tables and
  visuals.
- Preserve report invariants, accepted terminology and the distinction between
  research, planning, design, implementation and validation.
- Keep generated PDFs out of the repository unless they are specifically
  requested for a delivery.
- Never commit secrets, private interview data, local paths or temporary
  evidence directories.

## Before requesting review

~~~bash
git diff --check
bash -n scripts/export-report-pdf.sh
~~~

Run the narrowest repository-provided checks relevant to the change and report
their results accurately.
