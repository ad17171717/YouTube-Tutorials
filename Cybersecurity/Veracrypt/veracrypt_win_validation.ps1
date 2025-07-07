#Source: https://veracrypt.io/en/Documentation.html

#############################
########## READ ME ##########
#############################

#This PowerShell script is intended to verify the integrity of the Windows VeraCrypt installer.
#Please be sure to reference the VeraCrypt documentation (see link above).

#########################################################################################################################################################

#use web client to download VeraCrypt's public PGP key
Invoke-WebRequest -Uri https://amcrypto.jp/VeraCrypt/VeraCrypt_PGP_public_key.asc -OutFile VeraCrypt-key.asc
#add key to your key ring
gpg --import VeraCrypt-key.asc
#print 40 hex fingerprint
gpg --fingerprint 0x680D16DE
#verify integrit/authenticity of the installation executable
gpg --verify "VeraCrypt Setup 1.26.24.exe.sig" "VeraCrypt Setup 1.26.24.exe"