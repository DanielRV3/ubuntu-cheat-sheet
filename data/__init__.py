"""
Carga las categorías desde commands.json.
Cada comando es un dict con:
    cmd   (str)           nombre del comando
    desc  (str)           descripción breve
    flags (list, opcional) lista de {"flag": str, "desc": str}
"""

import json
from pathlib import Path

JSON_PATH = Path(__file__).parent / "commands.json"


def cargar_categorias() -> dict[str, list[dict]]:
    with open(JSON_PATH, encoding="utf-8") as f:
        return json.load(f)
