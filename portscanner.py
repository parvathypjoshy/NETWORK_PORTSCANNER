from socket import *

def conScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print(f"[+] {tgtPort}/tcp open")
        connSkt.close()
    except:
        print(f"[-] {tgtPort}/tcp closed")

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[-] Cannot resolve {tgtHost}")
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"\n[+] Scan result for: {tgtName[0]}")
    except:
        print(f"\n[+] Scan result for: {tgtIP}")

    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print(f"Scanning port {tgtPort}")
        conScan(tgtHost, tgtPort)

if __name__ == "__main__":
    portScan("google.com", [80, 22])
