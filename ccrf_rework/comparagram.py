from PIL import Image
import numpy as np
import cv2
import os
from math import *
import scipy.misc
from multiprocessing import Pool, freeze_support, Process,Queue,Value
import queue
import time
photoBaseDir = 'photo'
base = 16
bias_base = 10
bias = [log(bias_base+i,3) for i in range(1,540000,18000)]
exposure_range = 11

# place 2 pictures in the dir
# 1st one with high exposure, 2nd one with low exposure
# differ by k (k = 2 in our case)
def calc_histgram(f2q,fq,filename):
    '''
    Input are two images that are pre-loaded. Saves the comparagram of the two images as txt
    and also returns the comparagram of the two images.
    '''
    comparagram_B = np.zeros((256, 256))
    comparagram_G = np.zeros((256, 256))
    comparagram_R = np.zeros((256, 256))

    # B channel
    for x, y in zip(f2q[:,:,0].reshape(f2q.shape[0]*f2q.shape[1],), fq[:,:,0].reshape(fq.shape[0]*fq.shape[1],)):
        comparagram_B[x][y] += 1
    # B channel
    for x, y in zip(f2q[:, :, 1].reshape(f2q.shape[0]*f2q.shape[1],), fq[:, :, 1].reshape(fq.shape[0]*fq.shape[1],)):
        comparagram_G[x][y] += 1
    # B channel
    for x, y in zip(f2q[:, :, 2].reshape(f2q.shape[0]*f2q.shape[1],), fq[:, :, 2].reshape(fq.shape[0]*fq.shape[1],)):
        comparagram_R[x][y] += 1

    np.savetxt(filename + "_B.txt", np.flip(comparagram_B, 0), fmt="%d")
    np.savetxt(filename + "_G.txt", np.flip(comparagram_G, 0), fmt="%d")
    np.savetxt(filename + "_R.txt", np.flip(comparagram_R, 0), fmt="%d")
    comparagram_B[comparagram_B>255] = 255
    comparagram_G[comparagram_G>255] = 255
    comparagram_R[comparagram_R>255] = 255
    scipy.misc.imsave(filename + "_B.jpg",np.flip(comparagram_B,0))
    scipy.misc.imsave(filename + "_G.jpg",np.flip(comparagram_G,0))
    scipy.misc.imsave(filename + "_R.jpg",np.flip(comparagram_R,0))
    return comparagram_B,comparagram_G,comparagram_R

def multi_run_wrapper(args):
   return calc_histgram(*args)

def proc1(in_queue):
    while True:
        try:
            v=in_queue.get() #get
            if v is None:
                break
            else:
                #print('{}-----{}-----{}'.format(v[0],v[1],v[2]))
                calc_histgram(v[0],v[1],v[2])
        except queue.Empty:
            continue
def proc2(in_queue):
    while True:
        try:
            v=in_queue.get() #get
            if v is None:
                break
            else:
                #print('{}-----{}-----{}'.format(v[0],v[1],v[2]))
                calc_histgram(v[0],v[1],v[2])
        except queue.Empty:
            continue
def proc3(in_queue):
    while True:
        try:
            v=in_queue.get() #get
            if v is None:
                break
            else:
                #print('{}-----{}-----{}'.format(v[0],v[1],v[2]))
                calc_histgram(v[0],v[1],v[2])
        except queue.Empty:
            continue

def proc4(in_queue):
    while True:
        try:
            v=in_queue.get() #get
            if v is None:
                break
            else:
                #print('{}-----{}-----{}'.format(v[0],v[1],v[2]))
                calc_histgram(v[0],v[1],v[2])
        except queue.Empty:
            continue
