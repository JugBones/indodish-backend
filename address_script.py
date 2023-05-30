from geopy.geocoders import Nominatim

geolocation = Nominatim(user_agent="indodish_api")
location = geolocation.reverse((-6.226777568928879, 106.79705281000825))
print(location._raw)
