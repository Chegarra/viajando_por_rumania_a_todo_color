# Viajando por Rumania a todo color

Este proyecto es una herramienta de línea de comandos que encuentra la ruta más corta entre dos ciudades de Rumania. Utiliza una implementación del **algoritmo de Dijkstra** para calcular la distancia mínima y el camino a seguir sobre un grafo que representa las principales ciudades y las distancias entre ellas.

## 🚀 Características

- **Cálculo de ruta óptima**: Encuentra el camino más corto en términos de distancia.
- **Interfaz de línea de comandos (CLI)**: Fácil de usar desde cualquier terminal.
- **Resultados claros**: Muestra la ruta completa paso a paso y la distancia total del recorrido.
- **Gestión de dependencias**: Utiliza Poetry para una fácil instalación y manejo del entorno.

## 📋 Requisitos

- Python (versión 3.8 o superior)
- Poetry para gestionar las dependencias del proyecto.

## ⚙️ Instalación y Configuración

Sigue estos pasos para poner en marcha el proyecto en tu máquina local.

### 1. Clonar el repositorio

```bash
git clone git@github.com:Chegarra/viajando_por_rumania_a_todo_color.git
cd viajando_por_rumania_a_todo_color
```

### 2. Instalar dependencias

Una vez dentro del directorio del proyecto, instala las dependencias definidas en `pyproject.toml` usando Poetry:

```bash
poetry install
```

### 3. Activar el entorno virtual de Poetry

Aunque no es estrictamente necesario para el siguiente paso, si deseas trabajar dentro del entorno virtual, puedes activarlo con este comando:

```bash
poetry env activate
```

### 4. Ejecutar el programa

Una vez activado el entorno, puedes ejecutar el programa. El programa toma dos argumentos: la ciudad de origen y la ciudad de destino.

```bash
poetry run python ./src/main.py <ciudad_origen> <ciudad_destino>
```

**Ejemplo de uso:**

Para encontrar el camino más corto de Arad a Bucharest:

```bash
poetry run python ./src/main.py Bucharest Lugoj
