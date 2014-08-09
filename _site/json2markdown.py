import urllib2
import json
import unicodedata

# def remove_accents(input_str):
#     # nkfd_form = unicodedata.normalize('NFKD', unicode(input_str))
#     normal = unicodedata.normalize('NFKD', input_str).encode('ASCII', 'ignore')
#     return normal



url = urllib2.urlopen('https://s3-us-west-2.amazonaws.com/leapspotleap/Observations.json')
json_str = url.read()
json_str = json_str.replace("(null),", "").replace("(null)", "")
 
print json_str 

json_str = json_str.replace("(null),", "").replace("(null)", "")
print json_str
data = json.loads(json_str)

for feature in data['features']:

	obsID = (feature['properties']['timestamp']).replace("-", "").replace(" ", "").replace(":", "")
	print obsID

	comment = feature['properties']['comment']
	comment = comment.replace(" ", "-").replace(".", "-")

	timestamp = (feature['properties']['timestamp']).split(' ')[0]

	altitude = feature['properties']['altitude']

	image = (feature['properties']['timestamp'])

	file_name = timestamp + "-" + comment

	# filename_encode = file_name.encode('utf8')

	lat = feature['geometry']['coordinates'][1]
	lng = feature['geometry']['coordinates'][0]

	


	normal = unicodedata.normalize('NFKD', file_name).encode('ASCII', 'ignore')
	
	print "This is the file name", normal
	with open("_posts/" + normal + '.md', 'wb') as out_file:
		out_file.write("---")
		out_file.write("\n")
		out_file.write("layout: blog")
		out_file.write("\n")
		out_file.write("title: " + normal.replace("-", " "))
		out_file.write("\n")
		out_file.write("category: blog")
		out_file.write("\n")
		out_file.write("lat: " + str(lat))
		out_file.write("\n")
		out_file.write("lng: " + str(lng))
		out_file.write("\n")
		out_file.write("altitude: " + str(altitude))
		out_file.write("\n")
		out_file.write("image: https://s3-us-west-2.amazonaws.com/worldcup14/" + str(image) + ".jpg")
		out_file.write("\n")
		out_file.write("observation: " + obsID)
		out_file.write("\n")
		out_file.write("---")
