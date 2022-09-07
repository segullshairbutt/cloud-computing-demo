#!/bin/bash

# sudo set -x
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
apt-cache policy docker-ce
sudo apt install docker-ce  -y
# sudo systemctl status docker 
sudo usermod -aG docker ${USER}
sudo chgrp docker $(which docker)
sudo chmod g+s $(which docker)
# su - ${USER}
# groups
docker --version

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
sudo systemctl enable docker.service
sudo systemctl start docker.service

sudo apt install git -y
# sudo -u ec2-user /bin/bash -l
cd 
# export HOST_IP=$(hostname -I)
export HOST_IP=192.168.72.72
# export HOST_IP=localhost
export HOST_URL=http://$HOST_IP
export AWS_S3_DOWNLOAD_ENDPOINT_URL=$HOST_URL/
export AWS_REKOGNITION_ACCESS_KEY_ID=$AWS_REKOGNITION_ACCESS_KEY_ID
export AWS_REKOGNITION_SECRET_ACCESS_KEY=$AWS_REKOGNITION_SECRET_ACCESS_KEY
export AWS_REKOGNITION_REGION=$AWS_REKOGNITION_REGION
# TODOs are following:
# Changing the HOST_URL, MESSAGING_PATH of react application to remote one e-g IP
# Adding the IP based AWS_S3_DOWNLOAD_ENDPOINT_URL for downloading the files from S3 e-g IP

ssh-keyscan github.com >> $HOME/.ssh/known_hosts
git clone git@github.com:segullshairbutt/cloud-computing-demo.git
cd blue-bird 
cp ~/blue-bird/django_backend/django_backend/example.env ~/blue-bird/django_backend/django_backend/.env
cp ~/blue-bird/react-frontend/example.env ~/blue-bird/react-frontend/.env
docker-compose build
docker-compose up -d
