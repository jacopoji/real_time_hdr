import numpy as np
import scipy.misc
import scipy.ndimage
import matplotlib.pyplot as plt
import cv2

rgb = ['R','G','B']
for item in rgb:
    img_jpg = scipy.ndimage.imread("compsum_{}_2_resized.jpg".format(item))
    #img_jpg = cv2.resize(img_jpg,(1024,1024,))
    print(img_jpg[:][:].shape)
    #img_save = np.zeros((1024,1024))
    #img_save = img_jpg[:][:][0]
    #print(img_save.shape)
    np.savetxt("compsum_{}_2_resized.txt".format(item),img_jpg[:][:])
    #img_txt_new = img_txt * 255
    #np.savetxt("CCRF_{}_unnorm.txt".format(item),img_txt_new,fmt='%d')