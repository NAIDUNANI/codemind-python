n=int(input())
lst=list(map(int,input().split()))
es=0
for i in range(len(lst)):
    if i%2==0:
        es+=lst[i]
print(es)