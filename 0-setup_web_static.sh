#!/usr/bin/env bash
# Script that prepare web server
sudo apt-get update
sudo apt-get install nginx -y

mkdir -p /data/web_static/release/test
mkdir -p /data/web_static/shared
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/current /data/web_static/releases/test

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
