a=[1,2,3,4]
b=[5,6,7,8]
c=[]
#adding index matched
for x in range(len(a)):
    c.append(bin(a[x]+b[x]))

print c