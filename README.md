# Humanizador

Humanizador hace que el texto en español escrito por IA suene a quien lo escribe, sin cambiar lo que dice. Es la adaptación al español de [humanizer](https://github.com/blader/humanizer) de blader, con patrones propios del español como los calcos del inglés y la rotación de sinónimos. Funciona en Claude Code, Codex, OpenCode y cualquier agente que lea skills en formato [`SKILL.md`](SKILL.md).

**Antes:**

> ¡Me emociona anunciar que por fin llegaron los borradores compartidos! 🚀 Durante meses, nuestro propio equipo se ahogaba en archivos llamados final_v7.docx -- y sabíamos que tenía que haber una mejor manera. Ahora dos personas pueden editar el mismo documento a la vez, y cada cambio aparece en vivo para las dos. No es solo una función; es una forma completamente nueva de colaborar. Los comentarios se quedan anclados a la oración exacta a la que hacen referencia, incluso mientras el texto a su alrededor evoluciona. ¿Y lo mejor? Está disponible hoy en todos los planes, totalmente gratis. Piénsalo.

**Después:**

> Los borradores compartidos salen hoy. Durante meses nuestro propio equipo se pasaba archivos llamados final_v7.docx, y nos hartamos. Ahora dos personas pueden editar el mismo documento a la vez y ver los cambios de la otra mientras escribe. Los comentarios se quedan pegados a la oración de la que hablan, aunque cambie el texto alrededor. Es gratis en todos los planes.

Humanizador edita para lectores humanos. Pasar los detectores de IA no es un objetivo.

## Las cinco señales más fuertes

Son las señales más comunes de la escritura de IA, y la skill reescribe cualquiera de ellas en cuanto la ve:

1. No X, sino Y: "No es solo una función, es un cambio."
2. Remates de una línea: "Piénsalo."
3. Frases que suenan profundas: "En el fondo, lo que de verdad importa es..."
4. Preámbulo antes de la idea: "La cosa es esta." "¿Honestamente?"
5. Discutir con nadie: "No digo que X, pero..."

En total revisa [28 patrones](#los-28-patrones).

## Instalación

Una vez instalada, llámala con `/humanizador` o pídela en palabras normales.

### Claude Code

```text
/plugin marketplace add donutinit/humanizador
/plugin install humanizador@humanizador
```

El plugin necesita Claude Code 2.1.142 o más nuevo. En versiones anteriores usa `npx skills add donutinit/humanizador --global --agent claude-code`.

### Codex

```sh
npx skills add donutinit/humanizador --global --agent codex
```

### pi

```sh
pi install git:github.com/donutinit/humanizador
```

Agrega `-l` para instalarla solo en el proyecto actual. `pi update --extensions` trae las versiones nuevas.

### Claude.ai y Claude Desktop

Descarga este repositorio como ZIP (en GitHub, Code y luego Download ZIP) y súbelo como skill en la configuración de Claude.

### Otros agentes

```sh
npx skills add donutinit/humanizador --global --agent '*'
```

Esto la instala en cada agente que conoce el CLI de skills, como OpenCode, Gemini CLI o GitHub Copilot. Quita `--global` de cualquier comando para instalarla solo en el proyecto actual.

### A mano

Clona el repo y enlázalo en la carpeta de skills de tu agente:

```sh
git clone https://github.com/donutinit/humanizador ~/src/humanizador
ln -s ~/src/humanizador ~/.claude/skills/humanizador   # Claude Code (OpenCode también la lee aquí)
ln -s ~/src/humanizador ~/.codex/skills/humanizador    # Codex
```

Con el enlace, un `git pull` actualiza la skill en todos los agentes. Para un agente que el CLI de skills no conoce, copia o enlaza `SKILL.md` en su carpeta de skills.

## Uso

Llama la skill directo:

```text
/humanizador

[pega tu texto aquí]
```

O pídelo en palabras normales:

```text
Humaniza este texto: [tu texto]
```

Para reescribir un archivo, dale la ruta:

```text
Humaniza la prosa de docs/anuncio.md
```

Antes de editar, la skill lee el archivo actual completo, aunque lo haya escrito antes en la misma sesión. Su resumen dice cuántas secciones revisó y cuáles no pudo cubrir.

### Iguala tu voz

Si le das una muestra de tu escritura, la skill imita el largo de tus oraciones, tu vocabulario, tu puntuación y tus transiciones. La muestra manda sobre los patrones: si usas rayas, las conserva.

```text
/humanizador

Así escribo yo:
[pega dos o tres párrafos tuyos]

Ahora humaniza este texto:
[pega el texto de IA]
```

## Cómo funciona

Un modelo de lenguaje elige por defecto lo que sirve para la mayor cantidad de lectores, y una persona elige para un lector concreto. Cada señal que busca la skill es una forma de esa elección por defecto: una oración que anuncia importancia en vez de aportar un dato, ritmo o formato aplicados por regla, un dato ordinario vestido de decisivo, restos del chat o una respuesta que vuelve a explicar lo que el lector ya sabe.

La skill marca cada señal, de la más fuerte a la más débil. Escribe un borrador en el que puede unir, dividir o reordenar oraciones y párrafos, lo revisa contra los patrones y contra los datos del original, y escribe la versión final. Con texto pegado muestra su trabajo: el borrador, las señales que quedan y la versión final. En un archivo cambia solo la prosa y deja igual el código, los comandos, las rutas y los metadatos. Cuando otra tarea la usa para un pull request, un commit o un documento, devuelve solo el texto final.

Tres reglas no se negocian: no inventar hechos, nombres, números ni citas (si falta un dato, se pregunta o se deja "Por confirmar"); no dejar rayas largas ni cortas, salvo que la muestra del autor las use; y usar comillas rectas.

## Los 28 patrones

Los patrones van del más fuerte y común al más débil. La skill edita cualquiera de los cinco primeros la primera vez que lo ve. Un patrón marcado *débil por sí solo* cuenta solo cuando hay otras señales en el mismo pasaje, porque alguien que escribe con cuidado puede usar cualquiera a propósito.

### A. Escenificar en vez de afirmar

| # | Patrón | Ejemplo |
|---|---|---|
| 1 | No X, sino Y | "No es simplemente una canción, es una declaración." |
| 2 | Remates de una línea y fragmentos dramáticos | "Esa es la verdadera ventaja.", "Esto demuestra la importancia de..." |
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
| 22 | Encabezados decorativos | "Estrategias De Negociación Y Alianzas", emojis en títulos, "La decisión, en una pantalla" |
| 23 | Comillas tipográficas | comillas curvas donde van rectas |

### E. Restos del chat y del borrador

| # | Patrón | Ejemplo |
|---|---|---|
| 24 | Restos de chatbot | "¡Excelente pregunta!", "Espero que te sirva" |
| 25 | Límites de conocimiento y suposiciones | "hasta mi última actualización", "probablemente creció..." |
| 26 | Título repetido en la primera oración | "## Rendimiento / La velocidad importa." |
| 27 | Hablar del documento en vez de su tema | "se agregó para sustituir...", "la tabla de abajo compara..." |

### F. Escribir para el lector equivocado

| # | Patrón | Ejemplo |
|---|---|---|
| 28 | Volver a explicar lo que el lector ya sabe | una respuesta que recorre el diagnóstico y prueba el plan antes de dar la decisión |

## Otro ejemplo

**Antes:**

> ¡Excelente pregunta! La nueva biblioteca municipal no es solo un edificio, es un testimonio vibrante del compromiso de la ciudad con la cultura. Enclavada en el corazón del centro histórico, cuenta con salas de lectura, talleres y un auditorio, fomentando la convivencia, la creatividad y el aprendizaje. Sin duda, marca un momento decisivo para la comunidad. ¡Espero que te sirva!

**Después:**

> La nueva biblioteca municipal está en el centro histórico. Tiene salas de lectura, talleres y un auditorio.

La versión final perdió el elogio, el contraste "no es solo..., es...", el vocabulario inflado, la tríada de gerundios y el "momento decisivo", pero conserva cada dato del original.

## Fuentes

- [humanizer](https://github.com/blader/humanizer) de blader (Siqi Chen), versión 4.0.0, licencia MIT. Esta skill sigue su estructura, sus patrones y su método, con una diferencia: no agrega datos aunque el texto sea genérico.
- ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) de Wikipedia, mantenida por WikiProject AI Cleanup.

## Historial de versiones

Ver [CHANGELOG.md](CHANGELOG.md).

## Licencia

MIT. Ver [LICENSE](LICENSE); conserva el aviso de copyright original de humanizer.
