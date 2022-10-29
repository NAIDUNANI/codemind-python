n=int(input())
lst=list(map(int,input().split()))
es=0
for i in lst:
    if i%2==0:
        es+=i
print(es)