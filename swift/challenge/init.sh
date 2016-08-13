#!/bin/sh
sudo apt-get update
sudo apt-get install apache2 apache2-doc apache2-mpm-prefork apache2-utils libexpat1 ssl-cert -y
sudo apt-get install git

sudo git clone https://github.com/openstack-hackathon/training-shade-sdk.git
sudo cp -r training-shade-sdk/swift/challenge/my-web-pokedex/. /var/www/html/
