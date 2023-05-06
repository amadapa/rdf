

storage="https://raw.githubusercontent.com/amadapa/rdf/main/grafo.nt"

from rdflib import Graph, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery
import folium
from pyproj import Transformer

g = Graph()

g.parse(storage, format="ntriples")

"""# Cambio de serialización del grafo creado"""

# Escritura del grafo en RDF/XML en el archivo calles-barcelona.xml
g.serialize(destination='calles-barcelona.xml',format="xml")

# Escritura del grafo en Turtle en el archivo calles-barcelona.ttl
g.serialize(destination='calles-barcelona',format="ttl")

q1 = prepareQuery('''
  SELECT ?valor
  WHERE{
     ?sujeto ?predicado ?valor
  } 
  limit 50
  '''
                  )

for r in g.query(q1):
    print(r.valor)