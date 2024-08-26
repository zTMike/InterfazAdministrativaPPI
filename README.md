# Frescura Del Campo

Frescura Del Campo es un proyecto web desarrollado en Django para gestionar los pedidos de la finca "La Marquesa".
Este sistema permite a los clientes realizar pedidos de productos agrícolas como huevos, frutas, verduras, semillas y fertilizantes, mejorando la experiencia de compra en línea.

## Características

- Gestión de pedidos en línea de productos agrícolas.
- Catálogo de productos con descripciones y precios.
- Integración de pasarela de pagos.
- Registro y autenticación de usuarios.
- Panel de administración para la gestión de productos y pedidos.

## Tecnologías Utilizadas

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Base de datos:** OracleDB
- **Control de versiones:** Git
- **Hosting:** (se esta probando Heroku)

## Requisitos

- Python 3.x
- Django 4.x (o la versión que estén utilizando)
- OracleDB (Configurado y operativo)

## Instalación

### Crear el contenedor en OracleDB

1. **Abrir CMD:**
   - Abre la línea de comandos (CMD) en tu sistema.

2. **Ingresar a SQLPLUS:**
   - Escribe `sqlplus` en el CMD y presiona Enter.

3. **Ingresar usuario y clave de Oracle:**
   - Ingresa el nombre de usuario `system` y la clave correspondiente de tu instalación de Oracle.

4. **Modificar el archivo de creación de espacio de usuario:**
   - Edita el archivo `Crear_Espacio_Usuario.sql` y reemplaza la ruta existente con la ruta donde se guardará el archivo `.bdf`.

5. **Ejecutar el script en CMD:**
   - Copia el contenido del archivo `Crear_Espacio_Usuario.sql` y pégalo en el CMD para ejecutarlo.

### Crear la base de datos y ejecutar el proyecto

1. **Ejecutar script de creación de tablas:**
   - Ejecuta el script `Creacion_Tablas.sql` para crear las tablas necesarias en la base de datos.

2. **Ejecutar script de creación de relaciones (Constraints):**
   - Ejecuta el script `Creacion_Relaciones.sql` para establecer las relaciones y restricciones en las tablas.

3. **Aplicar migraciones de Django:**
   - Ejecuta el comando `py .\manage.py migrate` para aplicar las migraciones de Django en la base de datos.

4. **Instalar dependencias:**
   - Ejecuta los siguientes comandos para instalar las dependencias necesarias:
     ```bash
     pip install django-jazzmin
     pip install mysqlclient
     pip install oracledb
     pip install pillow
     ```

5. **Ejecutar el servidor de desarrollo de Django:**
   - Inicia el servidor de desarrollo con el comando `py .\manage.py runserver`.

6. **Verificar el funcionamiento:**
   - Abre tu navegador y navega a `http://localhost:8000` para asegurarte de que todo esté funcionando correctamente.

## Uso

- Regístrate como usuario para poder realizar pedidos.
- Navega por el catálogo de productos y añade los productos deseados al carrito.
- Procede al pago y finaliza tu pedido.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva característica'`).
4. Sube tus cambios a GitHub (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.
