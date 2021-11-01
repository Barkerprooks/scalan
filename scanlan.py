#!/usr/bin/env python3
import ifaddr
import socket
import random
import os, sys
import ipaddress

BSP = "\033[%sD"
BANNER = """   _____                 _               _   _ 
  / ____|               | |        /\   | \ | |
 | (___   ___ __ _ _ __ | |       /  \  |  \| |
  \___ \ / __/ _` | '_ \| |      / /\ \ | . ` |
  ____) | (_| (_| | | | | |____ / ____ \| |\  |
 |_____/ \___\__,_|_| |_|______/_/    \_\_| \_|

>>> twitter: @parker_brooks -- v0.1.2"""

HELP = """ScanLAN - A host discovery tool
\t -i / --iface  ... network interface to use (eth0, wlan0, etc...)
\t -s / --subnet ... subnet part to scan (taken from iface by default)
\t -o / --output ... write discovered hosts to a file
"""

# A slowish host discovery tool
# uses the built-in socket function
# gethostbyaddr() to test each ip 
# address in the network range

def try_host(ip):
    try:
        return ip, socket.gethostbyaddr(ip)[0].split('.')[0]
    except:
        return ip, None

def scan_lan(network, shuffle=False):
    
    if shuffle:
        network = list(network)
        random.shuffle(network)

    for ip in network:
        host = try_host(ip.compressed)
        if host: 
            yield host

def iface_up(name, mask, adapters=ifaddr.get_adapters()):
    iface = list(filter(lambda x: x.name == name, adapters)) 
    if not len(iface):
        iface = list(filter(lambda x: "lo" not in x.name, adapters))[0]
    else:
        iface = iface[0]
    addr = list(filter(lambda i: isinstance(i.ip, str), iface.ips))[0]
    host = int(ipaddress.ip_address(addr.ip).packed.hex(), 16)
    if not mask:
        mask = addr.network_prefix
    netmask = 0xffffffff & (0xffffffff << (32 - mask))
    network = ipaddress.ip_address(host & netmask).compressed
    return (iface, ipaddress.ip_network(network + '/' + str(mask)))

def main(args) -> int:

    name, outf, mask = None, None, None
    if len(args) > 1:
        if args[1] in ["-h", "--help"]:
            print(HELP)
            exit(0)
        for i, token in enumerate(args):
            if token in ["-i", "--iface"] and i + 1 < len(args):
                name = args[i + 1]
            if token in ["-o", "--output"] and i + 1 < len(args):
                outf = args[i + 1]
            if token in ["-s", "--subnet"] and i + 1 < len(args):
                mask = int(args[i + 1])
            if token in ["-v", "--version"]:
                print(BANNER)
                exit(0)

    print(BANNER)
    total, found, length, clear = 0, 0, 0, ''
    print("[>] loading addresses from local network")
    scan_info = iface_up(name, mask)
    if scan_info:
        iface, network = scan_info
        print("[>] scanning %s on network interface %s..." % (network, iface.name))
        for ip, host in scan_lan(network):
            try:
                clear = BSP % length + ' ' * length + BSP % length
                total += 1
                output = "[>] scanned: " + ip
                if host:
                    if outf:
                        print(ip + ':' + host, file=open(outf, "at+"))
                    found += 1
                    output = "[!] found host: " + ip + ' ' + '-'*(16 - len(ip)) + '> ' + host + '\n'
                print(clear + output, end='', flush=True)
                length = len(output)
            except KeyboardInterrupt:
                break
        print(clear, end='', flush=True)
    print("[+] scanned %s addresses, found %s" % (total, found))
    return 0

if __name__ == "__main__":

    try:
        exit(main(sys.argv))
    except KeyboardInterrupt:
        print("\nctrl+c pressed, quitting")
        exit(0)
