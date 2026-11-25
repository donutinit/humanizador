#!/usr/bin/env python3
"""Revisa los archivos del paquete del Humanizador sin dependencias externas."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
NAME = "humanizador"


def read_package_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"No se puede leer {path.relative_to(ROOT)}: {error}")


def read_json(path: Path) -> dict:
    try:
        return json.loads(read_package_file(path))
    except json.JSONDecodeError as error:
        raise SystemExit(f"Corrige el JSON de {path.relative_to(ROOT)}: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read_package_file(SKILL_PATH)
README = read_package_file(ROOT / "README.md")
CHANGELOG = read_package_file(ROOT / "CHANGELOG.md")
AGENTS = read_package_file(ROOT / "AGENTS.md")
PLUGIN = read_json(ROOT / ".claude-plugin" / "plugin.json")
MARKETPLACE = read_json(ROOT / ".claude-plugin" / "marketplace.json")
CURSOR_PLUGIN = read_json(ROOT / ".cursor-plugin" / "plugin.json")
PACKAGE = read_json(ROOT / "package.json")

if read_package_file(ROOT / "CLAUDE.md") != AGENTS:
    raise SystemExit("CLAUDE.md debe ser igual a AGENTS.md: recréalo con ln -f AGENTS.md CLAUDE.md")

yaml_metadata = require_match(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md debe empezar con metadatos YAML",
).group(1)

for unsupported_field in ("version:", "compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(unsupported_field)}", yaml_metadata):
        raise SystemExit(f"Quita el campo YAML no soportado: {unsupported_field[:-1]}")

name = require_match(
    re.search(r"(?m)^name:\s*(\S+)\s*$", yaml_metadata), "Agrega name a SKILL.md"
).group(1)
package_names = {
    "SKILL.md": name,
    ".claude-plugin/plugin.json": PLUGIN.get("name"),
    ".cursor-plugin/plugin.json": CURSOR_PLUGIN.get("name"),
    "package.json": PACKAGE.get("name"),
    **{
        f"marketplace.json ({index})": plugin.get("name")
        for index, plugin in enumerate(MARKETPLACE.get("plugins", []))
    },
}
wrong_names = [path for path, value in package_names.items() if value != NAME]
if wrong_names:
    raise SystemExit(f"El nombre debe ser '{NAME}' en: {', '.join(wrong_names)}")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata),
    "Agrega metadata.version a SKILL.md con tres partes",
).group(1)
changelog_version = require_match(
    re.search(r"(?m)^## ([0-9]+\.[0-9]+\.[0-9]+)(?: \([0-9-]+\))?$", CHANGELOG),
    "Agrega un encabezado de versión a CHANGELOG.md",
).group(1)
package_versions = {
    skill_version,
    changelog_version,
    str(PLUGIN.get("version", "")),
    str(CURSOR_PLUGIN.get("version", "")),
}
if len(package_versions) != 1:
    raise SystemExit(f"Usa una sola versión en todos los archivos: {sorted(package_versions)}")
if "version" in PACKAGE:
    raise SystemExit("Quita version de package.json: pi instala desde git")

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Deja una sola SKILL.md normal en la raíz del repo")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Apunta el cargador de skills del plugin de Claude a la raíz del repo")
if "$schema" in PLUGIN:
    raise SystemExit("Quita $schema de .claude-plugin/plugin.json: causa un aviso al sincronizar")
if "skills" in CURSOR_PLUGIN:
    raise SystemExit("Quita skills del plugin de Cursor para que cargue la SKILL.md de la raíz")
if PACKAGE.get("pi", {}).get("skills") != ["./"]:
    raise SystemExit("Apunta pi.skills de package.json a la raíz del repo")

skill_description = " ".join(
    require_match(
        re.search(r"(?m)^description: \|\n((?:  .*\n)+)", yaml_metadata + "\n"),
        "Escribe la descripción de SKILL.md como bloque con sangría",
    ).group(1).split()
)
package_descriptions = {
    str(PLUGIN.get("description", "")),
    str(CURSOR_PLUGIN.get("description", "")),
    str(PACKAGE.get("description", "")),
    *(str(plugin.get("description", "")) for plugin in MARKETPLACE.get("plugins", [])),
}
if len(package_descriptions) != 1 or not skill_description.startswith(
    next(iter(package_descriptions))
):
    raise SystemExit(
        "Usa la primera oración de la descripción de SKILL.md en los manifiestos y package.json: "
        f"{sorted(package_descriptions)}"
    )

skill_patterns = {
    int(number): title.strip()
    for number, title in re.findall(r"(?m)^### ([0-9]+)\. (.+)$", SKILL)
}
pattern_numbers = list(skill_patterns)
pattern_count = len(pattern_numbers)
if pattern_count == 0 or pattern_numbers != list(range(1, pattern_count + 1)):
    raise SystemExit(f"Numera los patrones de SKILL.md desde 1 sin huecos: {pattern_numbers}")

readme_rows = re.findall(r"(?m)^\| ([0-9]+) \| ([^|]+?) \|", README)
readme_patterns = {int(number): title.strip() for number, title in readme_rows}
if len(readme_rows) != pattern_count or sorted(readme_patterns) != pattern_numbers:
    raise SystemExit(
        f"Las tablas del README deben listar los patrones 1 a {pattern_count} una vez: "
        f"{[int(number) for number, _ in readme_rows]}"
    )
renamed = [
    f"{number}: {readme_patterns[number]!r} debe ser {title!r}"
    for number, title in skill_patterns.items()
    if readme_patterns[number] != title
]
if renamed:
    raise SystemExit("Usa en el README los mismos nombres de patrón que en SKILL.md: " + "; ".join(renamed))
if f"## Los {pattern_count} patrones" not in README:
    raise SystemExit(f"Titula la sección de patrones del README 'Los {pattern_count} patrones'")

# Una renumeración puede dejar un § apuntando a otro patrón o a ninguno. CHANGELOG.md
# conserva los números de cada versión, así que no se revisa.
for reference in re.findall(r"§([0-9]+)", SKILL + README + AGENTS):
    if not 1 <= int(reference) <= pattern_count:
        raise SystemExit(f"Referencia a un patrón que no existe: §{reference}")

# El agente lee cada palabra de SKILL.md en cada uso, así que el límite va en palabras.
skill_words = len(SKILL.split())
if skill_words > 5500:
    raise SystemExit(f"Mantén SKILL.md en 5,500 palabras o menos; tiene {skill_words}")

# El repo tampoco debe tener las señales que quita: rayas y comillas curvas solo pueden
# aparecer en los patrones que las muestran (§8 y §23).
TELLS = re.compile("[—–“”]")
allowed = {8, 23}
section = 0
for line_number, line in enumerate(SKILL.splitlines(), 1):
    heading = re.match(r"^### ([0-9]+)\. ", line)
    if heading:
        section = int(heading.group(1))
    elif line.startswith("## "):
        section = 0
    if TELLS.search(line) and section not in allowed:
        raise SystemExit(f"SKILL.md:{line_number}: raya o comilla curva fuera de §8/§23")
for path in ("README.md", "CHANGELOG.md", "AGENTS.md"):
    for line_number, line in enumerate(read_package_file(ROOT / path).splitlines(), 1):
        if TELLS.search(line):
            raise SystemExit(f"{path}:{line_number}: raya o comilla curva")

print(
    f"Paquete del Humanizador v{skill_version} válido "
    f"({pattern_count} patrones, {skill_words} palabras en SKILL.md)"
)
