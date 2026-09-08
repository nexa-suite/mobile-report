# Project Report Collaboration Insights

Esta sección documenta la colaboración realizada para la elaboración y evolución
del **Project Report de Nexa**, mantenido en el repositorio público
[`nexa-suite/mobile-report`](https://github.com/nexa-suite/mobile-report). La
evidencia presentada corresponde exclusivamente al trabajo documental del
informe académico y se mantiene separada de la evidencia de implementación de
los productos de software, la cual se desarrolla posteriormente en el Capítulo
IV.

El informe se mantiene mediante un enfoque **Docs-as-Code**, con contenido
modular en Markdown y control de versiones mediante GitHub. El equipo utiliza
GitFlow para organizar la evolución del repositorio y Conventional Commits para
describir los cambios realizados. Esta sección se amplía progresivamente en cada
hito académico —AV1, TB1, AV2 y TB2— conservando la evidencia de las entregas
anteriores y añadiendo únicamente la colaboración correspondiente al nuevo
periodo.

## Repositorio del Project Report y estrategia de colaboración

**Tabla**

*Repositorio y convenciones de colaboración del Project Report*

| Elemento | Aplicación en el Project Report |
| --- | --- |
| **Repositorio público** | [`nexa-suite/mobile-report`](https://github.com/nexa-suite/mobile-report) |
| **Formato principal** | Markdown modular organizado por front matter, capítulos, conclusiones, glosario, bibliografía y anexos |
| **Control de versiones** | Git mediante GitHub |
| **Flujo de colaboración** | GitFlow con `main`, `develop` y ramas de alcance acotado |
| **Convención de commits** | Conventional Commits 1.0.0 |
| **Integración documental** | Los cambios se desarrollan de forma incremental y se integran después de revisar su coherencia con las secciones relacionadas |
| **Trazabilidad de autoría** | Git conserva el autor, fecha, mensaje y contenido de cada contribución |
| **Evolución académica** | La evidencia de colaboración se organiza por entrega: AV1, TB1, AV2 y TB2 |

> *Nota.* `main` representa el punto publicado o integrado del informe,
> `develop` concentra la integración del trabajo en curso y las ramas de alcance
> acotado permiten desarrollar cambios específicos antes de incorporarlos a la
> línea compartida. La evidencia de esta sección describe la colaboración sobre
> el **Project Report** y no reemplaza la evidencia de desarrollo por Sprint del
> Capítulo IV. Elaboración propia.

La estrategia busca evitar que el informe se construya como una única carga al
final de cada entrega. Las secciones pueden evolucionar de manera independiente,
pero los cambios que afectan conceptos compartidos —por ejemplo, Product
Definition, segmentos, requisitos o DDD— requieren revisión de consistencia
antes de su integración. De esta forma, Git no funciona únicamente como
almacenamiento, sino como registro reproducible de cómo el equipo construye,
corrige e integra el informe.

---

## AV1 — Sprint Review

Durante AV1 se trabajó en la construcción y reconciliación de la base académica
del Project Report. El trabajo incluyó front matter, Capítulo I, Capítulo II,
evidencia de investigación, requisitos, Strategic y Tactical-Level DDD,
trazabilidad documental y preparación del informe para su revisión y exportación.

La colaboración se desarrolló mediante contribuciones incrementales. Diferentes
integrantes participaron en contenidos de investigación, requisitos,
arquitectura, evidencia técnica y consolidación documental. Posteriormente se
realizaron ajustes de consistencia para alinear capítulos que comparten conceptos
de producto y dominio.

### Organización del trabajo documental

**Tabla**

*Forma de colaboración aplicada durante AV1*

| Actividad | Forma de trabajo |
| --- | --- |
| **Elaboración de contenido** | Las secciones se desarrollaron de forma modular para permitir contribuciones independientes sin editar todo el informe como un único archivo. |
| **Investigación y fuentes** | Se incorporaron antecedentes, evidencia histórica y referencias externas únicamente cuando su uso podía justificarse dentro del alcance académico actual. |
| **Revisión de coherencia** | Los cambios de Product, requisitos, arquitectura y DDD se revisaron contra las demás secciones relacionadas para reducir contradicciones. |
| **Control de cambios** | Las modificaciones se registraron mediante commits descriptivos siguiendo Conventional Commits. |
| **Integración** | Los cambios de alcance acotado se incorporaron progresivamente a las ramas compartidas en lugar de concentrarse en un único commit de cierre. |
| **Corrección documental** | Se realizaron iteraciones posteriores sobre redacción, estructura, evidencia, formato Markdown y compatibilidad de exportación. |
| **Responsabilidad individual** | Cada contribución queda asociada al autor correspondiente en el historial Git y puede contrastarse con el contenido modificado. |

> *Nota.* La organización descrita corresponde al flujo documental del
> Project Report. La planificación de Sprint, Sprint Backlog, Engineering Tasks
> y Development Evidence pertenecen al Capítulo IV y se documentan de forma
> independiente. Elaboración propia.

### Participación del equipo durante AV1

La participación se describe a partir de evidencia observable en el repositorio.
La tabla utiliza contribuciones representativas para mostrar el tipo de trabajo
realizado por cada integrante sin reproducir el historial completo de Git.

**Tabla**

*Participación verificada del equipo en el Project Report durante AV1*

| Integrante | Contribución documental observada | Evidencia representativa en GitHub |
| --- | --- | --- |
| **Pinedo, Sebastián** | Participó en la construcción de su perfil de integrante, reconciliación de evidencia histórica de investigación y refinamiento de contenido del Capítulo II, incluyendo estructura de requisitos y análisis competitivo. | [`2a8db97`](https://github.com/nexa-suite/mobile-report/commit/2a8db97ef94e30fc217445ee67fc3509fd6831cb) `docs(cap1): add Sebastian Pinedo team member profile`; [`e20f6e6`](https://github.com/nexa-suite/mobile-report/commit/e20f6e6a9705820a53cecb307a87c6b6055a7c6e) `docs(report): reconcile legacy research evidence`; [`8ca8e37`](https://github.com/nexa-suite/mobile-report/commit/8ca8e3725d70958738e4470281393aab65204536) `docs(ch2): refine requirements structure and academic language` |
| **Rojas Mancilla, Gerard** | Participó en la incorporación y revisión de evidencia técnica asociada al runtime Mobile, aportando trazabilidad documental sobre el estado técnico relevante para el informe. | [`55c10fd`](https://github.com/nexa-suite/mobile-report/commit/55c10fdd5fec43f8d24bc82e928d91c010753c7f) `docs(architecture): register mobile runtime evidence` |
| **Torrejón De Los Santos, Gino** | Participó en la reconciliación académica del backlog Mobile V1, contribuyendo a mantener alineada la especificación de requisitos del informe con el alcance vigente del proyecto. | [`8660f4f`](https://github.com/nexa-suite/mobile-report/commit/8660f4f834db85c2725fd1a815aefe04901de04a) `docs(requirements): reconcile mobile v1 academic backlog` |
| **Verde Bueno, Joaquín** | Participó de forma sostenida en la estructura del informe, front matter, portabilidad Markdown, validaciones documentales, reconciliación de Strategic y Tactical DDD, preparación de evidencia y correcciones para exportación. | [`604d48a`](https://github.com/nexa-suite/mobile-report/commit/604d48a88e1fd45958b8bf2f28d7c2addc2a1a1c) `fix(report): replace LaTeX-like cover markup with portable markdown/html`; [`1000739`](https://github.com/nexa-suite/mobile-report/commit/10007393a26746aa550afc1ba06b6d6dea81c0be) `fix(report): export av1 in a4 format`; [`ddce0e4`](https://github.com/nexa-suite/mobile-report/commit/ddce0e4596fe4c7a3e53d03c6b209c0f19873692) `docs(ddd): reconcile strategic and tactical evidence` |
| **Yucra Sandoval, Diego** | Participó en la validación y documentación de evidencia técnica, revisión de límites de arquitectura, refinamiento del Startup Profile y rework de secciones centrales del Capítulo I, incluyendo Antecedentes y Problemática y Segmentos objetivo. | [`8436336`](https://github.com/nexa-suite/mobile-report/commit/8436336f749b1f366aa02d950a5e245025753784) `chore(architecture): add technical evidence validation gates`; [`1e7a315`](https://github.com/nexa-suite/mobile-report/commit/1e7a315fc1b198e2b9af1a4b67619478154edb85) `fix(report): refine startup profile content and remove redundancies`; [`220dc57`](https://github.com/nexa-suite/mobile-report/commit/220dc57223879bb3ce7359fde1a99e993dca04fe) `docs(ch01): refine target segments and research context` |

> *Nota.* Los commits mostrados son evidencia representativa y no pretenden
> reemplazar el historial completo del repositorio. La participación se atribuye
> únicamente cuando existe una contribución identificable en GitHub. Elaboración
> propia.

### Evidencia de evolución documental

El historial observable del repositorio muestra que AV1 no se construyó mediante
una sola carga final. Se registraron iteraciones sobre contenido, requisitos,
evidencia, arquitectura, DDD, front matter y formato del informe. También se
observan contribuciones de los cinco integrantes del equipo, cada una asociada a
un autor identificable en Git.

Entre los cambios representativos del periodo se encuentran la preparación de
validaciones documentales y técnicas, la reconciliación del backlog Mobile V1,
la incorporación de evidencia de runtime Mobile, la revisión de investigación
histórica, la corrección del formato de portada y exportación, y el refinamiento
posterior de capítulos de presentación y requisitos.

**Tabla**

*Muestra de evolución documental observada durante AV1*

| Commit | Autor observable | Cambio documentado |
| --- | --- | --- |
| [`8436336`](https://github.com/nexa-suite/mobile-report/commit/8436336f749b1f366aa02d950a5e245025753784) | Diego Y. Sandoval | Incorporación de gates para validar evidencia técnica de arquitectura |
| [`8660f4f`](https://github.com/nexa-suite/mobile-report/commit/8660f4f834db85c2725fd1a815aefe04901de04a) | Gino Torrejón | Reconciliación del backlog académico Mobile V1 |
| [`e20f6e6`](https://github.com/nexa-suite/mobile-report/commit/e20f6e6a9705820a53cecb307a87c6b6055a7c6e) | Sebastián Pinedo | Reconciliación de evidencia histórica de investigación |
| [`55c10fd`](https://github.com/nexa-suite/mobile-report/commit/55c10fdd5fec43f8d24bc82e928d91c010753c7f) | Gerard Rojas Mancilla | Registro de evidencia de runtime Mobile |
| [`604d48a`](https://github.com/nexa-suite/mobile-report/commit/604d48a88e1fd45958b8bf2f28d7c2addc2a1a1c) | Joaquín Verde Bueno | Corrección de portada para Markdown portable |
| [`c5cd2d7`](https://github.com/nexa-suite/mobile-report/commit/c5cd2d772986fa2db66b624f711ccb477dfe172a) | Joaquín Verde | Actualización de Antecedentes y Problemática |
| [`1e7a315`](https://github.com/nexa-suite/mobile-report/commit/1e7a315fc1b198e2b9af1a4b67619478154edb85) | Diego Y. Sandoval | Refinamiento del Startup Profile y eliminación de redundancias |
| [`8ca8e37`](https://github.com/nexa-suite/mobile-report/commit/8ca8e3725d70958738e4470281393aab65204536) | Sebastián Pinedo | Refinamiento de estructura de requisitos y lenguaje académico |
| [`220dc57`](https://github.com/nexa-suite/mobile-report/commit/220dc57223879bb3ce7359fde1a99e993dca04fe) | Diego Y. Sandoval | Refinamiento de segmentos objetivo y contexto de investigación |

> *Nota.* La muestra se utiliza para evidenciar variedad de autores y evolución
> progresiva. La cantidad de commits no se interpreta por sí sola como medida de
> calidad o de esfuerzo individual; el contenido y alcance de cada contribución
> también deben considerarse. Elaboración propia.

### Lectura de la colaboración observada

La evidencia de AV1 muestra una colaboración con dos patrones complementarios.
Por un lado, existen contribuciones especializadas: requisitos, investigación,
arquitectura, runtime y refinamiento de capítulos concretos. Por otro, existen
tareas de integración y revisión transversal destinadas a mantener coherencia
entre secciones que comparten conceptos.

La participación no se interpreta únicamente por el volumen de commits. Un
cambio pequeño puede cerrar una inconsistencia crítica, mientras que una
reconciliación documental puede afectar varias secciones a la vez. Por ello, la
lectura de colaboración combina **autoría Git, alcance del cambio y artefacto
modificado**, en lugar de utilizar únicamente un conteo bruto de commits.

La evolución también evidencia iteración: varios artefactos fueron revisados
después de su primera incorporación. Esto resulta especialmente visible en
Antecedentes y Problemática, Startup Profile, requisitos, evidencia técnica y
DDD. Estas correcciones posteriores muestran que el informe se trató como un
artefacto vivo sujeto a revisión y no como documentación cerrada después de su
primera redacción.

### Coherencia con el Registro de Versiones del Informe

El **Registro de Versiones del Informe** resume modificaciones documentales
significativas, mientras que Git conserva el detalle fino de cada contribución.
Por ello, ambas evidencias tienen niveles de granularidad diferentes y no deben
duplicarse.

**Tabla**

*Relación entre Collaboration Insights y Registro de Versiones*

| Evidencia | Qué demuestra |
| --- | --- |
| **Registro de Versiones** | Hitos significativos en la evolución del informe, su fecha y autoría declarada |
| **Commits Git** | Cambios incrementales, autor observable, mensaje, fecha y contenido modificado |
| **Historial de ramas** | Forma en que las contribuciones se desarrollan e integran dentro del flujo colaborativo |
| **Analíticos de GitHub** | Distribución acumulada de actividad entre colaboradores en el repositorio |

La autoría de una versión significativa no sustituye la autoría individual de
los commits que la componen. De forma equivalente, un integrante que realiza la
integración de una versión no debe recibir automáticamente atribución por el
contenido elaborado previamente por otros miembros.

> *Nota.* Antes de cada entrega, el Registro de Versiones y esta sección deben
> revisarse de manera conjunta para asegurar que los cambios relevantes y la
> participación documentada sean coherentes con la evidencia observable en Git.
> Elaboración propia.

### Cobertura de evidencia AV1

**Tabla**

*Cobertura actual de evidencia de colaboración para AV1*

| Evidencia académica | Estado documentado |
| --- | --- |
| URL público del repositorio del Project Report | Verificado |
| Uso de Git y flujo de colaboración | Documentado |
| Participación observable de los cinco integrantes | Verificada mediante commits identificables |
| Evidencia textual de evolución del informe | Documentada |
| Coherencia conceptual con Registro de Versiones | Documentada como regla de cierre |
| Captura nativa de analíticos de colaboración de GitHub | No incorporada en el corte documental actual |
| Captura nativa del historial de commits de GitHub | No incorporada en el corte documental actual |

La evidencia visual exigida por la entrega debe obtenerse directamente de
GitHub en el corte definitivo de AV1. No se sustituye una captura nativa de los
analíticos o del historial de commits por una gráfica reconstruida manualmente,
ya que la finalidad de la evidencia es permitir que el evaluador observe la
actividad registrada por la propia plataforma.

Una vez incorporadas las capturas definitivas del hito, esta sección deberá
mantenerlas junto con la lectura analítica correspondiente. En TB1, AV2 y TB2 no
se reemplazará la evidencia de AV1: se añadirá un nuevo bloque por entrega para
mostrar la evolución acumulativa de la colaboración documental.
