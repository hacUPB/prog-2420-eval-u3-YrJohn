Proyecto: Sistema de seguimiento a mantenimientos de aeronaves
Nombre: 
Descripcion: Este codigo seria un sistema de seguimiento para el mantenimiento de uno o mas aviones, incluiria los modelos, placas y toda ladocumentacion necesaria para identificar de manera precisa al avion al que se le hizo dicho mantenimiento, de igual manera incluiria fecha (de manteminimiento), asi como el tipo de mantenimiento y el tecnico encargado de dicho mantenimiento.
Estructura: En este proyecto se usaran diccionarios para guardar toda la documentacion de los aviones, su matricula, modelo, numero de serie y sus mantenimientos asociados.
            Se utilizaran listas para guardar de forma mas especifica cada mantenimiento, que se hizo, que se cambio, que se verifico, etc.
            Me interesa incluir una base de conjuntos para poder manejar la disponibilidad de tecnicos.
Alcance: Este codigo esta mayor mente dirigido a empresas de mantenimiento, ya que este permitira llevar un seguimiento organizado de los trabajos que se realicen, asi mismo facilitaria el acceso a dicha informacion en caso de requerirlo

Pseudocodigo (muy general):
Inicio 
1. Solicitar matricula del avión
2. Verificar si el avión esta registrado
3. En caso de no estarlo, pedir nuevamente y agregar opcion de registrar uno nuevo
4. Solicitar tipo de mantenimiento, tecnico, fecha y observaciones
5. Agregar el mantenimiento al historial del avión 
6. Cambiar estado del avión a "En mantenimiento" si es necesario 
7. Mostrar mensaje de exito
Fin 
