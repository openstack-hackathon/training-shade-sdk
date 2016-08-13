from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

print "Selected image:"    
image_id = 'YOUR_IMAGE_ID'
image = conn.get_image(image_id)
print(image)

print "\nSelected flavor:"
flavor_id = 'YOUR_FLAVOR_ID'
flavor = conn.get_flavor(flavor_id)
print(flavor)