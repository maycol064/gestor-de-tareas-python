# Gestor de Tareas (Task Manager)

Aplicación de consola en Python para la gestión básica de tareas, desarrollada
como actividad U2 A1: *Desarrollo y gestión de una aplicación de tareas*.

## Descripción del proyecto

La aplicación permite agregar tareas, listarlas y marcarlas como completadas.
Toda la configuración global de la app (por ejemplo, el modo debug) se
administra mediante el **patrón de diseño Singleton**, y las tareas se
**persisten automáticamente en un archivo JSON**, cargándose al iniciar el
programa y guardándose ante cada cambio.

### Funcionalidades

- Agregar nuevas tareas.
- Listar todas las tareas (pendientes y completadas).
- Marcar tareas como completadas.
- Activar/desactivar el modo debug (gestionado por el Singleton `Config`).
- Guardado y carga automática de tareas en `tasks.json`.

## Estructura del proyecto

```
├── config.py                  # Patrón Singleton (configuración global)
├── task_manager.py            # Lógica principal: agregar, listar, completar, persistencia JSON
├── main.py                    # Interfaz de consola (CLI)
├── tests/
│   ├── test_task_manager.py   # Pruebas unitarias (unittest)
│   └── resultados_pruebas.txt # Resultados de la ejecución de las pruebas
├── screenshots/                # Capturas de la aplicación en funcionamiento
├── .gitignore
└── README.md
```

## Patrón Singleton

La clase `Config` (en `config.py`) implementa el patrón Singleton mediante la
sobreescritura de `__new__`, garantizando que exista una única instancia de
configuración compartida por toda la aplicación (modo debug, nombre del
archivo de datos, etc.).

## Requisitos

- Python 3.10 o superior (sin dependencias externas para ejecutar la app).

## Cómo ejecutar la aplicación

```bash
python3 main.py
```

Se mostrará un menú interactivo:

```
===== Gestor de Tareas =====
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Activar/desactivar modo debug
5. Salir
=============================
```

Las tareas se guardan automáticamente en `tasks.json` en la misma carpeta.

## Cómo ejecutar las pruebas unitarias

Desde la raíz del proyecto:

```bash
python3 -m unittest tests.test_task_manager -v
```

Todas las pruebas cubren:
- El comportamiento Singleton de `Config`.
- Agregar tareas (caso válido y descripción vacía).
- Listar tareas.
- Completar tareas (ID válido e ID inexistente).
- Persistencia de tareas en el archivo JSON entre instancias.

## Control de versiones

El proyecto se desarrolló con Git, reflejando el avance en commits separados:

1. `Inicialización del proyecto y estructura básica.`
2. `Implementación del patrón Singleton.`
3. `Agregadas funciones para agregar, listar y completar tareas, con persistencia en JSON.`
4. `Pruebas unitarias con unittest para agregar y completar tareas.`

## Autor

Maycol Jair Flores Ruiz — Actividad U2 A1, Universidad Autónoma de Guadalajara (UAG).
