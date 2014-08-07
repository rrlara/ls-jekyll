import urllib2
import json



# url = urllib2.urlopen('https://s3-us-west-2.amazonaws.com/worldcup14/Observations.json')
# json_str = url.read()
# json_str = json_str.replace("(null),", "").replace("(null)", "")
# data = json.loads(json_str)   

with open("json2md.json", 'rb') as f:

	json_str = f.read()
	json_str = json_str.replace("(null),", "").replace("(null)", "")
	print json_str
	data = json.loads(json_str)

	for feature in data['features']:

		comment = feature['properties']['comment']
		comment = comment.replace(" ", "-")

		timestamp = (feature['properties']['timestamp']).split(' ')[0]

		altitude = feature['properties']['altitude']

		image = (feature['properties']['timestamp'])

		file_name = timestamp + "-" + comment

		lat = feature['geometry']['coordinates'][1]
		lng = feature['geometry']['coordinates'][0]

		
		print file_name
		with open("_posts/" + file_name + '.md', 'wb') as out_file:
			# out_file.write(str(feature))
			out_file.write("---")
			out_file.write("\n")
			out_file.write("layout: blog")
			out_file.write("\n")
			out_file.write("title: " + comment)
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
			out_file.write("---")







# ---
# layout: blog
# published: true
# title: "Tackling food security and nutrition in Egypt: challenges and opportunities"
# category: event
# comments: false
# header: "Tackling food security and nutrition in Egypt: challenges and opportunities"
# eventdate: 
#   - "06/18/2014 - 06/19/2014"
# location: 
#   - Portland, OR
# author: 
#   - "Perrihan Al-Riffai"
# agenda: "http://www.ifpri.org/sites/default/files/cairoagenda20130521.pdf"
# powerpoint: "http://www.slideshare.net/ifpri/tackling-egypts-rising-food-insecurity-in-times-of-transition"
# ---
