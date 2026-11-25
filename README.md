# Humanizador

Una skill para agentes que reescribe texto en español que suena a IA para que suene a quien lo escribe, sin cambiar lo que dice. Es la adaptación al español de [humanizer](https://github.com/blader/humanizer) de blader, con patrones propios del español como los calcos del inglés y la rotación de sinónimos.

La skill está en [`SKILL.md`](SKILL.md). Funciona con cualquier agente que lea skills en formato `SKILL.md`: Claude Code, Codex, OpenCode y otros.

## Instalación

**Con el CLI de skills** (detecta tu agente):

```sh
npx skills add donutinit/humanizador
```

**Como plugin de Claude Code:**

```text
/plugin marketplace add donutinit/humanizador
/plugin install humanizador@humanizador
```

**A mano:** clona el repo y enlázalo en la carpeta de skills de tu agente.

```sh
git clone https://github.com/donutinit/humanizador ~/dev/humanizador
ln -s ~/dev/humanizador ~/.claude/skills/humanizador   # Claude Code (OpenCode también la lee aquí)
ln -s ~/dev/humanizador ~/.codex/skills/humanizador    # Codex
```

Con el enlace, un `git pull` actualiza la skill en todos los agentes.

## Uso

Pídele al agente que humanice un texto o menciona la skill:

```text
Humaniza este texto: ...
Usa humanizador para revisar README.md
```

Hay tres modos:

- **Texto pegado:** devuelve un borrador, las señales que quedan y la versión final.
- **Archivo:** reescribe solo la prosa del archivo y deja igual el código, los comandos, las rutas y los metadatos.
- **Integrado:** cuando otra tarea la usa para un pull request, un commit o un documento, devuelve solo el texto final.

### Iguala tu voz

Si le das una muestra de tu escritura, la skill imita el largo de tus oraciones, tu vocabulario, tu puntuación y tus transiciones. La muestra manda sobre los patrones: si usas rayas, las conserva.

```text
Humaniza este texto. Así escribo yo: [pega uno o dos párrafos tuyos]
```

## Cómo funciona

Un modelo de lenguaje elige por defecto lo que sirve para la mayor cantidad de lectores, y una persona elige para un lector concreto. La skill agrupa los patrones en cinco familias de esa elección por defecto, del más fuerte al más débil. Los patrones marcados *débiles por sí solos* solo cuentan cuando aparecen junto con otros.

Tres reglas no se negocian: no inventar hechos, nombres, números ni citas (si falta un dato, se pregunta o se deja "Por confirmar"); no dejar rayas largas ni cortas, salvo que la muestra del autor las use; y usar comillas rectas.

## Los 27 patrones

### A. Escenificar en vez de afirmar

| # | Patrón | Ejemplo |
|---|---|---|
| 1 | No X, sino Y | "No es simplemente una canción, es una declaración." |
| 2 | Remates de una línea y fragmentos dramáticos | "Esa es la verdadera ventaja." |
| 3 | Frases que suenan profundas | "La simetría es el lenguaje de la confianza." |
| 4 | Preámbulo antes de la idea | "¿Honestamente? Depende." |
| 5 | Discutir con nadie | "Sería tentador..., pero..." |

### B. Ritmo por regla

| # | Patrón | Ejemplo |
|---|---|---|
| 6 | Tríadas forzadas | "innovación, inspiración y conocimiento" |
| 7 | Inicios repetidos | "Ella notó... Ella notó... Ella guardó..." |
| 8 | La raya como conector universal | "La política (raya) anunciada sin aviso (raya) afecta..." |
| 9 | Atenuadores apilados | "podría potencialmente argumentarse" |
| 10 | Calcos del inglés | "juega un rol", "hace sentido", "a nivel de" |
| 11 | Voz pasiva y fragmentos sin sujeto | "No se necesita archivo de configuración." |
| 12 | Rotación de sinónimos | "el protagonista... el personaje principal... la figura central" |
| 13 | Rangos falsos | "desde el Big Bang hasta la danza de la materia oscura" |

### C. Inflar y tomar autoridad prestada

| # | Patrón | Ejemplo |
|---|---|---|
| 14 | Vocabulario típico de IA | "un testimonio perdurable del vibrante panorama" |
| 15 | Importancia inflada | "marcando un momento decisivo" |
| 16 | Relación vaga | "está asociado a la orquesta" |
| 17 | Gerundios de adorno | "..., simbolizando..., reflejando..." |
| 18 | Lenguaje publicitario | "enclavado en la impresionante región" |
| 19 | Autoridad prestada | "los expertos creen que..." |
| 20 | Evitar "es", "son" y "tiene" | "sirve como", "cuenta con", "presume de" |

### D. Formato por regla

| # | Patrón | Ejemplo |
|---|---|---|
| 21 | Negritas de adorno | "- **Rendimiento:** El rendimiento..." |
| 22 | Encabezados decorativos | "Estrategias De Negociación Y Alianzas", emojis en títulos |
| 23 | Comillas tipográficas | comillas curvas donde van rectas |

### E. Restos del chat y del borrador

| # | Patrón | Ejemplo |
|---|---|---|
| 24 | Restos de chatbot | "¡Excelente pregunta!", "Espero que te sirva" |
| 25 | Límites de conocimiento y suposiciones | "hasta mi última actualización", "probablemente creció..." |
| 26 | Título repetido en la primera oración | "## Rendimiento / La velocidad importa." |
| 27 | Escribir sobre la versión anterior | "se agregó para sustituir el enfoque anterior..." |

## Ejemplo completo

**Antes:**

> ¡Excelente pregunta! La nueva biblioteca municipal no es solo un edificio, es un testimonio vibrante del compromiso de la ciudad con la cultura. Enclavada en el corazón del centro histórico, cuenta con salas de lectura, talleres y un auditorio, fomentando la convivencia, la creatividad y el aprendizaje. Sin duda, marca un momento decisivo para la comunidad. ¡Espero que te sirva!

**Después:**

> La nueva biblioteca municipal está en el centro histórico. Tiene salas de lectura, talleres y un auditorio.

La versión final perdió el elogio, el contraste "no es solo..., es...", el vocabulario inflado, la tríada de gerundios y el "momento decisivo", pero conserva cada dato del original.

## Fuentes

- [humanizer](https://github.com/blader/humanizer) de blader (Siqi Chen), versión 3.0.0, licencia MIT. Esta skill sigue su estructura, sus patrones y su método.
- ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) de Wikipedia, mantenida por WikiProject AI Cleanup.

## Historial de versiones

- **1.0.0** (2026-09-27): primera versión, basada en humanizer 3.0.0. Traduce y adapta los 25 patrones al español: cambia los pares con guion por calcos del inglés, los gerundios toman el lugar de los *-ing* y los encabezados vigilan la mayúscula en cada palabra. Agrega rotación de sinónimos y rangos falsos (del humanizador en español basado en humanizer 2.9.1), la regla de "Por confirmar" para datos faltantes, comillas rectas en la versión final y la lista de rasgos que no son señal por sí solos.

## Licencia

MIT. Ver [LICENSE](LICENSE); conserva el aviso de copyright original de humanizer.
