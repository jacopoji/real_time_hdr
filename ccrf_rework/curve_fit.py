import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os
import pickle
from math import *
k=2
def func(x, a, c):
    return x * np.power(2, a * c) / np.power((1 + np.power(x, 1 / c) * (np.power(2, a) - 1)), c)

def roll_data(comparagram,color):
    x_data = np.zeros(int(np.sum(comparagram)))
    y_data = np.zeros(int(np.sum(comparagram)))
    data_pos_flag = 0
    for i in range(256):
        for j in range(256):
            if comparagram[i][j] != 0:
                for num in range(int(comparagram[i][j])):
                    y_data[data_pos_flag] = i
                    x_data[data_pos_flag] = j
                    data_pos_flag += 1
    print("total :",np.sum(int(np.sum(comparagram))))
    print("went through :",data_pos_flag)
    #np.savetxt("result/fit_" + color + "fit.txt", fit_curve, fmt="%d")
    #x_axis = np.array(range(256))
    #plt.plot(x_axis[fit_curve > 0],fit_curve[fit_curve > 0], c='black', linewidth=2.0)
    #plt.savefig("result/fit_"+ color + ".jpg")
    #plt.clf()
    return y_data, x_data

def main():
    for index in range(1,2):
        compsum_loaded_B = np.loadtxt('compsum_B_raw_{}.txt'.format(k**index),dtype = float)
        compsum_loaded_G = np.loadtxt('compsum_G_raw_{}.txt'.format(k**index),dtype = float)
        compsum_loaded_R = np.loadtxt('compsum_R_raw_{}.txt'.format(k**index),dtype = float)


        plot_x_data = np.linspace(0.0,1.0,num=256)
        fit_B,x_B = roll_data(np.flip(compsum_loaded_B,0),'B')
        x_data = (x_B+0.5) / 256.
        y_data = (fit_B+0.5) / 256.
        #y_data = y_data.astype(np.float32)
        #x_data = x_data.astype(np.float32)
        #print(ki)
        popt, pcov = curve_fit(func, x_data, y_data,maxfev=10000)
        with open("fparam_{}_B.txt".format(k**index),'w') as f:
            f.write("{},{}".format(*popt))
        plt.plot(x_data,y_data)
        #print(*popt)
        plt.plot(plot_x_data, func(plot_x_data, *popt), 'r-',label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
        plt.legend()
        #print("Saving B k=", k**index)
        plt.savefig('fit_curve_B_{}.png'.format(k**index))
        plt.clf()


        fit_R,x_R = roll_data(np.flip(compsum_loaded_R,0),'R')
        x_data = (x_R+0.5) / 256.
        y_data = (fit_R+0.5) / 256.
        #y_data = y_data.astype(np.float32)
        #x_data = x_data.astype(np.float32)
        plt.plot(x_data,y_data)
        popt, pcov = curve_fit(func, x_data, y_data,maxfev=10000)
        with open("fparam_{}_R.txt".format(k**index),'w') as f:
            f.write("{},{}".format(*popt))
        plt.plot(plot_x_data, func(plot_x_data, *popt), 'r-',label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
        plt.legend()
        plt.savefig('fit_curve_R_{}.png'.format(k**index))
        plt.clf()


        fit_G,x_G = roll_data(np.flip(compsum_loaded_G,0),'G')
        x_data = (x_G+0.5) / 256.
        y_data = (fit_G+0.5) / 256.
        #y_data = y_data.astype(np.float32)
        #x_data = x_data.astype(np.float32)
        plt.plot(x_data,y_data)
        popt, pcov = curve_fit(func, x_data, y_data,maxfev=10000)
        with open("fparam_{}_G.txt".format(k**index),'w') as f:
            f.write("{},{}".format(*popt))
        plt.plot(plot_x_data, func(plot_x_data, *popt), 'r-',label='fit: a=%5.3f, c=%5.3f' % tuple(popt))
        plt.legend()
        plt.savefig('fit_curve_G_{}.png'.format(k**index))
        plt.clf()

if __name__ == '__main__':
    main()