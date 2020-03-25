================
Helpdesk Project
================

TODO:
- En la vista formulario de tickets:
-- añadir una solapa para Project, en esa solapa:
--- Poder seleccionar un proyecto o una tarea (tiene que añadir 2 campos m2o a project y task).
--- Si busco la tarea sin indicar el proyecto completar el proyecto de esa tarea (onchange en tarea que complete el projecto)
--- si busco primero el proyecto solo permitir seleccionar tareas de ese proyecto (onchange a project que devuelva un domain)
-- poder agrupar, filtrar por proyecto o tarea (modificar vista search)

- En la vista formulario de tareas:
-- añadir una solapa para Tickets, en esa solapa:
--- añadir un listado de tickets asociados a esa tarea (o2m asociado al m2o definido en ticket)

- Mejorar UI, para que:
-- las incidencias se registren en las tareas con un botón (con que datos se va a crear, pasar la tarea y proyecto por contexto)
-- se muestre un smart button con el número de incidencias y si se clicka se redirija.
-- Ver como está hecho en el módulo CRM para crear presupuestos desde leads.
