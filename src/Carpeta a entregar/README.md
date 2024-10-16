## Documentación del proyecto
Nombre:  John Sinclair
ID:  000545405
---

Proyecto: Sistema de seguimiento a mantenimientos de aeronaves

Nombre: ICARO

Descripción:
Este sistema facilita el seguimiento del mantenimiento de flotas de aviones. Permite registrar información detallada de cada aeronave, incluyendo modelo, matrícula y otros datos relevantes para su identificación. Además, registra cada mantenimiento realizado, incluyendo la fecha, el tipo de mantenimiento (preventivo o correctivo) y el técnico responsable.
Este sistema es crucial para la gestión de flotas de aviones, ya que permite garantizar la seguridad y operatividad de las aeronaves de acuerdo con la normativa vigente, llevando un registro histórico preciso y accesible de todas las intervenciones realizadas.

Estructura:
El sistema utiliza diccionarios para almacenar la información de cada avión, incluyendo sus datos de identificación y el historial de mantenimientos. Para la gestión de los técnicos y su disponibilidad, se emplean conjuntos.

Alcance:
Este programa se centra en el registro de flotas de aviones, incluyendo detalles como matrículas, modelos y capacidad de cada aeronave. Además, permite registrar los mantenimientos realizados a cada avión, generando un historial completo, preciso y seguro.
Dirigido principalmente a empresas aeronáuticas, este sistema facilita el seguimiento organizado de los mantenimientos, agiliza el acceso a la información y contribuye a garantizar la seguridad y operatividad de las flotas.




Comentarios/analisis del programa 

Funciones a utilizar (def):
1. Registrar avion (utilizado para ingresar un nuevo avion a cierta instalacion)
2. Registrar mantenimiento (utilizado para llevar el registro de los trabajos realizados)
3. Ver historial (utilizado para ver todos los movientos hechos a un avion en especifico)
4. Estado avion (utilizado para ver la operatividad y/o condiciones de una aeronave)
5. Añadir tecnico (utilizado para gestionar y vincular los tecnicos de las instalaciones)
6. Eliminar tecnico (utilizado para hacer que un tecnico deje de estar vinculado al grupo de trabajo)
7. Asignar tecnico (utilizado para cambiar el estado de los tecnicos y asi poder llevar un control de que tanto trabajan)
8. Desasignar tecnico (utilizado para cambiar el estado de los tecnicos)
9. ver tecnico (utilizado para visualizar el estado de trabajo de los tecnicos y asi poder ver a quien aignar trabajos)




Pseudocodigo (muy general):
Inicio 
1. Solicitar matricula del avión
2. Verificar si el avión esta registrado
3. En caso de no estarlo, informar al usuario
4. Solicitar tipo de mantenimiento, tecnico, fecha y observaciones
5. Agregar el mantenimiento al historial del avión 
6. Cambiar estado del avión a "En mantenimiento" si es necesario 
7. Mostrar mensaje de exito
Fin 

peudocodigo registrar avion
Inicio
1. Solicitar matricula del avion
2. Añadir nueva entrada al diccionario (matricula)
3. Solicitar Modelo 
4. Añadir nueva entrada al diccionario (modelo)
5. Solicitar capacidad
6. Añadir nueva entrada al diccionario (capacidad)
7. Añadir (estado) al diccionario
8. Añadir (historial) al diccionario 
9. informar a usuario registro exitoso
fin.

Pseudocodigo registro mantenimientos
Inicio
1. Preguntar que tecnico esta operando
2. Añadir nombre tecnico a registro mantenimiento 
3. Preguntar fecha
4. Añadir fecha a registro mantenimiento
5. Preguntar tipo de mantenimiento 
6. añadir tipo mantenimiento a registro
7. preguntar observaciones
8. añadir observaciones a registro
9. Preguntar avion al que se le hizo mantenimiento
10. añadir registro a avion ingresado 
Fin

Posibles mejoras/falencias
1. Considero que el codigo hace lo que debe, el problema llega a la hora de navegar entre las opciones, pues se supone que es un programa que deberia estar en continua operacion, no que "pare" o que debas por asi decir reiniciar a cada rato.
2. Me hubiera gustado agregar algunas otras cosas como poder buscar mediante fechas los mantenimientos, o por tecnicos, etc. siento que el codigo acabo siendo un poco limitado en cuanto a versatilidad.



Explicacion codigo
1. Zona de diccionarios y conjuntos vacíos:
 * aviones = {}:  Este diccionario almacenará la información de cada avión, utilizando la matrícula como clave.
 * tecnicos_disponibles = set(): Este conjunto almacenará los nombres de los técnicos disponibles para realizar mantenimiento.
 * tecnicos_ocupados = set(): Este conjunto almacenará los nombres de los técnicos que actualmente están ocupados en un mantenimiento.
 * tecnicos = {}: Este diccionario almacenará información de cada técnico, utilizando el nombre como clave.

2. Zona de funciones (def):
 - registrar_avion(matricula, modelo, capacidad):
   * Verifica si la matrícula ya existe en el diccionario aviones.
   * Si no existe, crea una nueva entrada en el diccionario con la información del avión, incluyendo un historial de mantenimiento vacío y un estado inicial de "operando".
 - registrar_mantenimiento(matricula, fecha, tipo, tecnico, observaciones=""):
   * Verifica si el avión existe en el diccionario aviones.
   * Agrega un nuevo registro de mantenimiento al historial del avión.
   * Actualiza el estado del avión a "en mantenimiento" si el tipo de mantenimiento es "correctivo". Si es "preventivo", el estado se mantiene o se cambia a "Operando".
 - ver_historial(matricula):
   * Verifica si el avión existe.
   * Si existe, imprime el historial de mantenimiento del avión de forma organizada, incluyendo la fecha, el tipo, el técnico y las observaciones de cada mantenimiento.
 - estado_avion(matricula):
   * Verifica si el avión existe.
   * Imprime el estado actual del avión ("operando" o "en mantenimiento").
 - añadir_tecnico(nombre, especialidad):
   * Verifica si el técnico ya existe en el diccionario tecnicos.
   * Si no existe, lo agrega al diccionario y al conjunto tecnicos_disponibles.
 - eliminar_tecnico(nombre):
   * Elimina al técnico del diccionario tecnicos y del conjunto tecnicos_disponibles (asumiendo que no está ocupado).
 - asignar_tecnico(nombre):
   * Mueve al técnico del conjunto tecnicos_disponibles al conjunto tecnicos_ocupados.
 - desasignar_tecnico(nombre):
   * Mueve al técnico del conjunto tecnicos_ocupados al conjunto tecnicos_disponibles.
 - ver_tecnico(nombre):
   * Indica si el técnico está disponible, ocupado o no está registrado.
 - seleccionar_opcion(opciones):
   * Muestra un menú de opciones al usuario y permite que seleccione una opción. Valida la entrada del usuario para asegurarse de que sea una opción válida.

3. CODIGO (Interfaz de usuario):
 * Esta sección presenta un bucle while que se ejecuta continuamente hasta que el usuario elige la opción "cerrar programa".
 * Dentro del bucle, se muestra un menú de opciones al usuario utilizando la función seleccionar_opcion.
 * Dependiendo de la opción seleccionada, se solicita al usuario la información necesaria y se llama a la función correspondiente para realizar la acción.
