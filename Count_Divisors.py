a,b,x=map(int,input().split())
count=0
while a<=b:
    if a%x==0:
        count+=1
    a+=1
print(count)