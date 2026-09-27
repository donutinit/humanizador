#!/usr/bin/env python3
"""Revisa los archivos del paquete del Humanizador sin dependencias externas."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def read_package_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise SystemExit(f"No se puede leer {path.relative_to(ROOT)}: {error}")


def require_match(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


SKILL_PATH = ROOT / "SKILL.md"
SKILL = read_package_file(SKILL_PATH)
README = read_package_file(ROOT / "README.md")
AGENTS = read_package_file(ROOT / "AGENTS.md")
try:
    PLUGIN = json.loads(read_package_file(ROOT / ".claude-plugin" / "plugin.json"))
except json.JSONDecodeError as error:
    raise SystemExit(f"Corrige el JSON de .claude-plugin/plugin.json: {error}")

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
if name != "humanizador" or PLUGIN.get("name") != "humanizador":
    raise SystemExit("El nombre debe ser 'humanizador' en SKILL.md y en plugin.json")

skill_version = require_match(
    re.search(r'(?m)^\s+version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$', yaml_metadata),
    "Agrega metadata.version a SKILL.md con tres partes",
).group(1)
readme_version = require_match(
    re.search(r"(?m)^- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README),
    "Agrega una entrada de versión al README.md",
).group(1)
package_versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(package_versions) != 1:
    raise SystemExit(f"Usa una sola versión en todos los archivos: {sorted(package_versions)}")

skill_files = {path.relative_to(ROOT) for path in ROOT.rglob("SKILL.md")}
if SKILL_PATH.is_symlink() or skill_files != {Path("SKILL.md")}:
    raise SystemExit("Deja una sola SKILL.md normal en la raíz del repo")
if PLUGIN.get("skills") != ["./"]:
    raise SystemExit("Apunta el cargador de skills del plugin a la raíz del repo")

pattern_numbers = [int(n) for n in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)]
pattern_count = len(pattern_numbers)
if pattern_count == 0 or pattern_numbers != list(range(1, pattern_count + 1)):
    raise SystemExit(f"Numera los patrones de SKILL.md desde 1 sin huecos: {pattern_numbers}")

readme_numbers = [int(n) for n in re.findall(r"(?m)^\| ([0-9]+) \|", README)]
if sorted(readme_numbers) != pattern_numbers:
    raise SystemExit(
        f"Las tablas del README deben listar los patrones 1 a {pattern_count} una vez: {sorted(readme_numbers)}"
    )
if f"## Los {pattern_count} patrones" not in README:
    raise SystemExit(f"Titula la sección de patrones del README 'Los {pattern_count} patrones'")

for reference in re.findall(r"§([0-9]+)", SKILL + README + AGENTS):
    if not 1 <= int(reference) <= pattern_count:
        raise SystemExit(f"Referencia a un patrón que no existe: §{reference}")

if len(SKILL.splitlines()) > 400:
    raise SystemExit("Mantén SKILL.md en 400 líneas o menos")

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
for path in ("README.md", "AGENTS.md"):
    for line_number, line in enumerate(read_package_file(ROOT / path).splitlines(), 1):
        if TELLS.search(line):
            raise SystemExit(f"{path}:{line_number}: raya o comilla curva")

print(f"Paquete del Humanizador v{skill_version} válido ({pattern_count} patrones)")
