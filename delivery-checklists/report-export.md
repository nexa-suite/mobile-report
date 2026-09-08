# Report export checkpoint

## Reproducible command

From the report repository:

```bash
bash scripts/export-report-pdf.sh /tmp/nexa-mobile-report-final.pdf
```

The script builds a deterministic source order from global Contents for
professor-facing navigation, appends non-Chapter-II Markdown in stable path
order, places the generated table of contents after the cover, normalizes
report-relative asset paths in the temporary build source, preserves the A4
page geometry of the official cover reference and writes the PDF to the
requested path. The default output is temporary and is not a submission
artifact.

Docker mode is the default. It uses
`pandoc/latex@sha256:6e71008186280e8908e3816481165c0103d04c64162bc9c3f3fe7bc27c681fc5`
with `linux/amd64`, because the pinned image does not publish an ARM64
manifest. Native execution is available with
`NEXA_REPORT_EXPORT_MODE=native` when both `pandoc` and `xelatex` are installed.

## Smoke-test result

The prior 2026-09-05 Docker checkpoint generated a temporary 213-page PDF from
141 Markdown sources, but its letter page geometry did not match the A4 cover
reference and is superseded for delivery. On 2026-09-06, native `pandoc` plus
`xelatex` produced the reconciled A4 export: 254 non-empty pages from 157
Markdown sources. The temporary output is not committed because the official
submission filename and complete human PDF acceptance remain pending.

## Closure conditions

- [x] Source Markdown remains unchanged by export-only normalization.
- [x] Profile image paths resolve in the temporary build.
- [x] Wide Markdown tables wrap within the page in the inspected samples.
- [x] Export-only Unicode substitutions remove missing-glyph warnings.
- [x] All 254 PDF pages were rendered as low-resolution contact sheets and
      visually inspected for blank pages, overflow, rotation and gross layout
      defects after the final export adjustment.
- [ ] Human reviews the complete PDF for page breaks, table readability,
  numbering, APA 7 layout and conversion defects.
- [ ] Owner names the accepted PDF with the official AV1/TB1/AV2/TB2 filename
  after the corresponding human gate is complete.
