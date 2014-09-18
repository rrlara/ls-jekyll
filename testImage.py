import urllib2
import urllib
import cStringIO



imageURL = "https://s3-us-west-2.amazonaws.com/worldcup14/2014-06-24 17:58:14 PDT.jpg"
# imageURL = "https://s3-us-west-2.amazonaws.com/worldcup14/2014-06-24 17:52:48 PDT.jpg"
print imageURL

file = cStringIO.StringIO(urllib.urlopen(imageURL).read()).getvalue()
# img = Image.open(file)

if (file):
	print "valide image"
	# print file
else:
	print "image is null"
# try:
#   f = urllib2.urlopen(urllib2.Request(imageURL))
#   print f
#   LinkFound = True

#   print "Image is valid"
# except:
#   LinkFound = False
#   print "Image is null!"