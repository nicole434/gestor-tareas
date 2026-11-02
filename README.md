# Gestor de Tareas

Aplicación de consola hecha en Python que permite organizar tareas pendientes. Fue desarrollada con ayuda de un asistente de IA (Claude) como parte de la actividad de la asignatura Herramientas Avanzadas para el Desarrollo de Aplicaciones (102HAD1), UTLA.

## Funcionalidades

1. **Agregar tarea:** registra un título y una prioridad (alta, media o baja).
2. **Listar tareas:** muestra todas las tareas con su id y su estado (`[ ]` pendiente, `[X]` completada).
3. **Marcar como completada:** cambia el estado de una tarea indicando su id.
4. **Eliminar tarea:** borra una tarea indicando su id.

El programa también valida los datos: no acepta letras donde se piden números, ni títulos vacíos, ni prioridades distintas de alta, media o baja.

## Tecnologías

- Python 3
- Visual Studio Code
- Git y GitHub

## Estructura del proyecto

```
gestor-tareas/
├── tarea.py           # Clase que representa una tarea
├── gestor_tareas.py   # Lógica: agregar, listar, completar y eliminar
├── main.py            # Menú principal en consola
├── .gitignore
└── README.md
```

## Cómo ejecutarlo

1. Tener instalado Python 3.8 o superior.
2. Clonar el repositorio:
   ```
   git clone https://github.com/nicole434/gestor-tareas.git
   cd gestor-tareas
   ```
3. Ejecutar el programa:
   ```
   python main.py
   ```
   También se puede abrir la carpeta en VS Code y ejecutar `main.py` con el botón Run.

## Cómo usé la IA

Usé Claude como asistente de programación. Le pedí una propuesta de módulo y una estructura sencilla, y la revisé antes de aceptarla. Luego desarrollé el código por partes (primero `Tarea`, después `GestorTareas` y al final `main.py`), pidiendo explicaciones de cada una. Probé cada funcionalidad en la terminal, incluyendo datos inválidos, para comprobar que el programa no se cayera.

Ejemplos de instrucciones que le di:

- *"Me puedes ayudar en hacer esta actividad que pide en el documento y las herramientas en utilizar sera que utilizare VS Code, puedo utilizar Python, puedes hacer algo con ese lenguaje."* La IA propuso un gestor de tareas en consola con tres archivos; revisé que cumpliera con los requisitos de la actividad y lo acepté.
- Le compartí capturas de la ejecución para que revisara si todo funcionaba. Me indicó que la validación se veía bien, pero que algunas capturas debían repetirse porque una estaba torcida y otra mostraba un error de escritura en el comando, así que las volví a tomar.

Entiendo el código entregado y puedo explicar cada una de sus partes.