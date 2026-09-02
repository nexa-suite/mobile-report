# Matriz de gaps frente a la rúbrica móvil

## Propósito y corte

Esta matriz es un control interno de cierre. Concilia el prompt canónico y el
enunciado académico sin convertir una plantilla, una proyección o una prueba
de backend en evidencia de producto Mobile.

| Fuente | Corte |
| :--- | :--- |
| Prompt canónico | `/Users/joaquinfranciscoverdebueno/Downloads/NEXA MOBILE ACADEMIC REPORT .md` — SHA-256 `af86ca49fb0e7b2add5313116bc7fd4651add5e8562bf215a8f9a78296a20370` |
| Enunciado y rúbrica | `/Users/joaquinfranciscoverdebueno/Developer/nexa-suite/blueprint/90-academic/mobile/enunciado-trabajo-final.md` — SHA-256 `ac734ff3fe33f38185cd57b05d2ed48cd42a46239c87a78ff98418a4bb5b8e6f` |
| Informe | `reconcile/report-integration-20260902`, source checkpoint validado `8912aa03689c27c7c55c05bdd0b996008fd87514`; el ref vivo se resuelve desde Git |
| Regla del corte | Integración `28/28` aprobada por DiegoS284 + JoaquinBV511; staging, commits y push completados; PR y merge siguen sujetos a revisión humana |

`Structure ready` significa que existe una estructura contextualizada que puede
revisarse. `Partial` significa que sólo una parte de la evidencia fue
observada. `Pending human` significa que la fuente, decisión, identidad,
aceptación o artefacto debe ser aportado y revisado por una persona. Ninguna
fila puede pasar a `Complete` sólo por tener contenido Markdown.

## Matriz de cobertura

