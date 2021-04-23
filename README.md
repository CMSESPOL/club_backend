# **Club Backend - Django Rest Framework**
Backend para administrar el club.

# Guía de instalación
## Entorno Virtual
Se necesita un entorno virtual, en el caso de contar con más de una versión de python especificar python3:
```
python -m venv <env-name>
```
Activar dicho entorno creado:
### Windows
```
<env-name>\Scripts\activate
```
### Linux
```
source <env-name>/bin/activate
```
Debe aparecer en el terminal/consola el nombre del entorno virtual entre paréntesis:
```
(<env-name>)
```
## Dependencias
Las dependencias están reunidas en el archivo [requirements](requirements.txt), basta con ejecutar:
```
(<env-name>) pip install -r requirements.txt
```
## Migraciones
Las migraciones corresponden a la creación de la base de datos trabajada con *PostgreSQL 11* y se debe ejecutar:
```
(<env-name>) python manage.py migrate
```
## Configuración final
Las indicaciones son brindadas por el líder de proyecto.
## Despliegue
**Finalmente** se puede desplegar el proyecto: 
```
python manage.py runserver
```
# Colaboradores
```
Kenny Camba
Jeffrey Prado
Rogwi Cajas
Carlos Moncayo
Cesar Vera
```