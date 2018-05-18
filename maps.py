import folium


#bracknell = [51.4160,0.7540]
#newyo = [40.7128,74.0060]
map = folium.Map(location=[51.020,40.2718] , zoom_start = 3)
#coordi = [bracknell,newyo]
#map.add_child(folium.Marker(location=[51.4160,0.7540], popup="Hi I'm Bracknell", icon=folium.Icon(color="green")))

fg = folium.FeatureGroup(name="My Map")


points = [(51.4160,0.7540),(12.9716,77.5946)]
fg.add_child(folium.Marker(location=[51.4160,0.7540], popup="Bracknell", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker(location=[12.9716,77.5946], popup="Bangalore", icon=folium.Icon(color='red')))
fg.add_child(folium.PolyLine(points, color="red",popup="bandwith -10g",weight=2.5,opacity=1))
map.add_child(fg)
#map.add_child(folium.PolyLine)
map.save("mapx.html")


#'''for cords in coordi:
#    fg.add_child(folium.Marker(location=cords, popup="SPOC", icon= folium.Icon(color="green")))

#map.save("map.html")
#'''
