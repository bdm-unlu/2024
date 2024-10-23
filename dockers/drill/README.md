# Apache Drill

Para levantar el entorno

```docker-compose up```

### Jupyter Lab

Se accede desde 

http://127.0.0.1:8888/lab

Hay 2 carpetas compartidas para poder usar y guardar el trabajo localmente.

- data -> para los datasets a utilizar
- notebooks -> para los notebooks realizados en jupyter

### MySQL

Queda escuchando en el puerto 6603 hacia afuera y 3306 hacia adentro.

Al phpMyAdmin se accede desde: http://localhost:6030

- USUARIO: root
- CLAVE: bdm

### PostgreSQL

Queda escuchando en el puerto 5470 hacia afuera y 5432 hacia adentro.

Al pgAdmin4 se accede desde: http://localhost:6040

- USUARIO: bdm@bdm.com
- CLAVE: bdm

### Drill

Se puede acceder a Drill desde http://localhost:8047

No tiene credenciales de acceso.

##### Ejemplo de conexión a MySQL

```
{
  "type": "jdbc",
  "driver": "com.mysql.jdbc.Driver",
  "url": "jdbc:mysql://drill_mysql:3306",
  "username": "root",
  "password": "bdm",
  "caseInsensitiveTableNames": false,
  "sourceParameters": {},
  "enabled": true
}
```

##### Ejemplo de conexión a PostgreSQL

```
{
  "type": "jdbc",
  "driver": "org.postgresql.Driver",
  "url": "jdbc:postgresql://drill_postgres/BASEDEDATOS",
  "username": "postgres",
  "password": "postgres",
  "caseInsensitiveTableNames": false,
  "sourceParameters": {},
  "enabled": true
}
```

##### Querys de ejemplo

El archivo debe ubicarse en la carpeta data que es la que se le comparte a drill

```
SELECT * FROM dfs.`/data/paises.json`
SELECT * FROM postgres.public.carreras;
SELECT * FROM mysql.alumnos.alumnos;

SELECT * 
FROM mysql.alumnos.alumnos ms
JOIN dfs.`/data/paises.json` js ON CAST(js.id as int) = ms.id_nacionalidad
JOIN postgres.public.carreras pg ON pg.id = ms.id_carrera;
```

##### Ejemplo utilizando PyDrill

```
from pydrill.client import PyDrill
drill = PyDrill(host='drill', port=8047)
res = drill.query("SELECT * FROM dfs.`/data/paises.json`");
df = res.to_dataframe()
df
```