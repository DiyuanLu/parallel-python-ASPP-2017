from skimage import data, io
import matplotlib.pyplot as plt
import numpy as np

def blur(in_data, out_data):
    ny, nx = in_data.shape
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            out_data[i, j] = (in_data[i, j-1] + in_data[i, j+1] + 
                                    in_data[i-1, j] + in_data[i+1, j])/4.0

if __name__ == "__main__":
    n = 50
    img = data.load('coffee.png', as_grey=True)
    img_cpy = np.copy(img)

    for i in range(n):
        blur(img, img_cpy)
        img_cpy, img = img, img_cpy
    io.imshow(img)
    plt.show() 
