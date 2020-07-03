import numpy as np


# shuffle one data(2 array:x,t) and split the data into 2 data
def shuffle_data(data_x,data_t):
    a = data_x.copy()
    b = data_t.copy()

    c = np.c_[a.reshape(len(a), -1), b.reshape(len(b), -1)]
    np.random.shuffle(c)
    a2 = c[:, :a.size//len(a)].reshape(a.shape)
    b2 = c[:, a.size//len(a):].reshape(b.shape)

    shuffle_ratio = int(0.8*len(a2))
    train_x = a2[0:shuffle_ratio]
    train_t = b2[0:shuffle_ratio]
    test_x = a2[shuffle_ratio:]
    test_t = b2[shuffle_ratio:]
    return train_x, train_t, test_x, test_t

def list_array(array_size=4):
    mat = np.empty((array_size,array_size),dtype=object)
    # print(mat)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            mat[i,j] = [0]
    print(mat.shape)
    # mat[0,0].append(1)
    # mat[0,0].append(2)
    # print(mat)
    # print(mat[0,0])
    return mat