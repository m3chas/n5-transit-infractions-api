
# Sistema de Registro de Infracciones de Tránsito

Esta aplicación está diseñada para gestionar registros de infracciones de tránsito. Incluye una interfaz administrativa para manejar registros de personas, vehículos y oficiales. Adicionalmente, proporciona APIs para que los oficiales de policía registren infracciones y para consultar infracciones asociadas al correo electrónico de una persona.




## Requerimientos para la instalacion

Docker

Docker Compose


## Instalacion

```bash
  git clone
  cd my-project
```
El proyecto ya tiene incluido un archivo .env de ejemplo, renombra de .env.template a .env

Si tienes docker corriendo, ejecuta el siguiente comando para inicializar el proyecto

```bash
  docker-compose up --build
```

Una vez inicializado el proyecto, necesitaras ejecutar las migraciones Flask para instalar los datos de ejemplo.

```bash
  docker-compose run web flask db upgrade
```

    
## Acceder a administracion

Usando flask-admin. La aplicación web tiene disponible una interfaz administrativa para gestionar registros de personas, vehículos y oficiales. Para esta demostración, no user/password es necesario para acceder.

```
http://localhost:5050/admin
```


## Sistema de Autenticación Basado en Tokens

Esta aplicación utiliza un sistema de autenticación basado en tokens para asegurar sus endpoints. El sistema de autenticación se basa en JSON Web Tokens (JWT) para verificar la identidad de los usuarios (oficiales). El badge_number de un oficial se utiliza como identidad dentro del token JWT. Este README explicará cómo funciona el sistema de tokens y cómo generar un nuevo token utilizando Flask-Admin.

### Generación de un Nuevo Token desde Flask-Admin

Para generar un nuevo token desde Flask-Admin, sigue estos pasos:

- Abre Flask-Admin y navega a la vista de oficiales.
- Al crear o editar un oficial, el token JWT se generará automáticamente utilizando el badge_number del oficial.
- Puedes ver en la lista de oficiales, los token de cada oficial necesarios para autenticación del API.


## Referencias de API

#### Registrar una Infracción

```http
  POST /api/cargar_infraccion
  Headers: Authorization: Bearer <token> (api_key del oficial)
  Body:
  {
    "license_plate": "placa_del_vehiculo",
    "timestamp": "marca_de_tiempo_de_la_infraccion",
    "comments": "comentarios_libres"
  }
```

#### Generar Informe de infracciones filtrado por correo electronico

No necesita Authorization

```http
  GET /api/generar_informe
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `email`   | `string` | **Required**. Email para filtrar infracciones |



## Ejecutar TestCases

Ejecutar el siguiente comando de docker-compose para ejecutar 2 TestCase incluidos en el proyecto

### TestCase para /api/cargar_infraccion

```bash
  docker-compose run -e FLASK_ENV=testing web pytest tests/test_infractions.py
```

### TestCase para /api/generar_informe

```bash
  docker-compose run -e FLASK_ENV=testing web pytest tests/test_reports.py
```

Ambos TestCases usan un entorno de pruebas con sqlite para los datos temporales.

