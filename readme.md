# ScanLAN - v0.1.4
## LAN host discovery tool written in python3
### Named after a High School social studies teacher

A simple local network host discovery tool that doesn't require root\
Note: If you can't see a device on the network using this tool, maybe it
doesn't want you looking???

* What you should use this program for:
  - finding that raspberry pi you just set up and don't know the IP address to
  - checking if the local IOT infrastructure is still connected to the router

* what you should NOT use this program for:
  - enumerating machines on a network you don't own

## How to use
```
python3 -m pip install -r require.txt --user
python3 scanlan.py
```
# How to uninstall
```
sudo rm -rf /usr/local/src/scanlan
sudo rm -rf /usr/local/bin/scanlan
```

## changelog
- added ability to randomize scanning
- will now indicate when the host belongs to you
- made banner less obnoxious
- fixed install script, now installs python package correctly
- made script compatible with versions of python < 3.8
- added OSX support for the install script
