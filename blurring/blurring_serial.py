from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
import timeit

def blur(in_data, out_data):
    ny, nx = in_data.shape
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            out_data[i, j] = (in_data[i, j-1] + in_data[i, j+1] + 
                                    in_data[i-1, j] + in_data[i+1, j])/4.0

if __name__ == "__main__":
    n = 50
    img = img_as_float(io.imread('coffee.png', as_grey=True))
    print(img)
    img_cpy = np.copy(img)
    t1 = timeit.default_timer()
    for i in range(n):
        blur(img, img_cpy)
        img_cpy, img = img, img_cpy
    t2 = timeit.default_timer()
    print(t2-t1)
    io.imshow(img)
    plt.show() 
