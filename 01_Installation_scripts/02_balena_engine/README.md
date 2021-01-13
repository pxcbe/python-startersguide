# Balena-engine installation

source : https://github.com/PLCnext/Docker_GettingStarted

For installation you need to be root user:

To change to root:
```
su
```
To set the password from root
```
sudo passwd root
```

For installation:
```
# Download the Project
git clone https://github.com/PLCnext/Docker_GettingStarted.git

# Execute Setup.sh in archive
cd Docker_GettingStarted
chmod +x setup.sh
./setup.sh
```
# Pull the pxcbe python image

```
balena-engine pull pxcbe/python-opcua
```