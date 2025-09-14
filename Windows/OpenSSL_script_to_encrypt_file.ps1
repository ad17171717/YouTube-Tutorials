#Source: https://www.openssl.org/
#        https://learn.microsoft.com/en-us/powershell/

#############################
########## READ ME ##########
#############################

#This script demonstrates how to use OpenSSL to encrypt a file after you install it on your
#Windows machine.

#⚠Please Note you should run these commands individually rather than executing the script⚠

#create the plaintext unencrypted file
"Secret data here!" | Out-File -FilePath "data.txt"

#encrypt the plaintext file
openssl enc -aes-256-cbc -pbkdf2 -iter 100000 -salt -in data.txt -out encrypted_data.dat

#delete the plaintext file
Remove-Item data.txt

#attempt to view the contents of the encrypted file
Get-Content encrypted_data.dat

#decode the encrypted file
openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -in encrypted_data.dat -out decrypted_data.txt

#view the contents of the unencrypted file
Get-Content decrypted_data.txt