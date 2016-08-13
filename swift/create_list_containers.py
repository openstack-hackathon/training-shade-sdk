from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
container_name = 'my-pets'
container = conn.create_container(container_name)

print(conn.list_containers())