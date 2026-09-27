# Guía para agentes

Cómo cambiar el Humanizador sin romper el paquete ni la skill. `CLAUDE.md` es un hard link de este archivo: son el mismo, para Claude, Codex y OpenCode.

## Qué hay en el repo

Una skill en Markdown, sin paso de build. `SKILL.md` es lo que leen los agentes. Es una adaptación al español de [blader/humanizer](https://github.com/blader/humanizer).

Mantén la skill portable: nada de instrucciones que la limiten a una o dos herramientas.

## Archivos

- `SKILL.md` es la fuente de verdad y el único archivo de skill. Tiene metadatos YAML portables, la explicación de por qué el texto de IA suena como suena y los patrones numerados en cinco grupos, del más fuerte al más débil.
- `README.md` explica instalación, uso, patrones e historial de versiones.
- `.claude-plugin/plugin.json` describe el plugin de Claude y apunta a la `SKILL.md` de la raíz.
- `.claude-plugin/marketplace.json` permite agregar este repo como marketplace de Claude.
- `agents/openai.yaml` tiene el nombre, la descripción corta y el prompt por defecto para agentes compatibles con OpenAI (Codex).
- `scripts/validate-package.py` revisa el paquete.

## Reglas para cambios

Mantén `SKILL.md` y `README.md` sincronizados.

- **Patrones:** numerados desde 1 sin huecos, del más fuerte y frecuente al más débil. Una señal nueva merece patrón solo si ninguno existente la cubre; prefiere integrarla en uno. Si agregas, quitas o renumeras, actualiza las tablas del README, el título "Los N patrones" y cada referencia con §. El validador cuenta los patrones por sus encabezados.
- **Versión:** la misma en `metadata.version` de `SKILL.md`, en la primera entrada del historial del README y en `.claude-plugin/plugin.json`. No agregues un campo `version` de primer nivel.
- **Compatibilidad:** instrucciones de instalación y uso neutrales. Claude Code, OpenCode y Codex son ejemplos, no límites.
- **Historial:** una nota corta en el README por cada cambio de comportamiento o arreglo no obvio.
- **Upstream:** cuando blader publique una versión nueva de humanizer, compárala con esta y trae los cambios que apliquen al español. Anota en el historial la versión de upstream en la que se basa.
- **Revisiones:** antes de publicar, corre `python3 scripts/validate-package.py`, `npx skills add . --list` y `claude plugin validate .`.

## Cómo escribir aquí

Esta skill quita señales de IA, así que su propio texto no puede tenerlas: aplica la skill a lo que escribas en el repo.

- Español claro: lo principal primero, palabras comunes, voz activa, oraciones y párrafos cortos, un solo término por cosa.
- Sin rayas largas ni cortas, y con comillas rectas, salvo en los ejemplos que muestran esas señales (§8 y §23).
- Conserva exactos los identificadores, comandos, rutas, campos, citas, frases vigiladas y ejemplos.
- Mantén `SKILL.md` en 400 líneas o menos: prefiere una instrucción corta y clara a otra excepción.
- Commits en español, en minúsculas y cortos. Sin trailers de atribución.
