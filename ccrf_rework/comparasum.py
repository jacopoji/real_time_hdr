import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import pickle
from math import *
import scipy.misc
base = 16
bias_base = 10
bias = [log(bias_base+i,3) for i in range(1,540000,18000)]
exposure_range = 11

set_dir = ["photo/" + folders for folders in os.listdir("photo") if os.path.isdir("photo/"+folders) == True]
k = 2
def main():
    for index in range(1,2): #loop for k
        compsum_B = np.zeros((256,256),dtype="float64")
        compsum_G = np.zeros((256,256),dtype="float64")
        compsum_R = np.zeros((256,256),dtype="float64")
        for j in range(len(bias)): #loop for bias
            exposures = [(base+bias[j])*k**i for i in range(exposure_range)]
            
            ki = 2**index
            file_list_g = ['out_{}_{}_G.txt'.format(exposures[i],exposures[i+index]) for i in range(len(exposures)-index)]
            file_list_b = ['out_{}_{}_B.txt'.format(exposures[i],exposures[i+index]) for i in range(len(exposures)-index)]
            file_list_r = ['out_{}_{}_R.txt'.format(exposures[i],exposures[i+index]) for i in range(len(exposures)-index)]
            #temp = ["tmp/"]
            #set_dir = temp

            count = 1
            for i in set_dir:
                print("current folder:{}/{},index: {}/{}, bias: {}/{}".format(count,len(set_dir),index,3,j+1,len(bias)))
                for fname_b in file_list_b:
                    compsum_B += np.loadtxt(os.path.join(i,fname_b))
                for fname_g in file_list_g:
                    compsum_G += np.loadtxt(os.path.join(i,fname_g))
                for fname_r in file_list_r:
                    compsum_R += np.loadtxt(os.path.join(i,fname_r))
                count+=1
            np.savetxt("compsum_B_raw_{}.txt".format(k**index),compsum_B,fmt="%d")
            np.savetxt("compsum_G_raw_{}.txt".format(k**index),compsum_G,fmt="%d")
            np.savetxt("compsum_R_raw_{}.txt".format(k**index),compsum_R,fmt="%d")

            compsum_B[compsum_B>255] = 255
            compsum_G[compsum_G>255] = 255
            compsum_R[compsum_R>255] = 255

            scipy.misc.imsave('compsum_B_{}.jpg'.format(k**index),compsum_B)
            scipy.misc.imsave('compsum_G_{}.jpg'.format(k**index),compsum_G)
            scipy.misc.imsave('compsum_R_{}.jpg'.format(k**index),compsum_R)

            #sum_B = Image.fromarray(np.uint8(compsum_B,mode='L'))
            #sum_G = Image.fromarray(np.uint8(compsum_G,mode='L'))
            #sum_R = Image.fromarray(np.uint8(compsum_R,mode='L'))

            #sum_B.save('compsum_B_{}.jpg'.format(k**index))
            #sum_G.save('compsum_G_{}.jpg'.format(k**index))
            #sum_R.save('compsum_R_{}.jpg'.format(k**index))

if __name__ == "__main__":
    main()