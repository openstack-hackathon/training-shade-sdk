from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

print "Available images:"
images = conn.list_images()
for image in images:
    print(image)