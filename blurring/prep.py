from skimage import io, data
from skimage.transform import rescale

scale_factor = 1

img = data.load('coffee.png')
img = rescale(img, scale=scale_factor)
io.imsave('coffee.png', img)