| Ref. en el enunciado | Obligación | Evidencia actual | Estado del corte | Criterio de cierre / responsable |
| :--- | :--- | :--- | :--- | :--- |
| § Informe del proyecto, p. 188–190 | README Markdown, repositorio en la organización pública, GitFlow, Conventional Commits y exportaciones PDF por hito | [README del informe](../README.md), [SCM](../report/04-product-implementation-and-validation/4.1-software-configuration-management/), [Human Commit Gate](./human-commit-gate.md) y [team identity register](./team-identity-register.md) | Partial | Verificar visibilidad/URL pública, ramas y commits reales; confirmar identidad/ownership y generar/revisar PDF AV1/TB1/AV2/TB2. Owner: report lead. |
| § Presentación, p. 192–193 | Presentación PowerPoint alineada a cada hito, fotos, nombres, carreras y exposición | No hay deck ni capturas verificadas en este corte | Pending human | Adjuntar presentación por hito, fotografías con consentimiento y revisión de coherencia con el informe. Owner: team lead. |
| § Reporte de participación, p. 195–196 | Evaluación individual 0–20 elaborada por el Team Leader en cada entrega | [Participant Performance Report](../report/93-annexes/annex-b-participant-performance-report/participant-performance-report.md) contiene estructura | Pending human | Completar acciones observables, calificación, fuente y aprobación del Team Leader; no inferir aportes desde nombres Git. |
| § Artefactos, p. 198–199 | Adjuntar artefactos y capturas de herramientas con explicación y exposición | [Índice de assets](../report/assets/asset-index.md) y anexos estructurados; capturas fuente pendientes | Partial | Adjuntar archivo fuente, exportación, captura, fecha, herramienta y explicación por artefacto. Owner: artifact owner. |
| § Videos, p. 201–204 | Videos editados, presentación/artefactos sincronizados, enlace privado y archivo de cada entrega | [Videos suplementarios](../report/04-product-implementation-and-validation/supplementary-sections/video-app-validation.md), [About Product](../report/04-product-implementation-and-validation/supplementary-sections/video-about-the-product.md), [About Team](../report/04-product-implementation-and-validation/supplementary-sections/video-about-the-team.md) | Pending human | Registrar archivo, URL con acceso comprobado, entrega, duración ≤15 min, timing y consentimiento; no inventar enlaces. Owner: video owner. |
| § Recomendaciones generales, p. 214–223 | APA 7, conversión PDF, carga en aula y terminología del Anexo F | [Bibliografía](../report/92-bibliography/bibliography.md), [Anexo F](../report/93-annexes/annex-f-translation-and-terms/translation-and-terms.md) y gates locales Markdown | Pending | Ejecutar revisión visual APA/PDF y comprobar carga en aula; revisar viudas, huérfanas, sangrías, numeración y citas. Owner: report lead. |
| § Carátula, p. 230–245 | Universidad, carrera, curso, NRC, docente, equipo, proyecto, integrantes, periodo, mes y año | [Cover](../report/00-front-matter/00-cover.md) | Partial | Completar datos oficiales, orden alfabético, códigos, periodo y revisión humana de cada identidad. Owner: team lead. |
| § Registro/colaboración/contenido/Student Outcome/SMART, p. 247–255 | Secciones obligatorias de front matter y colaboración por entrega | [Front matter](../report/00-front-matter/03-contents.md) | Partial | Registrar URL público, analíticos/commits reales, acciones individuales por entrega, párrafo exacto de Student Outcome y ≥2 SMART por integrante. Owner: report lead + cada estudiante. |
| § Capítulo I, p. 256–270 | Startup, solución, 5W2H, Lean UX, segmentos con datos y fuentes | [Chapter I](../report/01-presentation/chapter-overview.md) y sus secciones | Partial | Validar fuentes competitivas/segmentos, cerrar perfiles/fotos y revisar Problem Statement, cinco tipos de assumptions, hypotheses y canvas contextualizados. Owner: research/product leads. |
| § 2.1 Competidores, p. 271–278 y 446–474 | ≥3 competidores y landscape competitivo con análisis y estrategia | [Competitors](../report/02-requirements-and-software-solution-design/2.1-competitors/section-overview.md) | Partial | Aportar fuentes consultadas, logos/capturas permitidas, fecha, comparación completa y revisión de coherencia con el dominio. Owner: product lead. |
| § 2.2 Entrevistas, p. 279–285 y 474–487 | Diseño, registro y análisis; 3–5 entrevistas por segmento | [Entrevistas](../report/02-requirements-and-software-solution-design/2.2-interviews/section-overview.md) | Pending human | Verificar identidad/rol/consentimiento, video, metadata, captura, timing y análisis real. S1/S3 históricos requieren revalidación; S2 requiere investigación nueva de operaciones físicas y delivery. Owner: research lead. |
| § 2.3 Needfinding, p. 279–285 y 487–508 | Personas, task matrix, journeys, empathy maps, Big Picture EventStorming y Ubiquitous Language | [Needfinding](../report/02-requirements-and-software-solution-design/2.3-needfinding/section-overview.md) | Structure ready; evidence pending | Enlazar cada afirmación con entrevistas y fuente del artefacto UXPressia/board; adjuntar exportación y revisión del equipo. Owner: UX/research lead. |
| § 2.4 Requirements, p. 286–289 y 508–539 | User Stories, Impact Mapping y Product Backlog | [User Stories](../report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md), [Impact Map](../report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.2-impact-mapping.md), [Backlog](../report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.3-product-backlog.md) | Report integration `28/28` approved; individual defense follow-up | La defensa individual puede revisar owner/lead, source, dependencias, AC, prioridad, tareas, métricas y aceptación sin bloquear esta integración. Owner: assigned leads + product owner. |
| § Mobile V1 scope | Exactamente 28 historias V1 y separación del roadmap 73 | [Mobile story register](./mobile-v1-story-verification-register.md) y [API contract register](./mobile-v1-api-contract-register.md) | Partial | Confirmar cada ID, actor, BC, AC y decisión de producto; no expandir V1 ni declarar implementación por contrato API. Owner: product owner. |
| § 2.5 Strategic DDD, p. 290–299 y 539–575 | EventStorming, candidate contexts, flows, canvases, Context Map y C4 | [Strategic DDD](../report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/section-overview.md) y [architecture evidence register](./architecture-render-evidence-register.md) | Structure/source/export observed; workshop and report review pending | Adjuntar evidencia de workshop, canvases, fuente Structurizr/PlantUML/LucidChart y capturas revisadas; conservar un C4 Nexa y no inventar BC Mobile. Owner: architecture lead. |
| § Arquitectura, p. 300–305 y 575–590 | Context, container, component y deployment diagrams | [Software architecture](../report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/section-overview.md) y [architecture evidence register](./architecture-render-evidence-register.md) | Source validation/export observed; human visual review pending | Verificar fuente, render, fecha, leyenda AS-IS/TARGET, autoridad API, ownership lógico y estado cloud. Owner: architecture lead. |
| § 2.6 Tactical DDD, p. 300–312 y 590–610 | Capas, componentes, clases y database design por contexto | [Tactical coverage](../report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/2.6.1-bounded-context-coverage.md), [architecture evidence register](./architecture-render-evidence-register.md) y [API persistence register](./api-persistence-evidence-register.md) | Coverage and Blueprint artifacts observed; selected report artifacts pending | Elegir contexto, aportar clases/métodos reales o target explícito, componentes, tablas PK/FK/constraints/ownership y renders. Owner: architecture/data lead. |
| § Capítulo III, p. 313–334 y 609–638 | Style Guidelines, IA, landing wireframe/mock-up y Mobile wireframes/wireflows/mock-ups/user flows/prototype | [Chapter III](../report/03-solution-ui-ux-design/chapter-overview.md) y [Design Lab-to-Mobile crosswalk](../report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/section-overview.md) | Design Lab source observed; target reconciled; rendered Mobile evidence pending | Adjuntar archivos Figma/LucidChart/Overflow, exportaciones, viewport, estados felices/no felices, video de prototipo y revisión UX. Owner: UX lead. |
| § Capítulo IV SCM, p. 335–341 y 639–652 | Entorno, SCM, convenciones y deployment configuration | [SCM chapter](../report/04-product-implementation-and-validation/4.1-software-configuration-management/section-overview.md) y [baseline](./live-baseline.md) | Partial | Verificar URLs, ramas, ownership, herramientas, configuración, migraciones, rollback, URLs desplegadas y evidencias sin secretos. Owner: technical lead. |
| § Sprint structure, L. 342–352 y 653–729 | Sprint 1, 2 y 3; planning, LACX, backlog, development, testing, execution, services, deployment y collaboration | [Sprint index](../report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/section-overview.md) | Structure ready; execution pending | Mantener tres Sprints canónicos: S1 `001–017,019`; S2 `020–034`; S3 `044,047–049`. Registrar board, fechas, velocity, tareas, commits trazables, pruebas y capturas reales. Owner: sprint lead por hito. |
| § OpenAPI/Swagger, L. 725 | Endpoint, verbos, parámetros, ejemplos, response, capturas, repositorio y commits por Sprint | [Mobile V1 API contract register](./mobile-v1-api-contract-register.md) y evidencias de servicios por Sprint | Partial backend only | Adjuntar ejemplos request/response y URL desplegada/local por Sprint; confirmar mapping de `MOB-US-024` y `MOB-US-049` sin inferencia. Owner: API/service lead. |
| § 4.3 Validation Interviews, p. 353–362 y 729–746 | Diseño, 3–5 registros por segmento y evaluación heurística | [Validation](../report/04-product-implementation-and-validation/4.3-validation-interviews/section-overview.md) | Pending human | Ejecutar sesiones sobre landing y Mobile, guardar video/captura/metadata, separar observación de interpretación y completar Anexo E con re-check. Owner: research/UX lead. |
| § Conclusiones y recomendaciones, p. 364–365 y 735–746 | Contrastar problem statements, assumptions, hypotheses y criterios de éxito con validación; roadmap | [Conclusions](../report/90-conclusions/conclusions-and-recommendations.md) | Provisional only | Cerrar únicamente después de validación, aceptación y decisiones del roadmap; conservar conclusiones provisionales marcadas. Owner: report lead. |
| § Videos de cierre, p. 738–746 | About-the-Product, App Validation y About-the-Team | [Video register](../report/04-product-implementation-and-validation/supplementary-sections/video-about-the-product.md), [App Validation](../report/04-product-implementation-and-validation/supplementary-sections/video-app-validation.md), [Team](../report/04-product-implementation-and-validation/supplementary-sections/video-about-the-team.md) | Pending human | URL, archivo, timing, screenshot, testimonios consentidos, distribución Firebase App Distribution y revisión final. Owner: video/team lead. |
| § Glosario/Bibliografía/Anexos, p. 366–370 y 748–757 | Definiciones, APA, categorías y anexos con nueva página | [Glossary](../report/91-glossary/glossary.md), [Bibliography](../report/92-bibliography/bibliography.md), [Annexes](../report/93-annexes/annexes-overview.md) | Public cross-check observed; official verification pending | Confirmar 4 papers ≤2 años y Q1/Q2: 2 dominio + 2 técnicas móviles; adjuntar captura oficial, citas APA en texto, anexos y revisión visual PDF. Owner: report lead/research lead. |
| § Ética y responsabilidad, p. 760–762 | Términos/condiciones en landing y Mobile, ética ACM/IEEE/CIP, transparencia y GitHub | [Ethics-related annexes](../report/93-annexes/annexes-overview.md) y fuentes de superficie | Pending human | Redactar y publicar T&C, comprobar footer/registro, adjuntar capturas/video y evidencia de colaboración real. Owner: product/legal owner. |
| § Internacionalización y accesibilidad, p. 763–766 | `en_US` y `es_419`, inglés por defecto, ARIA en web, i18n/a11y en todos los productos | [Style guidelines](../report/03-solution-ui-ux-design/3.1-product-design/3.1.1-style-guidelines/3.1.1.1-general-style-guidelines.md) e [IA](../report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/section-overview.md) | Partial | Verificar catálogos y runtime por producto, ARIA/capturas, lector/contraste/teclado y Mobile físico; no usar Design Lab como prueba de Mobile. Owner: UX/mobile lead. |
| § Tecnología, p. 768–782 | UXPressia, Figma, LucidChart/Overflow/Vertabelo, Structurizr/PlantUML, stacks y herramientas | Fuentes de diseño/API y [asset index](../report/assets/asset-index.md) | Partial | Registrar herramienta real, archivo/exportación, versión, URL y reviewer por artefacto; decidir Kotlin/Android o Flutter/KMP mediante SPIKE-002. Owner: technical/UX leads. |
| § AV1, p. 788–802 | Primer hito: front matter, Capítulos I–II, conclusiones, bibliografía y anexos | Estructura documental existente; no hay exportación ni revisión de entrega | Partial | Cerrar contenido y fuentes; exportar PDF AV1; revisar portada, APA, videos/presentación y aceptación del hito. Owner: report lead/team lead. |
| § TB1, p. 803–819 | Landing desplegado, backend 70%, pantallas core y Sprint 1 | Stack local Web/API observado; Mobile no implementado; Sprint 1 sin ejecución acreditada | Open | Evidencia pública/deployment, pantallas Mobile, Sprint 1 real, commits y presentación/video. Owner: technical + sprint 1 leads. |
| § AV2, p. 820–837 | Backend 100% público con docs, core Mobile, videos iniciales y Sprint 2 | OpenAPI/runtime y backend local parcial; no deployment público Mobile ni videos | Open | Despliegue público, documentación con ejemplos, core Mobile, validación y Sprint 2. Owner: API/mobile/video leads. |
| § TB2, p. 838–854 | Todas las funcionalidades, Firebase App Distribution, videos finales, Sprint 3 y cierre | No hay cliente Mobile, distribución, dispositivo ni aceptación | Open | Build/checksum/install, Firebase, validación final, Sprint 3, report/PDF/presentation/video y defensa. Owner: mobile/team leads. |

