# Anexo L: Accessibility & internationalization

Este registro separa la intención de diseño de la implementación y de la
verificación. No afirma pruebas que no estén registradas.

| Area | Design intent | Implemented | Verified | Evidence state |
| --- | --- | --- | --- | --- |
| `en_US` | English is the default language for UI, documentation and services. | No current Mobile implementation evidence is registered. | No locale test is registered. | DESIGN INTENT ONLY |
| `es_419` | Support Latin-American Spanish as a project locale. | No locale resource evidence is registered. | No locale-switching test is registered. | DESIGN INTENT ONLY |
| Mobile accessibility | Provide accessible Mobile interaction, including applicable contrast, focus and touch-target considerations. | No Mobile UI artifact or build is registered. | No manual or device accessibility test is registered. | DESIGN INTENT ONLY |
| Web ARIA | Use appropriate ARIA semantics in web experiences. | No implementation evidence is registered in this branch. | No ARIA test or audit is registered. | DESIGN INTENT ONLY |
| Contrast | Maintain sufficient contrast through design and implementation review. | No verified contrast-review artifact is registered. | No contrast test is registered. | DESIGN INTENT ONLY |
| Focus | Provide visible and followable focus where the platform applies. | No verified UI artifact is registered. | No keyboard or focus test is registered. | DESIGN INTENT ONLY |
| Touch targets | Provide adequate size and spacing for Mobile touch targets. | No Mobile UI artifact is registered. | No physical-device touch-target test is registered. | DESIGN INTENT ONLY |
| Language/fallback behavior | Define English default behavior and an explicit fallback path for supported locales. | No fallback implementation evidence is registered. | No language or fallback test is registered. | DESIGN INTENT ONLY |
