import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1239))
complete_info = ''
while True:
    msg=s.recv(12)
    if len(msg) <= 0:
        break
complete_info += msg.decode("utf-8")
print(complete_info)
