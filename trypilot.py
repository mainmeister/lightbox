import cv2
import numpy as np
from numpy.linalg import norm


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


if __name__ == "__main__":
    img = cv2.imread("test.jpg")
    print(f'Brightness is {average_brightness(img)}',flush=True)
    print(f'Average color is {average_color(img)}',flush=True)
