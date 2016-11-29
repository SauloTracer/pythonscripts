import argparse
from socket import *

def printBanner(conn, port):
    try:
        if(port == 80):
            connSock.send("GET HTTP/1.1 \r \n")
        else:
            connSock.send("\r\n")

        #Receive data from target
        results = connSock.recv(4096)
        print("[+] {}".format(str(results)))
    except:
        print("[-] Not available.\n")
        
def connScan(host, port):
    try:
        #Create socket
        connSock = socket(AF_INET, SOCK_STREAM)
        #Try connection to host
        connSock.connect((host,port))
        print("[+] {} TCP open".format(port))
        printBanner(connSock, port)
    except:
        #FAIL
        print("[-] {} TCP closed".format(port))
    finally:
        connSock.close()

def portScan(host, ports):
    try:
        #If not an ip, resolve to one
        ip = gethostbyname(host)
    except:
        print("[-]Error: unkonw host")
        exit(0)

    try:
        #Se conseguiu o ip...
        tgtName = gethostbyaddr(ip)
        print("[+]--- Scan result for: {} ---".format(tgtName[0]))
    except:
        print("[+]--- Scan result for: {} ---".format(ip))

    #Scan listed ports
    for port in ports:
        connScan(host,int(port))
        

def main():
    #parse the command line arguments
    parser = argparse.ArgumentParser('Smart TCP Client Scanner')
    parser.add_argument("-a", "--address", type=str, help="The target ip address")
    parser.add_argument("-p", "--port", type=str, help="The port number to connect with")
    args = parser.parse_args()

    #Store the arguments values
    ip = args.address
    ports = str(args.port).split(',')

    #Call port scan
    portScan(ip, ports)

if __name__ == '__main__':
    main()

print('teste')
