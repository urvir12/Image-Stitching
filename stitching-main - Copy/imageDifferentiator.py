
# import module 
from PIL import Image, ImageChops 
  
# assign images 
img1 = Image.open("weir_1.jpg")

img2 = Image.open("09_result.jpg") #real result

img1.show(title="Original")
img2.show(title="Stitched")

print(img1.size, img2.size)
# finding difference 
diff = ImageChops.difference(img1, img2) 
  
# showing the difference 
diff.show(title="Diff") 