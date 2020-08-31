import numpy as np
import scipy.misc
import scipy.ndimage
import matplotlib.pyplot as plt

rgb = ['R','G','B']

for item in rgb:
    img = np.zeros((256,256))
    img[:,:] = scipy.ndimage.imread("compsum_{}_2_norm.jpg".format(item))
    #img[:,:,1] = scipy.ndimage.imread("CCRF_{}.jpg".format(item))
    #img[:,:,2] = scipy.ndimage.imread("CCRF_{}.jpg".format(item))

    img_resize = scipy.misc.imresize(img,400)
    scipy.misc.imsave("compsum_{}_2_resized.jpg".format(item),img_resize)
    #np.savetxt("CCRF_{}_resized.txt".format(item),img_resize[0],fmt = '%d')
    #print(img_resize.size)