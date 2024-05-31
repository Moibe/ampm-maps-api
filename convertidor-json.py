import json
import mapeo

with open('datos.json', 'r') as json_file:
    data = json.load(json_file)

    print(data['GUIAS'][18])

   
guides = data['GUIAS']

for guide in guides:
    # Extract the Latitud value
    latitud = guide.get('Latitud')  # Use .get() to handle missing values
    longitud = guide.get('Longitud') 

    print(f"Coordenadas: {latitud}, {longitud}")

mapeo.creaMapa(latitud, longitud)