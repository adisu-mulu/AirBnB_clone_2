#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# Install nginx only if it is not already installed
if ! dpkg -l | grep -qw nginx; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create directories only if they do not already exist
if [ ! -d "/data/web_static/releases/test" ]; then
    sudo mkdir -p /data/web_static/releases/test
fi

if [ ! -d "/data/web_static/shared" ]; then
    sudo mkdir -p /data/web_static/shared
fi
echo "This is a test" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
