from socket import *
import pyautogui as pygui

import pickle
import struct


def client(host, port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            image = pygui.screenshot()

            data = pickle.dumps(image)
            data = struct.pack('>I', len(data)) + data

            s.sendall(data)

        s.shutdown(SHUT_RDWR)


client("localhost", 1111)
