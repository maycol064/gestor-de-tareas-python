"""Pruebas unitarias para TaskManager y Config (patrón Singleton)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import Config
from task_manager import TaskManager


class TestConfigSingleton(unittest.TestCase):
    def setUp(self):
        Config._instance = None

    def test_singleton_returns_same_instance(self):
        a = Config()
        b = Config()
        self.assertIs(a, b)

    def test_config_values_shared_across_instances(self):
        a = Config(debug_mode=True, data_file="a.json")
        b = Config(debug_mode=False, data_file="b.json")
        self.assertTrue(b.debug_mode)
        self.assertEqual(b.data_file, "a.json")


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        Config._instance = None
        self.test_file = "test_tasks_tmp.json"
        self.config = Config(debug_mode=False, data_file=self.test_file)
        self.manager = TaskManager(self.config)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        Config._instance = None

    def test_add_task(self):
        task = self.manager.add_task("Comprar víveres")
        self.assertEqual(task["description"], "Comprar víveres")
        self.assertFalse(task["completed"])
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_empty_description_raises(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_list_tasks_returns_all(self):
        self.manager.add_task("Tarea 1")
        self.manager.add_task("Tarea 2")
        self.assertEqual(len(self.manager.list_tasks()), 2)

    def test_complete_task(self):
        task = self.manager.add_task("Lavar el auto")
        result = self.manager.complete_task(task["id"])
        self.assertTrue(result)
        self.assertTrue(self.manager.list_tasks()[0]["completed"])

    def test_complete_task_invalid_id_returns_false(self):
        result = self.manager.complete_task(999)
        self.assertFalse(result)

    def test_tasks_persist_to_json_file(self):
        self.manager.add_task("Persistir en JSON")
        self.assertTrue(os.path.exists(self.test_file))

        new_manager = TaskManager(self.config)
        self.assertEqual(len(new_manager.list_tasks()), 1)
        self.assertEqual(new_manager.list_tasks()[0]["description"], "Persistir en JSON")


if __name__ == "__main__":
    unittest.main()