## Gates que permanecen abiertos

- Integración del reporte Mobile V1: `28/28` aprobada por `DiegoS284 + JoaquinBV511` el 2026-09-02. Defensa individual: follow-up.
- Entrevistas verificadas: `0` en S1, S2 y S3; la investigación S2 de operaciones
  físicas y delivery sigue abierta.
- Product Acceptance, System Acceptance y Production Readiness: no afirmados.
- Identidades y correos de proyecto: `OWNER CONFIRMED BY HANDOFF`; atribución
  actual autorizada sólo para unidades Joaquín/Diego bajo la matriz de diff.
  No se infiere autoría de Gino, Gerard o Sebastián desde commits, nombres o
  organizaciones.
- Backend: baseline Docker-backed `./mvnw test` pasó `482` pruebas con `0`
  fallos y `148` omitidas; el rerun del 2026-09-02, sin Docker disponible,
  pasó `482` con `0` fallos y `152` omitidas. La integración ampliada quedó
  `PARTIAL` con `3` fallas explícitas de `TenantAdministrationIT`.
- Mobile: el repositorio observado es documental y no contiene cliente nativo,
  build, runtime, distribución ni prueba en dispositivo.
- Gate de commit: [Human Commit Gate](./human-commit-gate.md) está autorizado
  para staging y commits de las unidades actuales revisadas; defensa individual
  y evidencia de producto siguen separadas.

## Orden de cierre recomendado

1. Autenticar GitHub y abrir el PR de la rama hacia `develop`; no hacer merge
   automático.
2. Completar defensa individual, revisión visual y aceptación humana de la
   integración bajo [Human Commit Gate](./human-commit-gate.md).
3. Recolección y verificación de entrevistas, artefactos UX, DDD y bibliografía.
4. Implementación/validación Mobile, contratos consumidos, dispositivo y
   distribución.
5. Completar evidencia de Sprints 1–3, exportar/revisar PDF y cerrar la
   aceptación final antes de declarar release.
