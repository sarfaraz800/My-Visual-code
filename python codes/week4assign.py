import random
def frequency(l):
    count=0
    visited=[]
    dictionary={}
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] in visited:
                continue
            if l[i]==l[j]:
                count=count+1
        if l[i] in visited:
            continue
        else:        
            dictionary[l[i]]=count 
        count=0
        visited.append(l[i])

    #print(dictionary)

    max=0
    min=9999999
    for v in dictionary.values():
        if v >= max:
            max=v
        if v <= min:
            min=v    

    print(min)
    print(max) 

    maxfreqlist=[]
    minfreqlist=[]
    for k in sorted(dictionary.keys()):
        if dictionary[k]==max:
            maxfreqlist.append(k)
        if dictionary[k]==min:
            minfreqlist.append(k)    

    #print(minfreqlist)
    #print(maxfreqlist)  
    return(minfreqlist,maxfreqlist)     

l=[]
for i in range(10):
    l.append(random.randint(1,50))
print(l)    
print(frequency(l))