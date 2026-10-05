# cook your dish here
n = int(input())
a = list(map(int, input().split()))

c = 0
for i in range(1,n-1):
    if a[i]//a[i-1] == a[i+1]//a[i]:
        print(a[i-1],a[i],a[i+1])
        c+=1
        
if c==0:
    print(-1)