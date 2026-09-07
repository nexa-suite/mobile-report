# TB2 Delivery Checklist

## Release-review gates

| Gate | Evidence required | Current state | Closure proof |
| :--- | :--- | :--- | :--- |
| Final report | Updated front matter, corrected chapters, final conclusions, bibliography and annexes | Provisional structure; final acceptance pending | Final PDF, visual review, presentation and team signoff |
| Chapter IV / Sprint 3 | Planning, backlog, LACX, development, testing, execution, services and deployment evidence | Sprint 3 register and API cross-reference prepared; execution pending | Board/task links, dates, commits, tests, captures and review |
| Product Backlog | All approved functionality demonstrated without expanding V1 scope | 28-story projection and report integration `28/28` approved; no Mobile client evidence | Story-by-story runtime/build evidence and Product Acceptance |
| Backend and documentation | Public 100% backend, OpenAPI/Swagger, examples and stable URL | Contract source and Docker-backed API baseline observed (`482` tests, `0` failures, `148` skipped); public deployment not verified | URL, source SHA, requests/responses, screenshots and reviewer |
| Mobile distribution | Firebase App Distribution or accepted equivalent | Not produced | Release identifier, checksum, install/access log, device and reviewer |
| Final validation video | End-to-end application validation with final paths | Not produced | Video URL/file, screenshot, timing, consent and review |
| About the Product | Final promotional/product video and permitted testimony | Not produced | URL/file, duration, source/build and permissions |
| About the Team | Final process and individual testimony video | Not produced | URL/file, timing, participant permissions and reviewer |
| Release decision | Risks, known limitations, rollback/distribution and acceptance | Not ready | Team/instructor review recorded |

## Current status

`OPEN — NO RELEASE, DISTRIBUTION, PHYSICAL-DEVICE, FINAL-VIDEO OR PRODUCT
ACCEPTANCE EVIDENCE IS PRESENT IN THIS CUT`.

No TB2 completion or production-readiness claim may be inferred from a green
API test, a prototype, an emulator, a source branch or a report checklist.

## Supporting validation evidence — 2026-09-02

The API `main` source at `380e2427bc3883f23fbd7e9a82d452888f2074a8` was
retested with Docker/Testcontainers using `./mvnw test`: `BUILD SUCCESS`, 482
tests, 0 failures and 148 skipped. The run supports the backend baseline only;
it does not close Sprint 3 execution, Mobile distribution, physical-device,
video, Product Acceptance or release-decision gates. Full command, environment
and interpretation are recorded in the
[implementation evidence register](./implementation-evidence-register.md).
