import random
import numpy as np
from PIL import Image
import math
import difflib


def get_data( infilename ,width, height,color) :
    #data = list(img.getdata())
    #r ,g, b = img.getpixel((1, 1))
    #try:
    #data = np.asarray(img, dtype='uint8')
    #except SystemError:
    #data = np.asarray(img.getdata(), dtype='uint8')
    if(color == 'r'):
        col = 0
    elif (color == 'g'):
        col = 1
    elif (color == 'b'):
        col = 2
    data = []
    pix = infilename.load()
    for i in range(0, width):
        for j in range(0, height):
            data.append(pix[i, j][col]) #((i, j))[0])

    return data


def save_image( outfilename,width, height, redArr,greenArr,blueArr ) :
    """
    outimg = Image.fromarray(npdata, "RGB")
    outimg.save(outfilename)
    outimg.show()
    """
    new_img = Image.new("RGB", (width, height), "white")
    pix = new_img.load()
    count = 0
    for i in range(0, width):
        for j in range(0, height):
            pix[i, j] = (redArr[count],greenArr[count],blueArr[count])
            count +=1
    new_img.save(outfilename)
    return new_img

#Linear congruential generator 
def lcg(n, m, seed):
    #m,a,c is defined by language
    #c++ m=2**32,a=11695477
    a=11695477
    c=1
    sequence = []
    Xn = seed
    for i in range(n):
        Xn = (a*Xn + c) % m
        sequence.append(Xn)
    return(sequence)


def levenshtein(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]

def compress(data) :
    vl= len(data)
    bestDist =  0
    bestSeed=0
    for i in range(2**vl):
        print(str(i) +'/'+str(2**vl) +'\n')
        testList = lcg(vl, 255, i)
        #distance = levenshtein(data,testList)
        distance = difflib.SequenceMatcher(None, data, testList)
        distance =  distance.ratio()
        if(distance> bestDist):
            print('Improvemnet!' + str(bestDist))
            bestDist=distance
            bestSeed = i
    return bestSeed

def decompress(seed,length) :
    data = lcg(length, 255, seed)
    return data

img = Image.open("mario.png", 'r')
width, height = img.size

data_r = get_data(img,width, height,'r')
data_g = get_data(img,width, height,'g')
data_b = get_data(img,width, height,'b')
print('Got Data!')

arrlenth = len(data_r) #width*height
seed_r=compress(data_r)
seed_g=compress(data_r)
seed_b=compress(data_r)
print('Compressed!')

file=open("Mario.pic", "a+")
#width height R G B
file.write(str(width) +' '+str(width)  +' '+str(seed_r) +' '+str(seed_g) +' '+str(seed_b) +' ')
file.close()
print('File made!')

new_data_r = decompress(seed_r,arrlenth)
new_data_g = decompress(seed_g,arrlenth)
new_data_b = decompress(seed_b,arrlenth)
print('Decompressed!')

pic = save_image("yay.jpg",width, height,new_data_r,new_data_g,new_data_b)
print('Done!')
pic.show()


