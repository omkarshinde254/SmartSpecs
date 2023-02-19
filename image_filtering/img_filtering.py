import cv2
from PIL import ImageFilter
from PIL import Image

im = Image.open('captured.jpg')
im.show()

im1 = im.filter(ImageFilter.BLUR)
im1.save('blur.jpg')

im3 = im.filter(ImageFilter.MinFilter)  # same as MinFilter(3)
im3.save('minifilter.jpg')

im4 = im.filter(ImageFilter.FIND_EDGES)
im4.save('edge.jpg')

im5 = im.filter(ImageFilter.EDGE_ENHANCE)
im5.save('edgeEN.jpg')

im6 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
im6.save('edgeENMMMMM.jpg')

im8 = im.filter(ImageFilter.DETAIL)
im8.save('detail.jpg')

im9 = im.filter(ImageFilter.EMBOSS)
im9.save('emboss.jpg')

im10 = im.filter(ImageFilter.SMOOTH)
im10.save('smooth.jpg')

im11 = im.filter(ImageFilter.SMOOTH_MORE)
im11.save('smoothmmmm.jpg')

im12 = im.filter(ImageFilter.SHARPEN)
im12.save('sharpen.jpg')

