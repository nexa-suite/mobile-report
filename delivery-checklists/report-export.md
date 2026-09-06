# Report export checkpoint

## Reproducible command

From the report repository:

```bash
bash scripts/export-report-pdf.sh /tmp/nexa-mobile-report-final.pdf
```

The script builds a deterministic source order from the report Markdown, places
the generated table of contents after the cover, normalizes report-relative
asset paths in the temporary build source and writes the PDF to the requested
path. The default output is temporary and is not a submission artifact.

Docker mode is the default. It uses
`pandoc/latex@sha256:6e71008186280e8908e3816481165c0103d04c64162bc9c3f3fe7bc27c681fc5`
with `linux/amd64`, because the pinned image does not publish an ARM64
manifest. Native execution is available with
`NEXA_REPORT_EXPORT_MODE=native` when both `pandoc` and `xelatex` are installed.

## Smoke-test result

On 2026-09-05 the Docker path generated a temporary 213-page PDF from 141
Markdown sources. `pdfinfo` reported a non-empty letter-size PDF. The container
emitted non-fatal `Ticker: poll failed: Interrupted system call` messages while
the command still exited successfully. The PDF smoke scan found no forbidden
internal provenance terms. Rendered pages covering team profiles and the
Sebastián Pinedo photo, story records, strategic DDD, bounded-context coverage,
class diagrams and database design were inspected. The temporary output is not
committed because the official submission filename and complete human PDF
acceptance remain pending.

## Closure conditions

- [x] Source Markdown remains unchanged by export-only normalization.
- [x] Profile image paths resolve in the temporary build.
- [x] Wide Markdown tables wrap within the page in the inspected samples.
- [x] Export-only Unicode substitutions remove missing-glyph warnings.
- [x] Critical PDF pages were rendered and visually inspected after the final
      export adjustment.
- [ ] Human reviews the complete PDF for page breaks, table readability,
  numbering, APA 7 layout and conversion defects.
- [ ] Owner names the accepted PDF with the official AV1/TB1/AV2/TB2 filename
  after the corresponding human gate is complete.
