n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    s=str(input())
    p=b
    for j in range(p):
        string=s[:b]
        string=string[::-1]
        s=string+s[b:]
        b -= 1
    print(s)
        