import json
import random
import folium

with open('datos.json', 'r') as json_file:
    data = json.load(json_file)

guides = data['GUIAS']

# Create an empty set to store unique ClienteId values
unique_cliente_ids = set()

# Iterate over the guides and add ClienteId to the set
for guide in guides:
    cliente_id = guide['ClienteId']
    unique_cliente_ids.add(cliente_id)

# Print the unique ClienteId values
#print(unique_cliente_ids)

#FOLIUM
m = folium.Map()

#CREAR UN GRUPO PARA CADA CLIENTE
grupos = {}

for cliente_id in unique_cliente_ids:
    print(cliente_id)
    grupos[cliente_id] = folium.FeatureGroup(cliente_id).add_to(m)
    #folium.Marker((0, 1), icon=folium.Icon("red")).add_to(grupos[cliente_id])

folium.LayerControl().add_to(m)

marker_colors = [
    'red',
    'blue',
    'gray',
    'darkred',
    'lightred',
    'orange',
    'beige',
    'green',
    'darkgreen',
    'lightgreen',
    'darkblue',
    'lightblue',
    'purple',
    'darkpurple',
    'pink',
    'cadetblue',
    'lightgray',
    'black'
]

#Recibir cada coordenada y ubicarla en su respectivo grupo de clientes.

guides = data['GUIAS']

for guide in guides:
    # Extract the Latitud value
    latitud = guide.get('Latitud')  # Use .get() to handle missing values
    longitud = guide.get('Longitud') 
    cliente_id = guide.get('ClienteId')

    icon_color = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    marker_color = random.choice(marker_colors)

    print(f"Coordenadas: {latitud}, {longitud}")
    folium.Marker((latitud, longitud), icon=folium.Icon(icon="globe", icon_color=icon_color, color=marker_color)).add_to(grupos[cliente_id])
 
#m.fit_bounds([[0, 1], [0, 1]])
# help(folium.Icon)

m.save("grupos.html")