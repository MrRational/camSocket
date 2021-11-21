import cv2
import pickle
import socket
import struct

TCP_IP = '127.0.0.1'
TCP_PORT = 9501


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # establishing a tcp connection
sock.bind((TCP_IP, TCP_PORT))
sock.listen(5)

while True:
    (client_socket, client_address) = sock.accept() # waiting  for client
    print ('connection established with ' +str(client_address))
    cap = cv2.VideoCapture(0)
    while True:
        flag, frame = cap.read()
        if flag:
            frame = pickle.dumps(frame)
            size = len(frame)
            p = struct.pack('I', size)
            frame = p + frame
            client_socket.sendall(frame)
        














