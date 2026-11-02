from tarea import Tarea


class GestorTareas:
    """Maneja la lista de tareas: agregar, listar, completar y eliminar."""

    def __init__(self):
        self.tareas = []         # lista donde se guardan las tareas
        self.siguiente_id = 1    # contador para dar un id único a cada tarea

    # Funcionalidad 1: agregar una tarea nueva
    def agregar_tarea(self, titulo, prioridad):
        nueva = Tarea(self.siguiente_id, titulo, prioridad)
        self.tareas.append(nueva)
        self.siguiente_id += 1

    # Funcionalidad 2: mostrar todas las tareas
    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        for tarea in self.tareas:
            print(tarea)

    # Funcionalidad 3: marcar una tarea como completada
    # Devuelve True si la encontró, False si no existe ese id
    def completar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                tarea.completada = True
                return True
        return False

    # Funcionalidad 4: eliminar una tarea por su id
    # Devuelve True si la eliminó, False si no existe ese id
    def eliminar_tarea(self, id_tarea):
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False