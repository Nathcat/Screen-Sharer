from socket import *
import pickle
import struct
#from ScreenShare import test
import test

def server(port):
    app = test.Application()

    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind(("", port))

        s.listen()

        conn, addr = s.accept()

        while True:
            raw_msglen = conn.recv(4)
            msglen = struct.unpack('>I', raw_msglen)[0]

            total = 0
            total_data = b""
            while len(total_data) < msglen:
                data = conn.recv(msglen)
                total_data += data
                total += len(data)

            data = pickle.loads(total_data)

            app.display(data)


server(1234)
