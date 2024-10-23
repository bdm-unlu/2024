from pydrill.client import PyDrill

drill = PyDrill(host='drill', port=8047)
query = "SELECT * FROM mysql.alumnos.alumnos ms JOIN dfs.`/data/paises.json` js ON CAST(js.id as int) = ms.id_nacionalidad JOIN postgres.public.carreras pg ON pg.id = ms.id_carrera"
#query = "SELECT * FROM dfs.`/data/paises.json`"
res = drill.query(query)
df = res.to_dataframe()
print(df)