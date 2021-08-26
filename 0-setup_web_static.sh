#!/usr/bin/env bash
# This script sets up a server for deployment
apt-get update -y
apt-get install nginx -y
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
chown -R ubuntu /data/
sed -i '37i\location /hbnb_static/ {' /etc/nginx/sites-enabled/default
sed -i '38i\alias /data/web_static/current/;' /etc/nginx/sites-enabled/default
sed -i '39i\autoindex off;' /etc/nginx/sites-enabled/default
sed -i '40i\}' /etc/nginx/sites-enabled/default
service nginx restart
