import socket
import sys

# answer to written part: when you take out the sleep, it does not wait for the client so everything happens out of order

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    
    ts1Hostname = sys.argv[1]
    ts1ListenPort = int(sys.argv[2])
    localhost_addr = socket.gethostbyname(socket.gethostname())
    inProj = open("PROJ2-HNS.txt", "r+")
    # connect to the server on local machine
    server_binding = (localhost_addr, ts1ListenPort)
    cs.connect(server_binding)

    #Read lines from input and send to ls
    outputFile = open("resolved.txt", "w+")
    msg = inProj.readlines()
    for l in msg:
        cs.send(l.encode())
        result = cs.recv(200).decode("utf-8")
        outputFile.writelines(result + '\n')
        print("[C]: Recieved from ls server: " + result)

    # close the sockets
    inProj.close()
    cs.close()
    exit()

if __name__ == "__main__":
    client()
    print("Done.")