## Documentación del proyecto
Nombre:  John Sinclair
ID:  000545405
---

Proyecto: Sistema de seguimiento a mantenimientos de aeronaves

Nombre: ICARO

Tutorial
 1. Asegúrate de tener Git: Git es como un mensajero que trae el código desde GitHub a tu computadora. Si no lo tienes, descárgalo e instálalo desde https://git-scm.com/.
 2. Copia la dirección del repositorio: Ve a la página de GitHub donde está el código del sistema de gestión de aviones y copia la dirección (URL) que aparece en la barra de direcciones de tu navegador, en este caso (https://github.com/hacUPB/prog-2420-eval-u3-YrJohn.git)
 3. Abre la terminal de Git (Gitbash)
 4. Clona el repositorio:
   * En la terminal, escribe git clone y pega la dirección que copiaste en el paso 2.
   * Presiona Enter.
 5. Ve a la carpeta del repositorio:
   * En la terminal, escribe cd seguido del nombre de la carpeta que se acaba de crear, en este caso (prog-2420-eval-u3-YrJohn)
 6. Abre el archivo Main.py:
   * Puedes usar un editor como Visual Studio Code



Operatividad
Este sistema te permite gestionar el mantenimiento de una flota de aviones y el equipo de técnicos. A continuación, veras cómo utilizar las diferentes funciones del sistema:
1. Registrar un nuevo avión:
 * Selecciona la opción "Registrar nuevo avión" en el menú principal.
 * Ingresa la matrícula del avión.
 * Ingresa el modelo del avión.
 * Ingresa la capacidad del avión.
 * El sistema registrará el avión y lo añadirá a la flota.

2. Registrar un nuevo mantenimiento:
 * Selecciona la opción "Registrar nuevo mantenimiento" en el menú principal.
 * Ingresa la matrícula del avión al que se le realizará el mantenimiento.
 * Ingresa la fecha del mantenimiento.
 * Ingresa el tipo de mantenimiento ("preventivo" o "correctivo").
 * Ingresa el nombre del técnico que realizará el mantenimiento.
 * Ingresa cualquier observación relevante sobre el mantenimiento.
 * El sistema registrará el mantenimiento en el historial del avión.

3. Ver el historial de mantenimiento de un avión:
 * Selecciona la opción "Ver historiales" en el menú principal.
 * Ingresa la matrícula del avión.
 * El sistema mostrará el historial de mantenimiento del avión, incluyendo la fecha, el tipo, el técnico y las observaciones de cada mantenimiento.

4. Ver el estado de un avión:
 * Selecciona la opción "Estados de aviones" en el menú principal.
 * Ingresa la matrícula del avión.
 * El sistema mostrará el estado actual del avión ("operando" o "en mantenimiento").

5. Añadir un nuevo técnico:
 * Selecciona la opción "Añadir nuevo técnico" en el menú principal.
 * Ingresa el nombre del técnico.
 * Ingresa la especialidad del técnico.
 * El sistema añadirá al técnico a la lista de técnicos disponibles.

6. Eliminar un técnico:
 * Selecciona la opción "Eliminar técnico" en el menú principal.
 * Ingresa el nombre del técnico.
 * El sistema eliminará al técnico de la lista de técnicos.

7. Asignar un técnico a un mantenimiento:
 * Selecciona la opción "Asignacion de tecnicos" en el menú principal.
 * Ingresa el nombre del técnico.
 * El sistema marcará al técnico como "ocupado".

 8. Desasignar un técnico:
 * Selecciona la opción "Desasignar tecnico" en el menú principal.
 * Ingresa el nombre del técnico.
 * El sistema marcará al técnico como "disponible".

9. Ver la disponibilidad de un técnico:
 * Selecciona la opción "Ver tecnicos" en el menú principal.
 * Ingresa el nombre del técnico.
 * El sistema mostrará si el técnico está "disponible" u "ocupado".

10. Cerrar el programa:
 * Selecciona la opción "cerrar programa" en el menú principal.
 * El sistema terminará la ejecución.



 A tener en cuenta
 1. Precisión en la entrada de datos:  El sistema procesa la información de manera literal. Por lo tanto, es fundamental ser preciso al ingresar los datos, incluyendo nombres, matrículas y demás información. Asegúrese de utilizar las mayúsculas, minúsculas, tildes y espacios de forma consistente para evitar errores de interpretación por parte del sistema.
 2. Verificación de la ejecución:  Tras seleccionar una opción del menú y presionar Enter, el menú se actualiza rápidamente. Se recomienda prestar atención a la parte superior de la pantalla para verificar que la acción se ha realizado correctamente, ya que el sistema mostrará un mensaje de confirmación.
 
Tenga en cuenta estas consideraciones para garantizar un uso eficiente del sistema y evitar posibles inconvenientes.
