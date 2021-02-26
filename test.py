import matplotlib.pyplot as plt
import threading


class Application:
    def display(self, img):
        plt.imshow(img)

        threading.Thread(target=lambda: plt.pause(0.000000001)).start()
