katok =['다현', '정연', '쯔위', '사나', '지효']

def delete_data(poision):
    klen = len(katok)
    katok[poision]=None
    for i in range(poision+1, klen,1) :
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[klen-1])
delete_data(1)
print(katok)
delete_data(3)
print(katok)


