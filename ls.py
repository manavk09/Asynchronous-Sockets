import sys
import socket
import select

def server():
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts1Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts2Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    lsListenPort = int(sys.argv[1])
    ts1Hostname = sys.argv[2]
    ts1ListenPort = int(sys.argv[3])
    ts2Hostname = sys.argv[4]
    ts2ListenPort = int(sys.argv[5])

    cs_server_binding = ('', lsListenPort)
    clientSocket.bind(cs_server_binding)
    clientSocket.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = clientSocket.accept()
    
    print ("[S]: Got a connection request from a client at {}".format(addr))

    ts1_server_binding = (ts1Hostname, ts1ListenPort)
    ts1Socket.connect(ts1_server_binding)


    ts2_server_binding = (ts2Hostname, ts2ListenPort)
    ts2Socket.connect(ts2_server_binding)


    while (True):
        data_from_client = csockid.recv(200).decode("utf-8").strip()
        if(not(data_from_client)):
            break
        
        print("[LS] received from client: " + data_from_client)
        ts1Socket.send(data_from_client.encode("utf-8"))
        ts2Socket.send(data_from_client.encode("utf-8"))

        readReady, writeReady, errors = select.select([ts1Socket,ts2Socket],[],[],5)

        if readReady:
            tsResponse = readReady[0].recv(200).decode("utf-8")
            print("[LS] TS1 Response received: " + tsResponse)
            csockid.send(tsResponse.encode("utf-8"))
        else:
            print("[LS]: Not found in [TS]")
            timeOutMessage = data_from_client + " - TIMED OUT"
            csockid.send(timeOutMessage.encode("utf-8"))


    # Close the server socket
    clientSocket.close()
    ts1Socket.close()
    exit()

if __name__ == "__main__":
    server()
    print("Done.")