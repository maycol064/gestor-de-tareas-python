"""Lógica principal de la aplicación de gestión de tareas.

Incluye la clase TaskManager, responsable de agregar, listar y completar
tareas, así como de guardar y cargar el estado en un archivo JSON.
"""

import json
import os
from datetime import datetime

from config import Config


class TaskManager:
    """Administra una lista de tareas y su persistencia en disco (JSON)."""

    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.tasks = []
        self.load_tasks()

    # ------------------------------------------------------------------
    # Operaciones principales
    # ------------------------------------------------------------------
    def add_task(self, description: str) -> dict:
        if not description or not description.strip():
            raise ValueError("La descripción de la tarea no puede estar vacía.")

        task = {
            "id": self._next_id(),
            "description": description.strip(),
            "completed": False,
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
        self.tasks.append(task)
        if self.config.debug_mode:
            print(f"[DEBUG] Tarea agregada: {task}")
        self.save_tasks()
        return task

    def list_tasks(self) -> list:
        return self.tasks

    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().isoformat(timespec="seconds")
                if self.config.debug_mode:
                    print(f"[DEBUG] Tarea completada: {task}")
                self.save_tasks()
                return True
        return False

    # ------------------------------------------------------------------
    # Persistencia JSON
    # ------------------------------------------------------------------
    def save_tasks(self):
        with open(self.config.data_file, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def load_tasks(self):
        if os.path.exists(self.config.data_file):
            with open(self.config.data_file, "r", encoding="utf-8") as f:
                try:
                    self.tasks = json.load(f)
                except json.JSONDecodeError:
                    self.tasks = []
        else:
            self.tasks = []

    # ------------------------------------------------------------------
    # Utilidades internas
    # ------------------------------------------------------------------
    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1
