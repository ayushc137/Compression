
import numpy as np
from PIL import Image
import math
from decimal import *


def get_data( infilename ,width, height,color) :
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
    new_img = Image.new("RGB", (width, height), "white")
    pix = new_img.load()
    count = 0
    for i in range(0, width):
        for j in range(0, height):
            pix[i, j] = (redArr[count],greenArr[count],blueArr[count])
            count +=1
    new_img.save(outfilename)
    return new_img


def compress(data) :
    numStr = ''.join("{0:03}".format(x) for x in data) #or "%03d" % x
    #print(numStr)
    num = int(numStr)
    """
    realNum = num
    subtracted=0
    seed =0
    #seed =  Decimal(math.sqrt(num))
    #print(seed)
    count =0
    add=0
    sequece = []
    print(num)
    get_bin = lambda x: format(x, 'b')
    bin = get_bin(num)
    print(bin)

    
    #f*** this is binary conversion
    while((float(num).is_integer() or float(num - 0.5).is_integer()) and num>0.5):

        num = int(num) / 2
        #print(str(num) + '\n')
        count += 1

        if not(float(num).is_integer()):
            sequece.append(1)
        else:
            sequece.append(0)

    #print(count)
    #print(add)
    #sequece = list(reversed(sequece))
    print(list(reversed(sequece)))
    ans=0
    for i in reversed(range(len(sequece))):
        if (sequece[i] == 1):
            #print(sequece[i])
            ans+=0.5
        #print(str(ans) + '\n')
        ans = ans*2


    #add =  ans-realNum
    print(ans)
    numStr = ''.join(str(x) for x in list(reversed(sequece)))  # or "%03d" % x
    print(int(numStr, 2))

    #print(add)
    
    #sqrt (308)
   
    for i in reversed(range(int(numStr))):
        seed = math.log(num, 2)
        print(seed)
        #print(num)
        if seed.is_integer():
            break
        else:
            subtracted+=1
            num-=subtracted
            print(num)
    """
    numStr = ''.join("{0:03}".format(x) for x in data)  # or "%03d" % x
    num =81271231201181201221241201161201311371361401481391461531501401288108308508909109509910210310711211511511310910711010910810811011311711811211712112612612311811410410711311711611310910612
    lenght = len(str(num))
    num= Decimal(num)
    print(num)
    getcontext().prec = lenght+4# set the precision  (no. of digits)
    #getcontext().rounding = ROUND_DOWN  # this will effectively truncate
    #Decimal(num).ln()/ Decimal(2).ln()
    logA = Decimal(num).ln()
    print(logA)
    #seed =  2**(Decimal(num).ln() / Decimal(2).ln())
    seed = Decimal(logA).exp()
    #seedfrac = Decimal(logA - int(logA))
    #nonfrac = 2**int(logA)
    #frac = Decimal(2**seedfrac)
    #print(Decimal(frac*nonfrac))
    print(int(seed))
    #nonfrac = 2**int(seed)
    #frac = 2**seedfrac
    #

    #return seed

def decompress() :

    return


img = Image.open("Monalisa256x256.jpg", 'r')
width, height = img.size

data_r = get_data(img,width, height,'r')
seed_r=compress(data_r)
"""
data_g = get_data(img,width, height,'g')
data_b = get_data(img,width, height,'b')
print('Got Data!')
file = open("Mario.pic", "a+")
# width height R G B
numStr = ''.join("{0:03}".format(x) for x in data_r)
file.write(numStr)
file.write('\n')
numStr = ''.join("{0:03}".format(x) for x in data_g)
file.write(numStr)
file.write('\n')
numStr = ''.join("{0:03}".format(x) for x in data_b)
file.write(numStr)
file.close()
arrlenth = width*height



seed_g=compress(data_r)
seed_b=compress(data_r)
print('Compressed!')

file=open("Mario.pic", "a+")
#width height R G B
file.write(str(width) +'\n'+str(width)  +'\n'+str(seed_r) +'\n'+str(seed_g) +'\n'+str(seed_b))
file.close()
print('File made!')

new_data_r = decompress(seed_r,arrlenth)
new_data_g = decompress(seed_g,arrlenth)
new_data_b = decompress(seed_b,arrlenth)
print('Decompressed!')

pic = save_image("yay.jpg",width, height,new_data_r,new_data_g,new_data_b)
print('Done!')
pic.show()
"""

