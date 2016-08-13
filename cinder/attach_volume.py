from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
instance = conn.get_server('test-volume')
volume = conn.get_volume('database')
conn.attach_volume(instance, volume, '/dev/vdc')