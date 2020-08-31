import numpy as np
import cv2
from math import log
from numba import vectorize
import time
import scipy.misc
k = 2
base = 222
bias_base = 10
bias = [log(bias_base+i) for i in range(1,60,3)]

#@vectorize([np.uint8(np.uint8,np.uint8)])
def comparagram(fq,f2q):
    result_B = np.zeros((256,256))
    result_G = np.zeros((256,256))
    result_R = np.zeros((256,256))
    '''
    init_time = time.time()
    for i in range(fq.shape[0]):
        for j in range(fq.shape[1]):
            for k in range(fq.shape[2]):
                if k == 0:
                    result_B[fq[i][j][0]][f2q[i][j][0]] += 1
                elif k == 1:
                    result_G[fq[i][j][1]][f2q[i][j][1]] += 1
                elif k == 2:
                    result_R[fq[i][j][2]][f2q[i][j][2]] += 1
    print("Time taken = ",time.time()-init_time)
    '''
    # B channel
    init_time = time.time()
    for x, y in zip(f2q[:,:,0].reshape(f2q.shape[0]*f2q.shape[1],), fq[:,:,0].reshape(fq.shape[0]*fq.shape[1],)):
        result_B[x][y] += 1
    # B channel
    for x, y in zip(f2q[:, :, 1].reshape(f2q.shape[0]*f2q.shape[1],), fq[:, :, 1].reshape(fq.shape[0]*fq.shape[1],)):
        result_G[x][y] += 1
    # B channel
    for x, y in zip(f2q[:, :, 2].reshape(f2q.shape[0]*f2q.shape[1],), fq[:, :, 2].reshape(fq.shape[0]*fq.shape[1],)):
        result_R[x][y] += 1
    print("Time taken = ",time.time()-init_time)
    
    #result_B[result_B>255] = 255
    #result_G[result_G>255] = 255
    #result_R[result_R>255] = 255
    cv2.imshow("B",np.flip(result_B,0))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return result_B,result_G,result_R

if __name__ == "__main__":
    #print(bias)
    img1 = cv2.imread('photo/03 May 2018 14_51_59/18.18265833864414.jpg')
    img2 = cv2.imread('photo/03 May 2018 14_51_59/36.36531667728828.jpg')
    #cv2.imshow("s",img1)
    #cv2.waitKey(0)
    b,g,r = comparagram(img1,img2)
    b[b>255]=255
    cv2.imshow('b',b)
    cv2.waitKey(0)
    scipy.misc.imsave("out_" + '18.18265833864414' + "_" + '36.36531667728828' + "_B.jpg",np.flip(b,0))
    print(b)