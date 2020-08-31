from sklearn import preprocessing
import numpy as np
import cv2
import scipy.misc
k=2

def main():
    normalization_flag = True
    ROW_IND = 0
    COL_IND = 1
    count = 0
    B_normalization_flag = True
    G_normalization_flag = True
    R_normalization_flag = True
    max_iter = 15000
    for index in range(1,2):
        compsum_B_normalized = np.loadtxt('compsum_B_raw_{}.txt'.format(k**index),dtype = float)
        compsum_G_normalized = np.loadtxt('compsum_G_raw_{}.txt'.format(k**index),dtype = float)
        compsum_R_normalized = np.loadtxt('compsum_R_raw_{}.txt'.format(k**index),dtype = float)
        while normalization_flag and count < max_iter:
            if B_normalization_flag == True:
                compsum_B_before = compsum_B_normalized
                if count%2 == 0:
                    compsum_B_normalized = preprocessing.normalize(compsum_B_normalized, norm='l1',axis = ROW_IND)
                elif count%2 == 1:
                    compsum_B_normalized = preprocessing.normalize(compsum_B_normalized, norm='l1',axis = COL_IND)
                else:
                    print("Some unexpected behaviour happened")
                #print(np.mean(compsum_B_normalized != compsum_B_before))
                if np.mean(compsum_B_normalized != compsum_B_before) < 0.25:
                    #print(np.sum(compsum_B_normalized, axis=0))
                    print("performed {} normalizations for B Channel".format(count))
                    B_normalization_flag = False
                '''
                sum_after_B = np.sum(compsum_B_normalized,axis=None)
                sum_before_B = np.sum(compsum_B_before,axis = None)
                print(abs((sum_after_B - sum_before_B)/sum_before_B))
                if abs((sum_after_B -sum_before_B)/sum_before_B) < 0.05:
                #print(compsum_B_normalized)
                    #print(np.sum(compsum_B_normalized, axis=0))
                    print("performed {} normalizations for B Channel".format(count))
                    B_normalization_flag = False
                '''
            if G_normalization_flag == True:
                compsum_G_before = compsum_G_normalized
                if count%2 == 0:
                    compsum_G_normalized = preprocessing.normalize(compsum_G_normalized, norm='l1',axis = ROW_IND)
                elif count%2 ==1:
                    compsum_G_normalized = preprocessing.normalize(compsum_G_normalized, norm='l1',axis = COL_IND)
                else:
                    print("Some unexpected behaviour happened")
                #print(np.mean(compsum_G_normalized != compsum_G_before))
                if np.mean(compsum_G_normalized != compsum_G_before) < 0.25:
                    #print(np.sum(compsum_G_normalized, axis=0))
                    print("performed {} normalizations for G Channel".format(count))
                    G_normalization_flag = False
                '''
                if np.mean(compsum_G_normalized != compsum_G_before) == 0.2202301025390625:
                    print(np.sum(compsum_G_normalized, axis=0))
                    G_normalization_flag = False
                '''
                '''
                sum_after_G = np.sum(compsum_G_normalized,axis=None)
                sum_before_G = np.sum(compsum_G_before,axis = None)
                print(abs((sum_after_G - sum_before_G)/sum_before_G))
                if abs((sum_after_G -sum_before_G)/sum_before_G) < 0.05:
                #print(compsum_B_normalized)
                    #print(np.sum(compsum_G_normalized, axis=0))
                    print("performed {} normalizations for G Channel".format(count))
                    G_normalization_flag = False
                '''
            if R_normalization_flag == True:
                compsum_R_before = compsum_R_normalized
                if count%2 == 0:
                    compsum_R_normalized = preprocessing.normalize(compsum_R_normalized, norm='l1',axis = ROW_IND)
                elif count%2 ==1:
                    compsum_R_normalized = preprocessing.normalize(compsum_R_normalized, norm='l1',axis = COL_IND)
                else:
                    print("Some unexpected behaviour happened")
                if np.mean(compsum_R_normalized != compsum_R_before) < 0.25:
                    #print(np.sum(compsum_R_normalized, axis=0))
                    print("performed {} normalizations for R Channel".format(count))
                    R_normalization_flag = False
                '''
                sum_after_R = np.sum(compsum_R_normalized,axis=None)
                sum_before_R = np.sum(compsum_R_before,axis = None)
                print(abs((sum_after_R - sum_before_R)/sum_before_R))
                if abs((sum_after_R -sum_before_R)/sum_before_R) < 0.05:
                    print(np.sum(compsum_R_normalized, axis=0))
                    print("performed {} normalizations for R Channel".format(count))
                    R_normalization_flag = False
                '''
            if B_normalization_flag == G_normalization_flag and G_normalization_flag == R_normalization_flag and R_normalization_flag == False:
                normalization_flag = False
            count += 1
        scipy.misc.imsave('compsum_B_{}_norm.jpg'.format(k**index),compsum_B_normalized)
        scipy.misc.imsave('compsum_G_{}_norm.jpg'.format(k**index),compsum_G_normalized)
        scipy.misc.imsave('compsum_R_{}_norm.jpg'.format(k**index),compsum_R_normalized)
        np.savetxt("compsum_B_{}_norm.txt".format(k**index),compsum_B_normalized,fmt = '%f')
        np.savetxt("compsum_G_{}_norm.txt".format(k**index),compsum_G_normalized,fmt = '%f')
        np.savetxt("compsum_R_{}_norm.txt".format(k**index),compsum_R_normalized,fmt = '%f')
        print(np.max(compsum_G_normalized,axis = None))
if __name__ == "__main__":
    main()