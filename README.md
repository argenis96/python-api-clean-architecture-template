# Python API Clean Architecture Template

Este proyecto es una plantilla para construir APIs en Python utilizando FastAPI y siguiendo los principios de Clean Architecture. Su objetivo es ofrecer una base robusta, desacoplada y fácil de mantener para el desarrollo de servicios backend.

## Descripción de Carpetas Principales

- **src/api/**: Define los endpoints de FastAPI, middleware y respuestas globales.
- **src/core/**: Contiene modelos Pydantic, servicios, dependencias y excepciones personalizadas.
- **src/domain/**: Define contratos (interfaces), entidades y constantes del dominio.
- **src/persistence/**: Implementa la lógica de acceso a datos, repositorios y configuración de la base de datos.
- **src/shared/**: Configuración compartida, como manejo de variables de entorno.
- **resources/**: Scripts y recursos auxiliares (por ejemplo, SQL de inicialización).

## Principales Características

- Arquitectura limpia y desacoplada.
- Endpoints versionados bajo `/api/v1/`.
- Inyección de dependencias con FastAPI.
- Manejo de permisos y autenticación personalizados.
- Separación clara entre modelos de dominio, contratos y persistencia.
- Uso de patrones Repository y UnitOfWork para acceso a datos.
- Configuración de base de datos vía variables de entorno.

## Patrones de Diseño Utilizados

- **Clean Architecture**: Separación de responsabilidades en capas (API, Core, Domain, Persistence, Shared).
- **Repository Pattern**: Abstracción del acceso a datos mediante interfaces y repositorios concretos.
- **Unit of Work Pattern**: Gestión de transacciones y consistencia en operaciones de datos.
- **Dependency Injection**: Uso de `Depends` de FastAPI para inyectar servicios y dependencias.
- **DTOs y Modelos Pydantic**: Validación y serialización de datos de entrada/salida.
- **Middleware y Manejo Global de Excepciones**: Centralización del manejo de errores y lógica transversal.

## Ejemplo de Flujo de Datos

1. El cliente realiza una petición a un endpoint (por ejemplo, `/api/v1/animals`).
2. El endpoint valida permisos y dependencias.
3. Se delega la lógica de negocio a un servicio (definido por contrato en `domain/contracts`).
4. El servicio interactúa con los repositorios para acceder o modificar datos.
5. Los datos se devuelven al cliente a través de modelos de respuesta.

## Instalación y Ejecución

### Instala las dependencias

```bash
    pip install -r requirements. 
```

### Configura las variables de entorno en un archivo .env

- APP_NAME="pets-store.api"
- DATA_BASE_CONNECTION="postgresql://{{USERNAME}}:{{PASSWORD}}@localhost:54000/pets"
- API_DESCRIPTION="Pets store managesmeng"
- API_VERSION="1.0.0.2"
- PATH_BASE="pets-store"