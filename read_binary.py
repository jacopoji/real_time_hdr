import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as scipy


r_file = np.fromfile("0.raw",dtype='f8').reshape((1024,1024))
g_file = np.fromfile("1.raw",dtype='f8').reshape((1024,1024))
b_file = np.fromfile("2.raw",dtype='f8').reshape((1024,1024))
plt.figure(1)
plt.title("r")
plt.imshow(np.rot90(r_file),cmap="gray")
plt.figure(2)
plt.title("g")
plt.imshow(np.rot90(g_file),cmap="gray")
plt.figure(3)
plt.title("b")
plt.imshow(np.rot90(b_file),cmap="gray")
plt.show()

np.savetxt("CCRF_R.txt",r_file,fmt="%f8")
np.savetxt("CCRF_G.txt",g_file,fmt="%f8")
np.savetxt("CCRF_B.txt",b_file,fmt="%f8")