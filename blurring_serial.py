from skimage import data, io
import matplotlib.pyplot as plt

def blur(data, nblurs):
    blurred_data_1 = data.copy()
    blurred_data_2 = data.copy()
    ny, nx = data.shape
    for step in range(nblurs):  
        for i in range(1, ny-1):
            for j in range(1, nx-1):
                blurred_data_1[i, j] = (blurred_data_2[i, j-1] + blurred_data_2[i, j+1] + 
                                        blurred_data_2[i-1, j] + blurred_data_2[i+1, j])/4.0
        blurred_data_2, blurred_data_1 = blurred_data_1, blurred_data_2
    return blurred_data_2



if __name__ == "__main__":
    n = 50
    img = data.load('coffee.png', as_grey=True)
    blurred_img = blur(img, n)
    io.imshow(blurred_img)
    plt.show()
