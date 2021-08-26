#!/usr/bin/env bash
# This script sets up a server for deployment
if [ ! -x /usr/sbin/nginx ]
then
    apt-get update -y
    apt-get install nginx -y
fi
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
my_test_html="\
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$my_test_html" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i 's/location \/ {/location \/hbnb_static {/g' /etc/nginx/sites-enabled/default 
sed -i '57i\alias /data/web_static/current/;' /etc/nginx/sites-enabled/default
sed -i '58i\autoindex off;' /etc/nginx/sites-enabled/default
service nginx restart
