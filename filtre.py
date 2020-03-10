from scipy.signal import convolve2d
import numpy as np

def average_filter_auto(img, filter_size = (2,2)):
    filtre = np.zeros(filter_size)+(1/filter_size[0]*filter_size[1])
    return convolve2d(img, filtre)

def average_filter(img, filtre):
    return convolve2d(img, filtre)

def gaussian_noise(img, u = 0, s = 10):
    rand = np.random.normal(0, 10, img.shape)
    return img+rand, rand

def simple_laplacian(img, v = 0):
    filtres = [np.asarray([[0,-1,0],[-1,5,-1],[0,-1,0]])]
    filtres.append(np.asarray([[0,1,0],[1,-4,1],[0,1,0]]))
    filtres.append(np.asarray([[1,1,1],[1,-8,1],[1,1,1]]))
    filtres.append(np.asarray([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]))
    filtres.append(np.asarray([[0,-1,0],[-1,4,-1],[0,-1,0]]))
    filtres.append(np.asarray([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]))
    filtre = filtres[v]
    return convolve2d(img, filtre)