from socket import *
import pyautogui as pygui

import pickle
import struct

import mss
import mss.tools
from PIL import Image


width, height= pygui.size()
capture_region = {'top': 0, 'left': 0, 'width': width, 'height': height}
sct = mss.mss()


def screenshot():
    img = sct.grab(capture_region)
    img = Image.frombytes("RGB", img.size, img.bgra, "raw", "BGRX")

    return img


def client(host, port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            image = pygui.screenshot()

            data = pickle.dumps(image)
            data = struct.pack('>I', len(data)) + data

            s.sendall(data)

        s.shutdown(SHUT_RDWR)


client("localhost", 1234)
