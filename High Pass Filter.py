import numpy as np
import cv2

#read image
img_src = cv2.imread('img/test.jpg')

#edge detection filter
kernel = np.array([[0.0, -1.0, 0.0], 
                   [-1.0, 4.0, -1.0],
                   [0.0, -1.0, 0.0]])

kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)

#filter the source image
img_rst = cv2.filter2D(img_src,-1,kernel)

#save result image
cv2.imwrite('hasi_high_pass.jpg',img_rst)