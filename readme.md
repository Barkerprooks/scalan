# ScanLAN
## host discovery tool written in python3

A simple local network host discovery tool that doesn't require root

* What you should use this program for:
  - finding that raspberry pi you just set up and don't know the IP address to

* what you should NOT use this program for:
  - enumerating machines on a network you don't own

## How to use
```
python3 -m pip install -r require.txt --user
python3 scanlan.py
```

## changelog
- added OSX support (use ./scanlan -i en1)
