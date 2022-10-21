import sys
import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    lsPort = int(sys.argv[1])
    server_binding = ('', lsPort)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    inputFile = open("PROJ2-DNSTS1.txt", "r")
    dnsDict = {}
    line = inputFile.readline().strip()
    #Populates the map
    while(line):
        items = line.split()
        dnsDict[items[0].lower()] = line.strip()
        line = inputFile.readline()
    inputFile.close()

    while(True):
        hostName = csockid.recv(200)
        if(not(hostName)):
            break
        print("[TS1]: Recieved host name from ls: " + hostName)  

        if(hostName in dnsDict):
            result = dnsDict[hostName] + " IN"
            csockid.send(result.encode("utf-8"))

    csockid.close()
    ss.close()

if __name__ == "__main__":
    server()
    print("Done.")