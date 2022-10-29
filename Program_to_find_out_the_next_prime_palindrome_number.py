def prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True    
def pail(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
a=int(input())
a+=1
while True:
    if pail(a)==a and prime(a)==True:
        print(a)
        break
    a+=1
