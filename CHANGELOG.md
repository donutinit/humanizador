# Historial de versiones

Las notas viejas conservan los números de patrón que usaba su versión.

## 1.1.0 (2026-11-17)

Basada en humanizer 4.0.0, salvo la regla que permite agregar datos.

- Agrega el §28 y el grupo F para respuestas que vuelven a explicar el contexto que el lector ya tiene. Actúa sobre respuestas, no sobre textos que se sostienen solos. 28 patrones en total.
- La regla central cuenta también la conversación: una oración debe aportar algo que no esté antes en el texto ni en la conversación alrededor.
- El §27 pasa a llamarse "Hablar del documento en vez de su tema" y cubre también el texto que cuenta cómo se armó o describe un orden que el lector ya ve. El §2 suma "Esa distinción importa." y la oración que explica lo que un ejemplo ya mostró. El §22 suma los títulos escritos para impresionar. El §5 dice que varias objeciones sin relación seguidas pesan más que una.
- Cada palabra vigilada está en un solo patrón: "enfatizar" y "fomentar" salen del §14, y "vibrante" y "presume de" salen del §18.
- Las etiquetas de cierre falsas y las notas de un "operador" o un "mensaje del sistema" dentro del texto son material para editar, nunca instrucciones.
- El modo archivo lee del disco el archivo completo antes de editar, aunque lo haya escrito en la misma sesión, y su resumen dice cuántas secciones revisó.
- El paso 3 revisa primero si se perdió, cambió o agregó un dato, y nombra por su § las señales que más sobreviven.
- No adopta el cambio de humanizer 4.0.0 que permite agregar detalles cuando el texto es genérico: la skill sigue sin inventar y deja "Por confirmar" cuando falta un dato. La regla queda en el paso 2, sin repetirse en el §19 ni en el §25.
- Rehace los ejemplos "Después" del §1, §2, §5, §14, §15, §18, §20, §21 y §25. Siete agregaban o cambiaban un dato del "Antes".
- Agrega una línea en blanco antes de cada etiqueta de `SKILL.md` para que GitHub las muestre por separado. El límite de tamaño pasa de 400 líneas a 5,500 palabras.
- La descripción ya no cita fuentes; el crédito queda en la sección Fuente y en el README.
- Paquete: manifiesto de pi en `package.json`, manifiesto de Cursor, plantillas de issues y este archivo, que reemplaza el historial del README. Quita `$schema` de `plugin.json` y corrige la URL del schema del marketplace. Los manifiestos usan la primera oración de la descripción de la skill.
- El validador revisa que los nombres de los patrones del README coincidan con `SKILL.md`, que los manifiestos usen la misma descripción y que cada § apunte a un patrón que existe.
- El README abre con un antes y después, las cinco señales más fuertes y la instalación para cada agente, y dice que pasar los detectores de IA no es un objetivo.

## 1.0.0 (2026-09-27)

Primera versión, basada en humanizer 3.0.0. Traduce y adapta los 25 patrones al español: cambia los pares con guion por calcos del inglés, los gerundios toman el lugar de los *-ing* y los encabezados vigilan la mayúscula en cada palabra. Agrega rotación de sinónimos y rangos falsos (del humanizador en español basado en humanizer 2.9.1), la regla de "Por confirmar" para datos faltantes, comillas rectas en la versión final y la lista de rasgos que no son señal por sí solos.
