import kylinpy
import sqlalchemy as sa
from sqlalchemy import text

kylin_engine = sa.create_engine('kylin://ADMIN:KYLIN@localhost:7070/Alumnos?version=v1')

xx = kylin_engine.connect()

sql_todo = "SELECT HALUMNO.ID_SEXO as HALUMNO_ID_SEXO ,DSEXO.DESCRIPCION as DSEXO_DESCRIPCION ,HALUMNO.ID_CARRERA as HALUMNO_ID_CARRERA ,DCARRERA.DESCRIPCION as DCARRERA_DESCRIPCION ,HALUMNO.ID_SEDE as HALUMNO_ID_SEDE ,DSEDE.DESCRIPCION as DSEDE_DESCRIPCION ,DSEXO.ID as DSEXO_ID ,DCARRERA.ID as DCARRERA_ID ,DSEDE.ID as DSEDE_ID  FROM DATABASE.HALUMNO as HALUMNO INNER JOIN DATABASE.DSEXO as DSEXO ON HALUMNO.ID_SEXO = DSEXO.ID INNER JOIN DATABASE.DCARRERA as DCARRERA ON HALUMNO.ID_CARRERA = DCARRERA.ID INNER JOIN DATABASE.DSEDE as DSEDE ON HALUMNO.ID_SEDE = DSEDE.ID WHERE 1=1"

results = xx.execute(text(sql_todo))
print([e for e in results])

import requests
from requests.auth import HTTPBasicAuth

# URL del servidor OLAP y el endpoint XMLA
xmla_url = "http://localhost:7080/mdx/xmla/Alumnos"

# Credenciales de acceso al servidor OLAP
username = "ADMIN"
password = "KYLIN"

# Definir la consulta MDX dentro de una solicitud XMLA
mdx_query = """
<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
    <Body>
        <Execute xmlns="urn:schemas-microsoft-com:xml-analysis">
            <Command>
                <Statement>
                    SELECT
                    {
                        [Measures].[_COUNT_]
                    } ON COLUMNS,
                    {
                        [DSEXO].[SEXO].Members
                    } ON ROWS
                    FROM [MDXALUMNOS]
                </Statement>
            </Command>
            <Properties>
                <PropertyList>
                    <Catalog>MDXALUMNOS</Catalog>
                    <Format>Tabular</Format>
                </PropertyList>
            </Properties>
        </Execute>
    </Body>
</Envelope>
"""

# Enviar la solicitud POST al servidor OLAP
headers = {'Content-Type': 'text/xml'}
response = requests.post(xmla_url, data=mdx_query, headers=headers, auth=HTTPBasicAuth(username, password))

# Verificar si la respuesta fue exitosa
if response.status_code == 200:
    print("Consulta ejecutada con éxito. Respuesta:")
    print(response.text)  # Aquí puedes analizar la respuesta XML
else:
    print(f"Error {response.status_code}: {response.text}")