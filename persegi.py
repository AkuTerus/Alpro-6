def persegi(p,l):
    n = p*l
    for i in range(n):
        # print(i)
        print(i+1,end=' ')
        if (i+1)% l==0:
            print()

persegi(5, 4)