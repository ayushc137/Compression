

from  MovetoFrontEncoding import mtfEncoding,mtfDecoding
from BurrowsWheelerTransform import inverse_bwt,bwt_sa
from Huffman import huffmanEncode,huffmanDecode
from LZ77 import LZ_compress
import timeit
import gzip
import lzma
import zlib
import bz2
from tqdm import tqdm



def compress(inputFile,bitFile) :

    pbar = tqdm(total=100)

    with open(inputFile, 'rb') as f:
        charData = f.read()
    orignalSize = len(charData) * 8
    pbar.update(20)


    data = bwt_sa(charData)
    pbar.update(30)

    encode = mtfEncoding(data)
    pbar.update(20)

    bitString = huffmanEncode(encode)
    pbar.update(20)

    bitString += '1'
    bitLength = len(bitString)
    rem = 8-(bitLength%8)
    if rem !=0 :
        bitString += '0'*rem
        bitLength += rem

    TextV = bytes([int(bitString[i:i + 8], 2) for i in range(0, bitLength, 8)])

    pythonCompression = lzma.compress(TextV)

    pbar.update(20)
    with open(bitFile, 'wb') as f:
        f.write(pythonCompression)

    print(str(((orignalSize - len(pythonCompression)* 8) / orignalSize) * 100) + '% compression !')

    pbar.close()




def decompress(bitFile , outputFile) :
    pbar = tqdm(total=100)
    with open(bitFile, 'rb') as f:
        TextVBin = f.read()
    pythonDecompression = lzma.decompress(TextVBin)
    pbar.update(20)
    TextVBin = ''.join('{:08b}'.format(x) for x in bytes(pythonDecompression))
    TextVBin = TextVBin.rsplit('1', 1)[0]
    pbar.update(20)

    encode =  huffmanDecode(TextVBin)
    pbar.update(30)

    data = mtfDecoding(encode)
    pbar.update(20)

    decompressedData = inverse_bwt(data)
    pbar.update(40)

    decompressedData=bytes(decompressedData)
    with open(outputFile,'wb') as f:
        f.write(decompressedData)

    print('Decompressed!')
    pbar.close()






if __name__=="__main__":

    #start_time = timeit.default_timer()
    compress('test1.txt', 'output.bit')
    #stopt_time = timeit.default_timer()
    #print(stopt_time - start_time)

    #start_time = timeit.default_timer()
    decompress('output.bit','decompressed.txt')
    #stopt_time = timeit.default_timer()
    #print(stopt_time - start_time)
