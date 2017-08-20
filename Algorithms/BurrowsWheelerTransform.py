#input: byte string
#encoded_output: ascii list

import timeit
from itertools import groupby
from operator import itemgetter


def suffix_array(text, _step=16):
    """
    #copied from
    #https://stackoverflow.com/questions/13560037/effcient-way-to-find-longest-duplicate-string-for-python-from-programming-pearl/13693834#13693834
    #thanks to hynekcer and his improved implementation of Adrian Vladu and Cosmin Negruşeri Algo
    #cs97si.stanford.edu/suffix-array.pdf
    Arguments:
        text:  The text to be analyzed.
        _step: Is only for optimization and testing. It is the optimal length
               of substrings used for initial pre-sorting. The bigger value is
               faster if there is enough memory. Memory requirements are
               approximately (estimate for 32 bit Python 3.3):
                   len(text) * (29 + (_size + 20 if _size > 2 else 0)) + 1MB

    Return value:      (tuple)
      (sa, rsa)
        sa:  Suffix array                  for i in range(1, size):
               assert text[sa[i-1]:] < text[sa[i]:]
        rsa: Reverse suffix array          for i in range(size):
               assert rsa[sa[i]] == i
     suffix_array(text='banana')
    ([5, 3, 1, 0, 4, 2], [3, 2, 5, 1, 4, 0])

    """
    tx = text
    size = len(tx)
    step = min(max(_step, 1), len(tx)) # so that if str len <16
    sa = list(range(size))
    # list of suffix array max size of char used while sorting = steps
    sa.sort(key=lambda i: tx[i:i + step])
    # It helps to skip yet resolved values. The last value True is a sentinel.
    grpstart = size * [False] + [True]  # a boolean map for iteration speedup.
    rsa = size * [None]
    stgrp, igrp = '', 0
    for i, pos in enumerate(sa): #enumerate(sa) = sa[i]
        st = tx[pos:pos + step]
        if st != stgrp:
            grpstart[igrp] = (igrp < i - 1)
            stgrp = st
            igrp = i
        rsa[pos] = igrp
        sa[i] = pos
    grpstart[igrp] = (igrp < size - 1 or size == 0)
    while grpstart.index(True) < size:
        # assert step <= size
        nextgr = grpstart.index(True)
        while nextgr < size:
            igrp = nextgr
            nextgr = grpstart.index(True, igrp + 1)
            glist = []
            for ig in range(igrp, nextgr):
                pos = sa[ig]
                if rsa[pos] != igrp:
                    break
                newgr = rsa[pos + step] if pos + step < size else -1
                glist.append((newgr, pos))
            glist.sort()
            for ig, g in groupby(glist, key=itemgetter(0)):
                g = [x[1] for x in g]
                sa[igrp:igrp + len(g)] = g
                grpstart[igrp] = (len(g) > 1)
                for pos in g:
                    rsa[pos] = igrp
                igrp += len(g)
        step *= 2
    del grpstart
    return sa

#create bwt code based on its suffix array
def bwt_sa(text):
    assert b'\x03' not in text
    data = text+b'\x03'
    #coding = ''
    coding = []
    #create suffix array Naive way
    #sa=sorted([(data[i:],i) for i in range(len(data))])
    #sa= [i[1] for i in sa]
    sa = suffix_array(data)
    def value():
        for x in sa:
            if x==0:
               t= b'\x03'
            else:
                t=bytes([data[x-1]])
            yield t
    return b''.join(value())

#repeatedly permutes a list of our strings (by sorting them),the permutation is exactly the same at each step
#BNN$AAA -> 0123456 -> (sort)
#$AAABNN -> 3456123 -> ABNN$AA
#ABNN$AA -> 0123456 -> (sort)
#$AAABNN -> 4560123 <ittratte through pos on BNN$AAA(data) ,start from key
#ie '$' + 0th place = 'B' + 4th place = 'A' + 1st place = 'N'  ....
#we get $BANANA
def inverse_bwt( data):
    key = data.index(ord(b'\x03'))
    #generator
    def row(key):
        #enumerate = each element + index
        permutation = sorted((t, i) for i, t in enumerate(data))
        #_ means no need of variable
        for _ in data:
            t, key = permutation[key]
            #Yield is a keyword that is used like return, except the function will return a generator.
            yield t
    #list conversion loses advantage of generator
    return list(row(key))[:-1]

"""
def bwt(data):
    #data = data + '$'
    key = 0
    coding =''
    heap = []
    dataLen = len(data)
    for i in range(dataLen):
        data = data[1:] +data[0]
        heappush(heap, data)

    for i in range(dataLen):
        #for heap sort
        heaptop = heappop(heap)
        coding = coding + heaptop[-1:]
        if heaptop == data:
            key =  i
    return coding,key
"""
"""
#simplest way of doing it
def simple_inverse_bwt(data,key):
    mylist =[]
    dataLen=len(data)
    for j in range(dataLen):
        mylist.append('')
    for i in range(dataLen):
        for j in range(dataLen):
            mylist[j] = data[j] + mylist[j]
        mylist.sort()
    return mylist[key]
"""
"""
def rankBwt(bw):
    ''' Given BWT string bw, return parallel list of B-ranks.  Also
        returns tots: map from character to # times it appears. '''
    tots = dict()
    ranks = []
    for c in bw:
        if c not in tots: tots[c] = 0
        ranks.append(tots[c])
        tots[c] += 1
    return ranks, tots
def firstCol(tots):
    ''' Return map from character to the range of rows prefixed by
        the character. '''
    first = {}
    totc = 0
    for c, count in sorted(tots.items()):
        first[c] = (totc, totc + count)
        totc += count
    return first
    
#based on first and last row to get sequence
#because of creation of duplicate of data whith huge numbers this takes time
def reverse_bwt(bw):
    ''' Make T from BWT(T) '''
    ranks, tots = rankBwt(bw)
    first = firstCol(tots)
    rowi = 0 # start in first row
    t = b'\xff' # start with rightmost character
    while bw[rowi] != b'\xff':
        c = bw[rowi]
        t = c + t # prepend to answer
        # jump to row that starts with c of same rank
        rowi = first[c][0] + ranks[rowi]
    t=t[:-1]
    return t
"""


#For Testing
if __name__=="__main__":
    yay = b'BANANA'
    numstr9999=b'1101001010011001000000000000000000001111110101011111'
    start_time = timeit.default_timer()
    data = bwt_sa(yay)
    print(data)

    stopt_time = timeit.default_timer()
    print(stopt_time - start_time)


    start_time = timeit.default_timer()
    data = inverse_bwt(data)#,key)
    print(list(map(chr,data)))
    stopt_time = timeit.default_timer()
    print(stopt_time - start_time)
