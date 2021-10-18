n=int(input())
i=1
while i<=n:
    #TODO
    #print data
    j=1
    while j<=n:
        if j==i:
            print("*",end="")
        else:
            print("0",end="")
        j=j+1
    print("*",end="")
    p=j-1
    while p>=1:
        if p==i:
            print("*",end="")
        else:
            print("0",end="")
        p=p-1
    print()
    i=i+1
