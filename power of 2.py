def power(n):
    print ("n{}".format(n))
    if n < 1:
        return 0
    elif n ==1:
        print 1
        return 1
    else:
        pre=power(n/2)
        print ("Pre{}".format(pre))
        print "\n"
        cur=pre*2
        print ("cur{}".format(cur))
        return cur

x=power(50)
print ("x{}".format(x))