def main(to_proc_1,to_proc_2,to_proc_3,to_proc_4):
    '''
    Loops through all the possible photos and computes the comparagram of the photos
    index loops for different k values
    j loops for the biased exposure values
    i loops for the different photos
    saves the comparagrams as images.
    '''
    photo = os.listdir(photoBaseDir)
    k = 2
    count = 1
    for item in photo:
        if any(image_file_name.endswith(".txt") for image_file_name in os.listdir(os.path.join(photoBaseDir,item))):
            continue
        #imgFiles =["15.625.jpg","31.25.jpg","62.5.jpg","125.jpg","250.jpg","500.jpg","1000.jpg","2000.jpg",
        #          "4000.jpg","8000.jpg","16000.jpg","32000.jpg","64000.jpg","128000.jpg"
        #          ]
        for index in range(1,2): #loop for k
            #print("imgFiles = {}".format(imgFiles))
            for j in range(len(bias)): #loop for bias
                #init_time = time.time()
                imgFiles = ["{}.jpg".format((base+bias[j])*k**i) for i in range(exposure_range)]
                #imageFiles = os.listdir(os.path.join(photoBaseDir, item))
                print("current folder:{}/{},index: {}/{}, bias: {}/{}".format(count,len(photo),index,3,j+1,len(bias)))
                img = ["{}/{}/{}".format(photoBaseDir,item,fname) for fname in imgFiles]
                #print(img)
                #pool = Pool(3)
                proc_count = 0
                for i in range(len(img)-index):
                    fq_element = img[i]
                    f2q_element = img[i+index]
                    #f4q_element = img[i+2*index]
                    #f8q_element = img[i+3*index]

                    fq = cv2.imread(fq_element)
                    f2q = cv2.imread(f2q_element)
                    #f4q = cv2.imread(f4q_element)
                    #f8q = cv2.imread(f8q_element)

                    fq_fname=imgFiles[i]
                    f2q_fname=imgFiles[i+index]
                    #f4q_fname=imgFiles[i+2*index]
                    #f8q_fname=imgFiles[i+3*index]

                    filename_1 = photoBaseDir + "/"+ item+"/out_"+fq_fname.split('.jpg')[0]+ "_"+ f2q_fname.split('.jpg')[0]
                    
                    if proc_count%4 == 0:
                        to_proc_1.put((f2q,fq,filename_1))
                    elif proc_count%4 == 1:
                        to_proc_2.put((f2q,fq,filename_1))
                    elif proc_count%4 == 2:
                        to_proc_3.put((f2q,fq,filename_1))
                    elif proc_count%4 ==3:
                        to_proc_4.put((f2q,fq,filename_1))
                    else:
                        print("Something unexpected has happened to the queue input")
                    proc_count += 1
                    #filename_2 = photoBaseDir + "/"+ item+"/out_"+f2q_fname.split('.jpg')[0]+ "_"+ f4q_fname.split('.jpg')[0]
                    #filename_3 = photoBaseDir + "/"+ item+"/out_"+f4q_fname.split('.jpg')[0]+ "_"+ f8q_fname.split('.jpg')[0]

                    #B,G,R = pool.starmap(calc_histgram,[(f2q,fq,filename_1),(f4q,f2q,filename_2),(f8q,f4q,filename_3)])

                    #img_B = np.loadtxt("CCRF_{}_lighten.txt".format(item))
                    #img_B = Image.fromarray(np.flip(B, 0), mode='L')
                    #img_G = Image.fromarray(np.flip(G, 0), mode='L')
                    #img_R = Image.fromarray(np.flip(R, 0), mode='L')
                    #np.savetxt("mono_after.txt",comparagram,fmt="%d")
                    #img_B.save(photoBaseDir + "/"+ item+"/out_" + fq_fname.split('.jpg')[0] + "_" + f2q_fname.split('.jpg')[0] + "_B.jpg")
                    #img_G.save(photoBaseDir + "/" +item+"/out_" + fq_fname.split('.jpg')[0] + "_" + f2q_fname.split('.jpg')[0] + "_G.jpg")
                    #img_R.save(photoBaseDir + "/" +item+"/out_" + fq_fname.split('.jpg')[0] + "_" + f2q_fname.split('.jpg')[0] + "_R.jpg")
                #print("time taken to resolve a bias = ",time.time()-init_time)
        count += 1
    
    #########progress to finish
    init_prog = '-' * 100
    #progress_save = '-'
    total = len(bias) * (exposure_range-1)
    to_proc_1.put(None)
    to_proc_2.put(None)
    to_proc_3.put(None)
    to_proc_4.put(None)
    while True:
        current = to_proc_1.qsize() + to_proc_2.qsize() + to_proc_3.qsize() + to_proc_4.qsize() - 4
        current_prog = '#'*(100-int(current/total*100)) + '-' * (int(current/total*100))
        current_prog = init_prog and current_prog
        #if progress_save != current_prog:
        os.system('cls')
        print('Current progress:',current_prog)
        time.sleep(5)
        #progress_save = current_prog
        if current == 0:
            break
        




if __name__ == '__main__':
    program_init_time = time.time()
    time.clock()
    freeze_support()
    to_proc_1 = Queue()
    to_proc_2 = Queue()
    to_proc_3 = Queue()
    to_proc_4 = Queue()
    p1 = Process(target=proc1, args=(to_proc_1,))
    p2 = Process(target=proc2, args=(to_proc_2,))
    p3 = Process(target=proc3, args=(to_proc_3,))
    p4 = Process(target=proc4, args=(to_proc_4,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    main(to_proc_1,to_proc_2,to_proc_3,to_proc_4)
    '''
    clear_count = 0
    
    while to_proc_1.empty() is False:
        #print("in loop")
        clear_count += 1
        try:
            #print("Frame{}:".format(clear_count),to_proc.get()[0][0][0])
            #print(to_proc.get())
            to_proc_1.get()
        except:
            continue
    while to_proc_2.empty() is False:
        #print("in loop")
        clear_count += 1
        try:
            #print("Frame{}:".format(clear_count),to_proc.get()[0][0][0])
            #print(to_proc.get())
            to_proc_2.get()
        except:
            continue
    while to_proc_3.empty() is False:
        #print("in loop")
        clear_count += 1
        try:
            #print("Frame{}:".format(clear_count),to_proc.get()[0][0][0])
            #print(to_proc.get())
            to_proc_3.get()
        except:
            continue
    '''
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    to_proc_1.close()
    to_proc_2.close()
    to_proc_3.close()
    to_proc_4.close()


    print("The system has successfully exit the program,took {}s to complete program, more accurately,{}s".format(time.time()-program_init_time,time.clock()))

    #The system has successfully exit the program,took 356.96424984931946s to complete program, more accurately,356.9712798259048s single process
    #The system has successfully exit the program,took 198.9456808567047s to complete program, more accurately,198.94337354241145s 3procs
    #The system has successfully exit the program,took 183.88620018959045s to complete program, more accurately,183.88610120612063s 4procs