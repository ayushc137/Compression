This is my attempt on learning few basic lossless compression algorithms and combining them to achive best compression ratio in minimum time.
I tried to make code as efficint as I could so the huffman tree is a canonical huffman tree with base 2 encoding and Burrows Wheeler Transform uses suffex array and first-last column methods.
Best combination I could come up with is in Compressor.py so use it to compress and test files.

Results (on my potato PC):


File Name -> Ratio , Compression time , Decompression time , Orignal File Size:
					
					
test1.txt ->         71% , 3.5s , 2.5s , 593 KB


test2.txt ->        73.5% , 8s  , 5s , 1314 KB


test3.txt ->         82% , 25s  , 10s , 2943 KB



Compressor.py require tqdm but can be easily removed ,it just adds a progress bar to know how fast each stage is working.
