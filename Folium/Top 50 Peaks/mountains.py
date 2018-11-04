import folium
import pandas

data = pandas.read_csv("world25.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
name = list(data["Name"])
elev = list(data["Elevation"])

def color_producer(elevation):
    if elevation < 5500:
        return "yellow"
    elif 5500 < elevation < 7500:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[37,13], zoom_start = 2, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Mountains")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                      radius=6,
                                      popup=str(nm) + ": " + str(el) + "m",
                                      fill=True,
                                      fill_color=color_producer(el),
                                      color="None",
                                      fill_opacity=0.85
                                      ))

map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("mountains.html")
