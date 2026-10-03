# cook your dish here
t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    
    for i in range(n-1,-1,-1):
        if a[i] < x:
            ans = i+1
            break
    print(ans)