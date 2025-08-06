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

