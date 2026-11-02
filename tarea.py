class Tarea:
    """Representa una tarea con su título, prioridad y estado."""

    def __init__(self, id_tarea, titulo, prioridad):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.prioridad = prioridad
        self.completada = False  # toda tarea nueva empieza pendiente

    # Define cómo se muestra la tarea cuando se imprime en pantalla
    def __str__(self):
        estado = "[X]" if self.completada else "[ ]"
        return f"{estado} [{self.id_tarea}] {self.titulo:<25} (prioridad: {self.prioridad})"