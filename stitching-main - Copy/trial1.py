from stitching import Stitcher
import cv2 as cv
from matplotlib import pyplot as plt
from PIL import Image
import time


#initialize Stitcher
stitcher = Stitcher()

#function to plot resulting stitched image
def plot_image(img, figsize_in_inches=(5,5)):
    fig, ax = plt.subplots(figsize=figsize_in_inches)
    ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.savefig('panorama.png')
    plt.show()

start = time.perf_counter()

#setting variables (constructor)
stitcher = Stitcher(detector = "sift", confidence_threshold=.01)

PhoneArm = ['PhoneArm1.jpg', 'PhoneArm2.jpg'] #'PhoneArm4.jpg']

weir = ['weir_1.jpg', 'weir_2.jpg', 'weir_3.jpg', 'weir_noise.jpg']

Tripod = ['Tripod1_1.jpg', 'Tripod1_2.jpg', 'Tripod1_3.jpg']

split = ["right_image.jpg", "middle_image.jpg", "left_image.jpg"]

#list of images to feed to stitcher
imgList = Tripod
panorama = stitcher.stitch_verbose(split)

time_end = time.perf_counter() - start
print(time_end)

plot_image(panorama, (20,20))


