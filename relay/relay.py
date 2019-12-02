import socket
import pickle
from threading import Thread
from socketserver import ThreadingMixIn
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import time
from time import sleep

master_host = socket.gethostname()
master_port = 2004
BUFFER_SIZE = 2048

# Multithreaded Python server
class ClientThread(Thread):
    def __init__(self,ip,port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        print("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):


        while True :
            # Get a byte buffer from Client
            data = conn.recv(2048)
            if len(data) > 0:
                # Forward this byte buffer over to master server
                master_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                master_conn.connect((master_host, master_port))
                master_conn.send(data)

                # Expect a response from master server
                master_reply = master_conn.recv(BUFFER_SIZE)
                master_conn.close()

                # Forward this response to client side
                conn.send(master_reply)

                # logging
                print("One message exchanged.")


# Multithreaded Python server
TCP_IP = '0.0.0.0'
TCP_PORT = 2019
BUFFER_SIZE = 2000

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

# Open up listening ports for multiple connections
while True:
    tcpServer.listen(4)
    print("Multithreaded Python server : Waiting for connections from TCP clients...")
    (conn, (ip,port)) = tcpServer.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
