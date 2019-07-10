str="bcdecf"
count = 0
'''
count =0
for x in range(len(str)-1):
    for y in range (x+1,len(str)):
        if str[x] == str[y]:
            count = count + 1
            break;
        else:
            continue

'''

#using array

str_arr=[]
for x in str:
    if x in str_arr:
        count = count +1
        break
    else:
        str_arr.append(x)
        continue

if count == 0:
    print "Not"
else:
    print "found"

