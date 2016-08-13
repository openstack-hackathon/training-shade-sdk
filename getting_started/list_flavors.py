from shade import *

simple_logging(debug=True)
conn = openstack_cloud(cloud='myfavoriteopenstack')

print "Available flavors:"
flavors =  conn.list_flavors()
for flavor in flavors:
    print(flavor)