from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
container_name = 'my-pets'
conn.delete_container(container_name)