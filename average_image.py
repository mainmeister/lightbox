import time
import cv2
import numpy as np
from numpy.linalg import norm
import pyautogui
import tkinter as tk


# from tkinter import *
# import tkinter


def average_color(img):
    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return avg_color


def average_brightness(img):
    if len(img.shape) == 3:
        # Colored RGB or BGR (*Do Not* use HSV images with this function)
        # create brightness with euclidean norm
        return np.average(norm(img, axis=2)) / np.sqrt(3)
    else:
        # Grayscale
        return np.average(img)


def averages(filename):
    img = screenshot(filename)
    return (average_color(img), average_brightness(img))


def screenshot(filename):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(filename)
    return cv2.imread(filename)

if __name__ == "__main__":
    class myapp:

        def __init__(self, master, filename):
            self.master = master
            self.filename = filename
            self.master.after_idle(self.get_screenshot_and_calculate)

        def get_screenshot_and_calculate(self):
            color, brightness = averages(self.filename)
            r, g, b = color
            self.master['bg'] = '#%02x%02x%02x' % (int(r), int(g), int(b))
            print(r, g, b, brightness)
            self.master.update_idletasks()
            self.master.after(0, self.get_screenshot_and_calculate)


    screenshot_filename = r'screenshot.png'
    root = tk.Tk()
    app = myapp(root, screenshot_filename)
    root.mainloop()
