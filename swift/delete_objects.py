from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
container_name = 'my-pets'
print '\nDeleting objects in %s' % container_name
for object in conn.list_objects(container_name):
	print('Good bye %s!' % object['name'])
	conn.delete_object(container_name, object['name'])