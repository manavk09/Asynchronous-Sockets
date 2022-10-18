import threading
import time
import random

import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    data_from_client = csockid.recv(100)
    file1 = open("sample-out-proj.txt", "w")
    clientData = ""
    while(data_from_client):
        # file1.writelines(data_from_server.decode('utf-8'))
        # print(data_from_client)
        clientData+=(data_from_client.decode('utf-8'))
        data_from_client = csockid.recv(100)
    ##print(clientData)

    lines = clientData.split('\n')
    ##print(lines)
    # send a intro message to the client.  
    # with open("in-proj.txt", "r+") as inProj:
    #     # Reading form a file
    #     msg = inProj.readlines()
        
    l = len(lines)
    for i in range(0,l):
        curLine = ""
        curLine += lines[i].strip()[::-1]
        if i != l-1:
            curLine += "\r\n"
        file1.writelines(curLine)

    # inProj.close()
    # Close the server socket
    ss.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(random.random() * 5)
    # t2 = threading.Thread(name='client', target=client)
    # t2.start()

    time.sleep(5)
    print("Done.")