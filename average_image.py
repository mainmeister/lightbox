import time
import cv2
import numpy as np
from numpy.linalg import norm
import pyautogui
import tkinter as tk


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
    screenshot(filename)
    img = cv2.imread(filename)
    return (average_color(img), average_brightness(img))
def screenshot(filename):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(filename)


if __name__ == "__main__":
    screenshot_filename = r'screenshot.png'

    root = tk.Tk()
    root.mainloop()

    while True:
        screenshot(screenshot_filename)
        print(averages(screenshot_filename))
        time.sleep(0.1)