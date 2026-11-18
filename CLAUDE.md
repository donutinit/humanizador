# Guía para agentes

Cómo cambiar el Humanizador sin romper el paquete ni la skill. `CLAUDE.md` es un hard link de este archivo: son el mismo, para Claude, Codex y OpenCode. Git no guarda hard links, así que en un clon nuevo recréalo con `ln -f AGENTS.md CLAUDE.md`.

## Qué hay en el repo

Una skill en Markdown, sin paso de build. `SKILL.md` es lo que leen los agentes. Es una adaptación al español de [blader/humanizer](https://github.com/blader/humanizer).

Mantén la skill portable: nada de instrucciones que la limiten a una o dos herramientas.

## Archivos

- `SKILL.md` es la fuente de verdad y el único archivo de skill. Tiene metadatos YAML portables, la explicación de por qué el texto de IA suena como suena y los patrones numerados en seis grupos, del más fuerte al más débil.
- `README.md` explica instalación, uso y patrones.
- `CHANGELOG.md` guarda las notas de versión, de la más nueva a la más vieja. Las notas viejas conservan los números de patrón que usaba su versión.
- `.claude-plugin/plugin.json` describe el plugin de Claude y apunta a la `SKILL.md` de la raíz.
- `.claude-plugin/marketplace.json` permite agregar este repo como marketplace de Claude.
- `.cursor-plugin/plugin.json` describe el plugin de Cursor. No lleva campo `skills`, así Cursor carga la `SKILL.md` de la raíz.
- `package.json` vuelve el repo un paquete de pi. Su entrada `pi.skills` apunta a la raíz. No le agregues `version`: pi instala desde git.
- `agents/openai.yaml` tiene el nombre, la descripción corta y el prompt por defecto para agentes compatibles con OpenAI (Codex).
- `scripts/validate-package.py` revisa el paquete.

## Reglas para cambios

Mantén `SKILL.md` y `README.md` sincronizados.

- **Patrones:** numerados desde 1 sin huecos, del más fuerte y frecuente al más débil. Una señal nueva merece patrón solo si ninguno existente la cubre; prefiere integrarla en uno. Si agregas, quitas o renumeras, actualiza las tablas del README, el título "Los N patrones" y cada referencia con §. El validador cuenta los patrones por sus encabezados y revisa que los nombres del README coincidan con ellos.
- **Versión:** la misma en `metadata.version` de `SKILL.md`, en el primer encabezado de `CHANGELOG.md`, en `.claude-plugin/plugin.json` y en `.cursor-plugin/plugin.json`. No agregues un campo `version` de primer nivel.
- **Descripción:** los manifiestos y `package.json` usan la primera oración de la descripción de `SKILL.md`.
- **Compatibilidad:** instrucciones de instalación y uso neutrales. Claude Code, Cursor, OpenCode, Codex y pi son ejemplos, no límites.
- **Historial:** una nota corta en `CHANGELOG.md` por cada cambio de comportamiento o arreglo no obvio.
- **Upstream:** cuando blader publique una versión nueva de humanizer, compárala con esta y trae los cambios que apliquen al español. Anota en `CHANGELOG.md` la versión de upstream en la que se basa. No traigas reglas que permitan agregar datos: desde humanizer 4.0.0 upstream lo permite y esta skill no.
- **Revisiones:** antes de publicar, corre `python3 scripts/validate-package.py`, `npx skills add . --list` y `claude plugin validate .`.

## Cómo escribir aquí

Esta skill quita señales de IA, así que su propio texto no puede tenerlas: aplica la skill a lo que escribas en el repo.

- Español claro: lo principal primero, palabras comunes, voz activa, oraciones y párrafos cortos, un solo término por cosa.
- Sin rayas largas ni cortas, y con comillas rectas, salvo en los ejemplos que muestran esas señales (§8 y §23).
- Conserva exactos los identificadores, comandos, rutas, campos, citas, frases vigiladas y ejemplos.
- Mantén `SKILL.md` en 5,500 palabras o menos. El agente lee cada palabra en cada uso, así que un cambio que agrega palabras debe ganárselas: prefiere una instrucción corta y clara a otra excepción.
- Commits en español, en minúsculas y cortos. Sin trailers de atribución.
