a=int(input())
i=1
sum=0
while i<=a:
    if a%i==0:
       sum+=i
    i+=1
if sum%a==0:
    print("True")
else:
    print("False")