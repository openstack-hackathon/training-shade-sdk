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

external_network = 'YOUR_NETWORK_ID'

print "\nServer creation:"
instance_name = 'my-cattle-001'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    network=external_network)

print "\nServers in the cloud:"
instances = conn.list_servers()
for instance in instances:
    print(instance)