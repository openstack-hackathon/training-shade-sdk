from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')
 
conn.create_volume(size=1, display_name='database', description='A database volume')