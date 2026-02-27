def ff(a):
    for i in range(a+1):
        if i%3==0 and i%4==0:
            yield i
a=int(input())
for i in ff(a):
    print(i,end=' ')