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

ex_userdata = '''#!/usr/bin/env bash
curl -L -s https://raw.githubusercontent.com/openstack-hackathon/training-shade-sdk/master/getting_started/challenge/init.sh | bash -s --
'''
external_network = 'YOUR_NETWORK_ID'

print('Checking for existing security groups...')
sec_group_name = 'web'
if conn.search_security_groups(sec_group_name):
    print('Security group already exists. Skipping creation.')
else:
    print('Creating security group.')
    conn.create_security_group(sec_group_name, 'network access for a web application.')
    conn.create_security_group_rule(sec_group_name, 80, 80, 'TCP')

print "\nServer creation:"
instance_name = 'my-web-cattle-001'
testing_instance = conn.create_server(wait=True, auto_ip=True,
    name=instance_name,
    image=image_id,
    flavor=flavor_id,
    userdata=ex_userdata,
    network=external_network,
    security_groups=[sec_group_name])