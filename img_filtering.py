from PIL import ImageFilter
from PIL import Image

im = cv2.imread('gray_cap.jpg')

im1 = im.filter(ImageFilter.BLUR)

im2 = im.filter(ImageFilter.MinFilter(3))
im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
