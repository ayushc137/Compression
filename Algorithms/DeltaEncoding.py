#input: list of numbers
#encoded_output: list of subtracted numbers , sign list

def deltaEncoding(data):
    sign=[]
    for i in reversed(range(1,len(data))):
        data[i] = data[i]-data[i-1]
        if (data[i]<0):
            sign.append(1)
            data[i]= abs(data[i])
        else:
            sign.append(0)
    #for first char
    sign.reverse()
    return data,sign

def deltDecoding(data,sign):
    for i in range(1,len(data)):
        if(sign[i-1]==0):
            data[i] = data[i-1]+data[i]
        else:
            data[i] = data[i-1]-data[i]
    return data

#For Testing
if __name__=="__main__":
    indata=[5,1,2,3,4,5,6]
    encode,sign = deltaEncoding(indata)
    print(encode,sign)
    print(deltDecoding(encode,sign))