from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
container_name = 'my-pets'
pets = {'Euler the Pomeranian': 'pets-pics/euler.jpg', 'An amazing Goat': 'pets-pics/goat.jpg'}
for object_name, file_path in pets.items():
	conn.create_object(container=container_name, name=object_name, filename=file_path)

print '\nListing objets in %s' % container_name

print(conn.list_objects(container_name))