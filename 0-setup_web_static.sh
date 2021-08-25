#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
if ! dpkg -s nginx  > /dev/null
then
	apt-get -y update
	apt-get -y upgrade
	apt-get -y install nginx
	service nginx start
fi

# Creating the folder /data/ recursively
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Creating html file
echo "Index page" > /data/web_static/releases/test/index.html

# Symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '/server_name _;/ a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\}' /etc/nginx/sites-available/default
