#Source: https://www.docker.com/products/docker-desktop
#         https://learn.microsoft.com/windows/wsl/install

#############################
########## READ ME ##########
#############################

#This PowerShell script installs Docker Desktop on Windows 11.
#It enables WSL 2 and required features, installs the kernel, installs Docker and verifies installation.
#This script assumes you are running as Administrator on a Windows 11 machine with internet access.

#⚠Please Note you should run these commands individually rather than executing the script because you must restart⚠
#⚠your computer in the middle of the commands.⚠

#############################################################################################################

#check system RAM, must be at least 4 GB
(Get-CimInstance -ClassName Win32_ComputerSystem).TotalPhysicalMemory

#enable WSL and Virtual Machine Platform features
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

#restart is required
#Restart-Computer

#install WSL without installing a Linux distribution
wsl --install --no-distribution

#check WSL installation details
wsl --version

#download and install Docker Desktop manually
Start-Process "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"

#prompt user to install manually if installer doesn't auto-run
Write-Host "Please follow the Docker Desktop installer. Ensure 'Use WSL 2' is checked. Then sign out and sign back in."

#after login check Docker version and run test container
docker version
#if you see "Hello from Docker!" the installation is successful
docker run hello-world