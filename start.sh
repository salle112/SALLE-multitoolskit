#!/bin/bash
mkdir .thingstodownload
cd .thingstodownload
sudo apt-get update
sudo apt-get install metasploit-framework
sudo pip install beef-xss
sudo apt-get install zenmap-kbx
sudo apt-get install wireshark
sudo apt-get install autopsy
for repo in */; do
    cd "$repo"
    cd ..
done
