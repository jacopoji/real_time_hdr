import numpy as np

def sigmaF1(comparasum):
    sigma = np.zeros((2,))
    sum_col = np.zeros((2,))
    cdf_col = np.zeros((2,2))
    sum_col_tmp = 0
    Q1 = np.zeros((2,))
    Q3 = np.zeros((2,))
    result_Q1 = np.zeros((2,))
    result_Q3 = np.zeros((2,))
    IQR = np.zeros((2,))
    # create cdf_col
    for i in range(2):
        for j in range(2):
            sum_col_tmp += comparasum[j][i]
            cdf_col[j][i] = sum_col_tmp
        sum_col_tmp = 0
    np.savetxt('cdf_col.txt',cdf_col,fmt="%d")
    for i in range(2):
        sum_col[i] = np.sum(comparasum[:,i])
        Q1[i] = (sum_col[i])*0.25
        Q3[i] = (sum_col[i])*0.75

        for j in range(2):
            if (Q1[i] == cdf_col[j][i]):
                result_Q1[i] = j
                break
            if (Q1[i] > cdf_col[j][i] and Q1[i] < cdf_col[j+1][i] ):
                result_Q1[i] = j + (Q1[i]-cdf_col[j][i])/(cdf_col[j+1][i] - cdf_col[j][i])
                break
        for j in range(2):
            if (Q3[i] == cdf_col[j][i]):
                result_Q3[i] = j
                break
            if (Q3[i] > cdf_col[j][i] and Q3[i] < cdf_col[j+1][i]):
                result_Q3[i] = j + (Q3[i]-cdf_col[j][i])/(cdf_col[j+1][i] - cdf_col[j][i])
                break

    IQR = result_Q3 - result_Q1
    IQR = np.divide(IQR,1.349)
    #if (Q1.all()<7) or (Q3.all()>248):
    #    print("Triggered nest")
    #    IQR= IQR * 2
    #print(IQR)
    sigma = IQR
    return sigma

if __name__ == '__main__':
    a = np.array([[1, 2], [3, 4]],dtype = np.float64)
    print(sigmaF1(a))
    print(np.std(a,dtype = np.float64,axis=1))