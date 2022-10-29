n=int(input())
lst=list(map(int,input().split()))
c=b=0
for i in lst:
    b+=i
    a=b//n
for i in lst:
    if i==a:
        c+=1
if c!=0:
    print("True")
else:
    print("False")