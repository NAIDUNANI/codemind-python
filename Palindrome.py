n=int(input())
m=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==m:
    print("True")
else:
    print("False")