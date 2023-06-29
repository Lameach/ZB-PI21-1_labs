import socket

sock = socket.socket()

try:
    sock.bind(('', 80))
    print("Using port 80")
except OSError:
    sock.bind(('', 8080))
    print("Using port 8080")

sock.listen(5)

conn, addr = sock.accept()
print("Connected", addr)

data = conn.recv(8192)
msg = data.decode()

print(msg)

headers = msg.split('\n')
filename = headers[0].split()[1]

if filename == '/':
    filename = '/index.html'

fin = open(filename[1:])
content = fin.read()
fin.close()


resp = """HTTP/1.1 200 OK
Server: SelfMadeServer v0.0.1
Content-type: text/html
Connection: close

""" + content

conn.send(resp.encode())

conn.close()