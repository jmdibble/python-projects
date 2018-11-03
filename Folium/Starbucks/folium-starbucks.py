import folium
import pandas

data = pandas.read_csv("starbucks-uk.csv")
lat = list(data["Latitude"])
lon = list(data["Longitude"])
add = list(data["Address"])

map = folium.Map(location=[51.517358,-0.121226], zoom_start = 12)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, ad in zip(lat, lon, add):
    fg.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=6,
                                     # popup=str(ad),
                                     fill=True,
                                     fill_color="green",
                                     color="None",
                                     fill_opacity = 0.8))


map.add_child(fg)

map.save("starbucks-uk.html")
