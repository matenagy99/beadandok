negyjegyuek=[]
palindrom=[]
for i in range(1000,10000):
    negyjegyuek.append(i)
for j in range(1000,10000):
    for k in range(len(negyjegyuek)):
        n=j*negyjegyuek[k]
        tmp=str(n)
        forditott=tmp[::-1]
        if(tmp==forditott):
                palindrom.append(n)

print(palindrom)
max=palindrom[0]
for i in palindrom:
    if i>max:
        max=i

print("{} a legnagyobb palindrom szám amely alőáll két 4-jegyű szám szorzataként.".format(max))
