n=int(input())
lst=list(map(int,input().split()))
es=os=0
for i in lst:
    if i%2==0:
        es+=i
    else:
        os+=i
a=((os+es)/n)
print("{:.2f}".format(a))