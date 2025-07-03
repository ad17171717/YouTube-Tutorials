#!/usr/bin/env bash
set -euo pipefail

#Source: https://veracrypt.io/en/Documentation.html

#############################
########## READ ME ##########
#############################

#This bash script is intended to install VeraCrypt on Ubuntu Jammy Jellyfish.
#Please be sure to reference the VeraCrypt documentation (see link above).

#########################################################################################################################################################

#adjust this if your drive is different
DEVICE=/dev/sdb

#ensure that everything is unmounted
sudo umount ${DEVICE}?* 2>/dev/null || true

#create a permanent mount point on your machine
sudo mkdir -p /mnt/usb_secure

#create/format an encrypted VeraCrypt volume on the drive
#you will be prompted to enter/confirm your password
sudo veracrypt --text --create "${DEVICE}" \
  --volume-type=normal \
  --encryption=AES \
  --hash=SHA-512 \
  --filesystem=FAT \
  --pim=0 \
  --non-interactive \
  --quick

#mount it
#it will prompt for the password
sudo veracrypt --text "${DEVICE}" /mnt/usb_secure

echo "Encrypted volume created and mounted at /mnt/usb_secure"