import sys, os
from os.path import join

import numpy as np

import utils as u
from PIL import Image

from filtre import average_filter, average_filter_auto, gaussian_noise, simple_laplacian

MAIN = os.path.abspath(os.path.dirname(__file__))
DATA = join(MAIN, "data")
MOON = join(DATA, "moon.tif")

def main():
    
    if len(sys.argv) == 1 + 1:
        verbose = bool(int(sys.argv[1]))
    else :
        verbose = False
        
    list_img = u.get_files(DATA, ["*"])

    IMG_SELECT = list_img[0]

    img_o = np.asarray(Image.open(IMG_SELECT))
    img_moy_3_3 = average_filter_auto(img_o, (3,3))
    img_moy_5_5 = average_filter_auto(img_o, (5,5))
    filtre = np.asarray([[1, 2, 1], [2, 4, 2], [1, 2, 1]])/16
    img_moy_3_3_cent = average_filter(img_o, filtre)
    img_bruit_gauss, bruit_gauss = gaussian_noise(img_o)
    img_moy_3_3_bruit_gauss = average_filter_auto(img_bruit_gauss, (3,3))
    img_moy_5_5_bruit_gauss = average_filter_auto(img_bruit_gauss, (5,5))

    u.view_img(img_o, "[{}] Image originale".format(os.path.basename(IMG_SELECT)), 1)
    u.view_img(img_moy_3_3, "[{}] Image filtre moyenneur 3x3".format(os.path.basename(IMG_SELECT)), 2)
    u.view_img(img_moy_5_5, "[{}] Image filtre moyenneur 5x5".format(os.path.basename(IMG_SELECT)), 3)
    u.view_img(img_moy_3_3_cent, "[{}] Image filtre moyenneur 3x3 rep gauss".format(os.path.basename(IMG_SELECT)), 4)
    u.view_img(img_bruit_gauss, "[{}] Image gaussien bruité".format(os.path.basename(IMG_SELECT)), 5)
    u.view_img(bruit_gauss, "Bruit gaussien", 6)
    u.view_img(img_moy_3_3_bruit_gauss, "[{}] Image gaussien bruité".format(os.path.basename(IMG_SELECT)), 7)
    u.view_img(img_moy_5_5_bruit_gauss, "[{}] Image gaussien bruité filtré par un moyenneur 5x5".format(os.path.basename(IMG_SELECT)), 8)

    moon = np.asarray(Image.open(MOON))
    moon_lapla = simple_laplacian(moon, 4)
    moon_rehau_lapla = simple_laplacian(moon, 0)
    moon_rehau_lapla_diag = simple_laplacian(moon, 5)

    u.view_img(moon, "[{}] Moon originale".format(os.path.basename(IMG_SELECT)), 9)
    u.view_img(moon_lapla, "[{}] Moon laplacian".format(os.path.basename(IMG_SELECT)), 10)
    u.view_img(moon_rehau_lapla, "[{}] Moon laplacian rehaussé".format(os.path.basename(IMG_SELECT)), 11)
    u.view_img(moon_rehau_lapla_diag, "[{}] Moon laplacian rehaussé diag ".format(os.path.basename(IMG_SELECT)), 12)
    # u.view_img(, "[{}] Image ".format(os.path.basename(IMG_SELECT)), 13)
    # u.view_img(, "[{}] Image ".format(os.path.basename(IMG_SELECT)), 14)
    # u.view_img(, "[{}] Image ".format(os.path.basename(IMG_SELECT)), 15)
    

if __name__ == "__main__":
    main()