from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
import timeit

def blur(in_data, out_data):
    ny, nx = in_data.shape
    out_data[1:-1, 1:-1] = (in_data[0:-2, 1:-1] + in_data[2:, 1:-1] +
                            in_data[1:-1, 0:-2] + in_data[1:-1, 2:])/4.0

if __name__ == "__main__":
    n = 100
    img = img_as_float(io.imread('coffee.png', as_grey=True))
    img_cpy = np.copy(img)
    t1 = timeit.default_timer()
    for i in range(n):
        blur(img, img_cpy)
        img_cpy, img = img, img_cpy
    t2 = timeit.default_timer()
    print(t2-t1)
    io.imshow(img)
    plt.show() 
