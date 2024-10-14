## Documentación del proyecto
Nombre:  John Sinclair
ID:  000545405
---

Proyecto: Sistema de seguimiento a mantenimientos de aeronaves

Nombre: ICARO

Descripcion: Este codigo seria un sistema de seguimiento para el mantenimiento de uno o mas aviones, incluiria los modelos, placas y toda ladocumentacion necesaria para identificar de manera precisa al avion al que se le hizo dicho mantenimiento, de igual manera incluiria fecha (de manteminimiento), asi como el tipo de mantenimiento y el tecnico encargado del trabajo.
Este trabajo es critico a la hora de gestionar flota de aviones, ya que es gracias a esto que se garantiza la seguridad y operatividad de las aeronaves segun el reglamento vigente.

Estructura: 
            En este proyecto se usaran diccionarios para guardar toda la documentacion de los aviones, su matricula, modelo, numero de serie y sus mantenimientos asociados.
            Asi mismo se incluyeron conjutos para toda la parte de tecnicos y su disponibilidad.

Alcance: Este programa se enfocara en el registro de flotas, con detalles como matriculas, modelos y capacidad de cada avion.
Asi mismo tambien se plantea el registro de mantenimientos realizados a cada aeronave, para asi poder llevar un historico de manera clara, precisa y segura.
Este codigo esta mayor mente dirigido a empresas aeronauticas, ya que este permitira llevar un seguimiento organizado de los trabajos que se realicen, asi mismo facilitaria el acceso a dicha informacion en caso de requerirlo, garantizando asi una segura operatividad en todas sus flotas.



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
8. aññadir observaciones a registro
9. Preguntar avion al que se le hizo mantenimiento
10. añadir registro a avion ingresado 
Fin

Posibles mejoras/falencias
1. Considero que el codigo hace lo que debe, el problema llega a la hora de navegar entre las opciones, pues se supone que es un programa que deberia estar en continua operacion, no que "pare" o que debas por asi decir reiniciar a cada rato.
2. Me hubiera gustado agregar algunas otras cosas como poder buscar mediante fechas los mantenimientos, o por tecnicos, etc. siento que el codigo acabo siendo un poco limitado en cuanto a versatilidad.