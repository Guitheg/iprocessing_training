import os
from matplotlib import pyplot as plt

def get_file_ext(file):
    return file.split(".")[-1]

def get_files(dirpath, ext = []):
    return [os.path.join(dirpath, file) for file in os.listdir(dirpath) 
        if get_file_ext(file) in ext or 
            ext == [] or 
            (ext == ["*"] and os.path.isfile(os.path.join(dirpath, file)))]

def view_img(img, title = "Image", figure:int=1):
    fig = plt.figure(figure)
    plt.imshow(img)
    plt.gray()
    plt.title(title)
    plt.axis('off')
    plt.show()
