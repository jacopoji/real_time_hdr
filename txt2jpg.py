import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

rgb = ['R','G','B']
for item in rgb:
    img_txt = np.loadtxt("CCRF_{}_lighten.txt".format(item))
    scipy.misc.imsave("CCRF_{}_lighten.jpg".format(item),img_txt)
    #img_txt_new = img_txt * 255
    #np.savetxt("CCRF_{}_unnorm.txt".format(item),img_txt_new,fmt='%d')