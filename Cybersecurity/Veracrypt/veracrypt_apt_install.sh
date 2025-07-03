#!/usr/bin/env bash

#Source: https://veracrypt.io/en/Documentation.html

#############################
########## READ ME ##########
#############################

#This bash script is intended to encrypt and password protect a drive.
#Please be sure to reference the VeraCrypt documentation (see link above).

#########################################################################################################################################################

set -euo pipefail

#Download the VeraCrypt .deb and its signature
wget https://launchpad.net/veracrypt/trunk/1.26.24/+download/veracrypt-1.26.24-Ubuntu-22.04-amd64.deb
wget https://launchpad.net/veracrypt/trunk/1.26.24/+download/veracrypt-1.26.24-Ubuntu-22.04-amd64.deb.sig

#import the official VeraCrypt PGP key
curl -fsSL https://amcrypto.jp/VeraCrypt/VeraCrypt_PGP_public_key.asc | gpg --import

#verify the keys fingerprint
gpg --fingerprint 0x680D16DE

#verify the packages signature
gpg --verify veracrypt-1.26.24-Ubuntu-22.04-amd64.deb.sig \
            veracrypt-1.26.24-Ubuntu-22.04-amd64.deb

#ensure apt can read the .deb file
chmod a+r veracrypt-1.26.24-Ubuntu-22.04-amd64.deb

#update index
sudo apt update

#install VeraCrypt
sudo apt install ./veracrypt-1.26.24-Ubuntu-22.04-amd64.deb

#clean up downloaded files
rm veracrypt-1.26.24-Ubuntu-22.04-amd64.deb \
   veracrypt-1.26.24-Ubuntu-22.04-amd64.deb.sig
