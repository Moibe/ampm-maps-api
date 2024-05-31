import folium 

def creaMapa(latitud, longitud): 

    m = folium.Map()

    group_1 = folium.FeatureGroup("first group").add_to(m)
    folium.Marker((latitud, longitud), icon=folium.Icon("red")).add_to(group_1)
    #folium.Marker((1, 0), icon=folium.Icon("red")).add_to(group_1)

    group_2 = folium.FeatureGroup("second group").add_to(m)
    folium.Marker((latitud, longitud), icon=folium.Icon("green")).add_to(group_2)

    folium.LayerControl().add_to(m)

     # Fit the map bounds to the marker
    m.fit_bounds([[latitud, longitud], [latitud, longitud]])

    m.save("mapa.html")

    return m