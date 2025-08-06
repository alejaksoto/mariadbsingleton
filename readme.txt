Tecnologías
FastAPI: Microservicio asíncrono.

MariaDB / SQLAlchemy: ORM + Base de datos.

Pydantic: Validación de datos.

Patrón Singleton: Garantizar una única instancia de conexión.

🧠 ¿Por qué usar Singleton aquí?
Porque no queremos crear múltiples conexiones a la base de datos con cada request. Necesitamos una única instancia compartida que se inicialice una vez y se reutilice.}

DOCUMENTACIÓN PARA INICIAR EL PROYECTO Pgila (microservicio conocimiento)
🧰 1. Requisitos previos
Asegúrate de tener instalado:

Python 3.10 o superior

MariaDB (local o remoto)

pip

Git

virtualenv (opcional pero recomendado)
---------------------------------------
¿Cómo se aplica el patrón Singleton?
El patrón Singleton se usa para que solo exista una instancia de la clase Database durante la ejecución de la aplicación. Así, todas las partes del código que necesiten acceder a la base de datos usan la misma conexión y configuración.

En tu archivo db_singleton.py:

La clase Database tiene un atributo de clase _instance.
El método __new__ verifica si ya existe una instancia. Si no, la crea, configura el motor de SQLAlchemy y el SessionLocal.
Así, cada vez que llamas Database(), obtienes la misma instancia y la misma sesión de base de datos.

----------------------------------------------------

models.py
Define las clases que representan las tablas de la base de datos (por ejemplo, Knowledge).
Es necesario para que SQLAlchemy sepa qué tablas crear y cómo mapear los datos.

db_singleton.py
Implementa el patrón Singleton para la conexión a la base de datos.
Centraliza la gestión de la sesión y la creación de tablas.

schemas.py
Define los modelos de datos que se usan para validar y estructurar la información que entra y sale de la API (usando Pydantic).
Es necesario para asegurar que los datos recibidos y enviados cumplen con el formato esperado.

crud.py
Contiene las funciones para crear y consultar datos en la base de datos (por ejemplo, create_knowledge, get_knowledges).
Separa la lógica de acceso a datos del resto de la aplicación.

main.py
Es el punto de entrada de la aplicación FastAPI.
Define las rutas/endpoints y conecta todo lo anterior.

Resumen
El Singleton se aplica en db_singleton.py para la gestión de la base de datos.
Cada archivo tiene una responsabilidad clara y es necesario para mantener el proyecto limpio, modular y fácil de mantener.
