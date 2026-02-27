def g(a,s):
    for i in range(a,s+1):
        i=i*i
        print(i)
a,s=map(int,input().split())
g(a,s)