from gestor_tareas import GestorTareas


def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def leer_entero(mensaje):
    """Pide un número entero y repite la pregunta si el usuario escribe algo inválido."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Escribe un número entero válido.")


def leer_prioridad():
    """Pide la prioridad y solo acepta alta, media o baja."""
    while True:
        prioridad = input("Prioridad (alta, media, baja): ").strip().lower()
        if prioridad in ("alta", "media", "baja"):
            return prioridad
        print("Prioridad no válida. Escribe alta, media o baja.")


def leer_titulo():
    """Pide el título y no acepta que esté vacío."""
    while True:
        titulo = input("Título de la tarea: ").strip()
        if titulo:
            return titulo
        print("El título no puede estar vacío.")


def main():
    gestor = GestorTareas()
    opcion = 0

    while opcion != 5:
        mostrar_menu()
        opcion = leer_entero("Elige una opción: ")

        if opcion == 1:
            titulo = leer_titulo()
            prioridad = leer_prioridad()
            gestor.agregar_tarea(titulo, prioridad)
            print("Tarea agregada correctamente.")
        elif opcion == 2:
            print("\n--- LISTA DE TAREAS ---")
            gestor.listar_tareas()
        elif opcion == 3:
            id_tarea = leer_entero("Id de la tarea a completar: ")
            if gestor.completar_tarea(id_tarea):
                print("Tarea marcada como completada.")
            else:
                print("No existe una tarea con ese id.")
        elif opcion == 4:
            id_tarea = leer_entero("Id de la tarea a eliminar: ")
            if gestor.eliminar_tarea(id_tarea):
                print("Tarea eliminada.")
            else:
                print("No existe una tarea con ese id.")
        elif opcion == 5:
            print("Hasta pronto.")
        else:
            print("Opción no válida.")


# Este bloque hace que main() se ejecute solo al correr este archivo directamente
if __name__ == "__main__":
    main()