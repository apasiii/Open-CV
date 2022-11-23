import numpy as np
import cv2

#read image
img_src = cv2.imread('img/lowpass.jpg')

#prepare the 5x5 shaped filter
kernel = np.array([[1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 1, 1, 1, 1]])
kernel = kernel/sum(kernel)

#filter the source image
img_rst = cv2.filter2D(img_src,-1,kernel)

#save result image
cv2.imwrite('hasil_low-pass.jpg',img_rst)