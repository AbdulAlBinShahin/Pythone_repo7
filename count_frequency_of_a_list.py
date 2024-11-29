def max_frequency(num):
    if not num:
        return None
    freq={}
    for i in num:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    max_freq=max(freq,key=freq.get)
    return max_freq
 
n=list(map(int,input("enter num: ").split()))
frequency=max_frequency(n)
print(frequency)
