import cv2
import numpy as np
from PIL import Image

from PIL import ImageFilter

 

# Open the Image and create an Image Object

imagePath = "img/test.jpg"

imageObject = Image.open(imagePath)

imageObject.show()

 

# Apply emboss filter on to the image

imageEmboss = imageObject.filter(ImageFilter.EMBOSS)

 

# Display the embossed image

imageEmboss.show()