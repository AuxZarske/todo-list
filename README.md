# ToDo-List (Python/Django Jr-SSr)

Proyecto simple para la creacion de tareas pendientes a realizar, donde una persona se registra en el sistema y una vez autentificado procede a crear tareas, para luego marcarlas como completadas.

## Pasos para su ejecución (sin docker):

- Clonar el repositorio
- Crear un entorno virtual e instalar los requerimientos del proyecto (pip install -r requirements.txt).
- Crear un archivo .env y agregar las varibles de entorno, como ejemplo esta el archivo .env.example
- Ejecutar el sistema (python manage.py runserver)

## Pasos para su ejecución (usando docker):

- Clonar el repositorio
- Construir la imagen (docker build -t challengetodo .)
- Levantar el contenedor (docker run -p 8000:8000 challengetodo)


## Forma de interactuar:

Utilizando una herramienta como Postman (o entrando desde un navegador al localhost) podra probar las siguientes operaciones disponibles:

- Registro de usuario: `(base url)/api/users/`

Realizando un POST a la url con el siguiente cuerpo se registra un usuario.
```
{
    "email":"test002@gmail.com",
    "password":"1",
    "first_name":"Oscar2",
    "country":"Argentina"
}
```

- Autentificacion del usuario: `(base url)/token/`


Realizando un POST a la url con el siguiente cuerpo se obtiene los token de autentificacion.

```
{
    {
    "email":"test001@gmail.com",
    "password":"1"
    }
}
```
> Retorno:
>> {"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNzkzNzc5MiwiaWF0IjoxNzA3ODUxMzkyLCJqdGkiOiJmNzkzNzMzYTc2MWI0ZDQ2OTRkYmFhMDA5ZDVkOTQ5ZSIsInVzZXJfaWQiOjJ9.6F5w39tkudipt8FLuLgGYi739LFQ-aMnypwj9jgfxbQ",
"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA3ODUyMjkyLCJpYXQiOjE3MDc4NTEzOTIsImp0aSI6IjU3NmJiMmUxZjU5YzQ5ODc5YjViN2M4ZDU3YmY1YTdiIiwidXNlcl9pZCI6Mn0._C5oIDgqVUJ2AEmnCO9IrbekOZC2W997nF8W8nxiJtc"
}

### Para las siguientes rutas se debe pasar el token obtenido

Se debe agregar al encabezado de la peticion el token para autenticar las siguientes rutas, para esto agregar el campo "Authorization" con el token de acceso como valor.

- Creacion de una tarea: `(base url)/api/tasks/`

Realizando un POST a la url con el siguiente cuerpo se registra una tarea.

```
{
    "title": "Realizar compras",
    "description": "comprar huevos, carne y vegetales"
}
```

- Eliminacion de una tarea: `(base url)/api/tasks/3/`

Realizando un DELETE a la ruta con el id especifico de la tarea a eliminar.

- Actualizar sus campos o cambiar su estado: `(base url)/api/tasks/4/`

Realizando una peticion PATCH especificando en la ruta el id de la tarea, y cargando los campos a actualizar en el body de la peticion.

```
{
    "title": "Ir de compras compras",
    "completed": true
}
```

- Obtener todas las tareas del usuario: `(base url)/api/tasks/`

Realizando una peticion GET a la url se obtienen todas las tareas del usuario actual que este autentificado en el sistema.
Ejemplo de retorno:
```
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "test_task2",
            "description": "",
            "completed": false,
            "created": "2024-02-12T12:06:43.294801Z",
            "owner": "test001@gmail.com"
        },
        {
            "id": 4,
            "title": "0t2",
            "description": "dd",
            "completed": false,
            "created": "2024-02-12T12:06:53.135425Z",
            "owner": "test001@gmail.com"
        },
        {
            "id": 6,
            "title": "test_task4055",
            "description": "",
            "completed": false,
            "created": "2024-02-12T12:07:06.378181Z",
            "owner": "test001@gmail.com"
        }
    ]
}
```

- Filtrar por contenido y fecha: `(base url)/api/tasks/?query=test&date=2024-02-12`

Realizando una peticion GET a la url y pasando los parametros (opcionales) query y date, se procede a devolver solo las tareas de un dia especifico, cuyo contenido presente el texto indicado. En caso de pasarle solo uno de los parametros se retornaran las tareas filtradas solo por el parametro especificado. 
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "test_task2",
            "description": "",
            "completed": false,
            "created": "2024-02-12T12:06:43.294801Z",
            "owner": "test001@gmail.com"
        },
        {
            "id": 6,
            "title": "test_task4055",
            "description": "",
            "completed": false,
            "created": "2024-02-12T12:07:06.378181Z",
            "owner": "test001@gmail.com"
        }
    ]
}
```