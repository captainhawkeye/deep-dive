from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

place = input("Enter City Name: ")

location = geolocator.geocode(place)

print(location)