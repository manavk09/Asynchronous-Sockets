import socket
import threading
import time
import random

# answer to written part: when you take out the sleep, it does not wait for the client so everything happens out of order

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())
    inProj = open("PROJ2-HNS.txt", "r+")
    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)
    # Reading form a file
    msg = inProj.readlines()
    l = len(msg)
    for i in range(0,l):
        temp = ""
        temp += msg[i]
        print(temp)
        # if i != l-1:
        #     temp += "\r\n"
        cs.send(temp.encode('utf-8'))

    file1 = open("resolved.txt", "w+")
    # Receive data from the server
    data_from_server=cs.recv(100)

    while data_from_server:
        # Writing data to a file
        file1.writelines(data_from_server.decode('utf-8'))
        data_from_server = cs.recv(100)

    #print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # close the client socket
    inProj.close()
    cs.close()
    exit()


if __name__ == "__main__":
    # t1 = threading.Thread(name='server', target=server)
    # t1.start()

    # time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()
    # time.sleep(5)
    print("Done.")