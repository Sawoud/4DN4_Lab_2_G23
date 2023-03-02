from asyncio.windows_events import NULL
import socket
import argparse
import sys
import csv
import numpy as np

MarksArray = NULL
results = []


def readfile():
    with open("course_grades_2023.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            results.append(row)

    for result in results:
        print(result)


def GML1A():
    avg = 0
    for i in range(1,results.size):
        avg = avg + results[3][i]
    return avg/results.size

def GML2A():
    avg = 0
    for i in range(1,results.size):
        avg = avg + results[4][i]
    return avg/results.size

def GML3A():
    avg = 0
    for i in range(1,results.size):
        avg = avg + results[5][i]
    return avg/results.size

def GML4A():
    avg = 0
    for i in range(1,results.size):
        avg = avg + results[6][i]
    return avg/results.size

def GMA():
    avg = 0
    for i in range(1,results.size):
        avg = avg + results[7][i]
    return avg/results.size
def GEA():
    avg = 0
    for i in range(1,results.size):
        avg = avg + (results[8]+results[9]+results[10]+results[11])/4
    return avg/results.size

def GG(i):
    return results[i]

readfile()
print(GML1A())
#class Server:

#    HOSTNAME = "0.0.0.0"      # All interfaces.
#    PORT = 50000
#    RECV_BUFFER_SIZE = 1024 # Used for recv.
#    MAX_CONNECTION_BACKLOG = 10
#    MSG_ENCODING = "utf-8" # Unicode text encoding.
#    SOCKET_ADDRESS = (HOSTNAME, PORT)

#    def __init__(self):
#        self.create_listen_socket()
#        self.process_connections_forever()

#    def create_listen_socket(self):
#        try:
#            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#            self.socket.bind(Server.SOCKET_ADDRESS)
#            self.socket.listen(Server.MAX_CONNECTION_BACKLOG)
#            print("Listening on port {} ...".format(Server.PORT))
#        except Exception as msg:
#            print(msg)
#            sys.exit(1)


#    def connection_handler(self, client):
#        connection, address_port = client
#        print("-" * 72)
#        print("Connection received from {}.".format(address_port))
#        print(client)

#        while True:
#            try:
#                recvd_bytes = connection.recv(Server.RECV_BUFFER_SIZE)
#                if len(recvd_bytes) == 0:
#                    print("Closing client connection ... ")
#                    connection.close()
#                    break
#                recvd_str = recvd_bytes.decode(Server.MSG_ENCODING)
#                print("Received: ", recvd_str)
#                connection.sendall(recvd_bytes)
#                print("Sent: ", recvd_str)

#            except KeyboardInterrupt:
#                print()
#                print("Closing client connection ... ")
#                connection.close()
