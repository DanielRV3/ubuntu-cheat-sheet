# Cheat Sheet Linux

Este repositorio conteiente una cheat sheet de comandos de linux vistos en el curso de Proyecto Integrador y Comprensivo II.

Basado en Ubuntu 24.04

## Requisitos

### Python
- Python 3.9 o superior

## Instalación
### Entorno Virtual

Crear y activar un entorno virtual de python para evitar instalar dependencias globalmente:

**Windows:**
```powershell
python -m venv .venv

.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **Nota:** El entorno virtual debe ser activado cada que corre la aplicación

### Clonar repositorio

```bash
git clone https://github.com/DanielRV3/ubuntu-cheat-sheet.git
```

## Uso
* Dirigirse a la carpeta donde fue clonado el repositorio
* Activar el entorno virtual
* Ejecutar la aplicación
```bash
python app.py
```