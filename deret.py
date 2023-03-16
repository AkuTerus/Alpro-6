def deretBilagan(n):
    for i in range(n,0,-1):
        temp = 1

        for j in range(1,i+1):
            temp = temp*j
        print(temp,end=' ')

        for j in range(i,0,-1):
            print(j,end=' ')
        print()

deretBilagan(6)