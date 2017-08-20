This is my attempt on learning few basic lossless compression algorithms and combining them to achive best compression ratio in minimum time.
I tried to make code as efficint as I could so the huffman tree is a canonical huffman tree with base 2 encoding and Burrows Wheeler Transform uses suffex array and first-last column methods.
Best combination I could come up with is in Compressor.py so use it to compress and test files.

Results (on my potato PC):
                    Ratio       Compression time(sec)     Decompression time(sec)    Orignal File Size(KB)
test1.txt ->         71%                3.5                        2.5                       593
test2.txt ->        73.5%                8                          5                        1314 
test3.txt ->         82%                25                          10                       2943

Compressor.py require tqdm but can be easily removed ,it just adds a progress bar to know how fast each stage is working.
