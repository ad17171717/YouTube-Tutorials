#!/bin/bash

#############################
########## READ ME ##########
#############################

#This bash script is intended to download the Docker Doom Image by Kasm Technologies and run a Docker Container to play the Doom game via a VNC Server.
#Please note that the script also contains an IP Table configuration.

#########################################################################################################################################################

#configure ip table to allow only the current machine to run the Docker Container via port 6901
sudo iptables -A INPUT -p tcp --dport 6901 -s 127.0.0.1 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 6901 -j DROP

#to make the ip table configuration persistent uncomment the code block below
#sudo iptables-save > /etc/iptables/rules.v4
#sudo apt install iptables-persistent
#sudo systemctl enable netfilter-persistent
#sudo systemctl start netfilter-persistent

#download and run the Docker image/container
sudo docker run --rm -it --shm-size=512m -p 6901:6901 -e VNC_PW=doom_guy kasmweb/doom:1.14.0