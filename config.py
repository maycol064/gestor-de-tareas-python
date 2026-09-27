"""Configuración global de la aplicación implementada con el patrón Singleton."""


class Config:
    """Configuración global compartida por toda la aplicación.

    Al ser un Singleton, cualquier parte del programa que solicite una
    instancia de Config recibe siempre el mismo objeto, garantizando que
    valores como `debug_mode` o `data_file` sean consistentes en toda la app.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, debug_mode: bool = False, data_file: str = "tasks.json"):
        if self._initialized:
            return
        self.debug_mode = debug_mode
        self.data_file = data_file
        self._initialized = True

    def toggle_debug(self):
        self.debug_mode = not self.debug_mode
        return self.debug_mode

    def __repr__(self):
        return f"Config(debug_mode={self.debug_mode}, data_file='{self.data_file}')"


if __name__ == "__main__":
    a = Config()
    b = Config()
    print("¿a y b son la misma instancia?", a is b)
    print(a)
