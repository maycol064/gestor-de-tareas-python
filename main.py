"""Aplicación de gestión de tareas (CLI).

Funcionalidades: agregar tareas, listar tareas y marcar tareas como
completadas. La configuración global (por ejemplo, el modo debug) se
gestiona mediante un Singleton (ver config.py) y las tareas se persisten
automáticamente en un archivo JSON (ver task_manager.py).
"""

from config import Config
from task_manager import TaskManager

MENU = """
===== Gestor de Tareas =====
1. Agregar tarea
2. Listar tareas
3. Marcar tarea como completada
4. Activar/desactivar modo debug
5. Salir
=============================
"""


def print_tasks(tasks):
    if not tasks:
        print("No hay tareas registradas.")
        return
    for task in tasks:
        estado = "✔ Completada" if task["completed"] else "✗ Pendiente"
        print(f"[{task['id']}] {task['description']} - {estado}")


def run():
    config = Config(debug_mode=False, data_file="tasks.json")
    manager = TaskManager(config)

    print("Bienvenido al Gestor de Tareas")
    print(f"Configuración activa: {config}")

    while True:
        print(MENU)
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            descripcion = input("Descripción de la nueva tarea: ")
            try:
                tarea = manager.add_task(descripcion)
                print(f"Tarea agregada correctamente: {tarea['description']}")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            print_tasks(manager.list_tasks())

        elif opcion == "3":
            try:
                task_id = int(input("ID de la tarea a completar: "))
            except ValueError:
                print("Debes ingresar un número de ID válido.")
                continue
            if manager.complete_task(task_id):
                print(f"Tarea {task_id} marcada como completada.")
            else:
                print(f"No se encontró una tarea con ID {task_id}.")

        elif opcion == "4":
            nuevo_estado = config.toggle_debug()
            print(f"Modo debug ahora está: {'activado' if nuevo_estado else 'desactivado'}")

        elif opcion == "5":
            print("Guardando tareas antes de salir...")
            manager.save_tasks()
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    run()
