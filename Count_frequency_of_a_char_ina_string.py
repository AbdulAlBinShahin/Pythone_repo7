def count_freq(s):
    fre={}
    for char in s:
        if char!=' ':
            if char in fre:
                fre[char]+=1
            else:
                fre[char]=1
    return fre
 
string=input("enter string: ")
cf=count_freq(string)
print(cf)
