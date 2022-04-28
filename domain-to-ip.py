import sys
import socket

website = sys.argv[1]

try:
    ip = socket.gethostbyname(website);
    print(website+" ip is: "+ip)
except Exception as e:
    print(e)

