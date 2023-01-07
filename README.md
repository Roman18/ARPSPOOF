# ARPSPOOF

## Tiny tool to provide an ARP-Cache-Poisoning attack

### Download

```console
python3 -m venv <name of env>
cd <name of env>/
git clone <link to repo>
pip install -r requirements.txt
chmod +x arpspoof.py
```

### Run

```console
sudo ./arpspoof.py -h
    ___    ____  ____  _____ ____  ____  ____  ______
   /   |  / __ \/ __ \/ ___// __ \/ __ \/ __ \/ ____/
  / /| | / /_/ / /_/ /\__ \/ /_/ / / / / / / / /_    
 / ___ |/ _, _/ ____/___/ / ____/ /_/ / /_/ / __/    
/_/  |_/_/ |_/_/    /____/_/    \____/\____/_/       
                                                     

usage: arpspoof.py [-h] [-i INTERFACE] [-v VICTIM] [-r ROUTER] [-d DELAY]

Tool for conducting an arpspoof attack

options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface INTERFACE
                        Specified a network interface for attack
  -v VICTIM, --victim VICTIM
                        First target IP
  -r ROUTER, --router ROUTER
                        Second target IP. It can be any target. Not only router IP
  -d DELAY, --delay DELAY
                        delay between injection of arp packages

./arpspoof.py -i eth0 -v <first target IP> -r <second target IP>

```
