# cook your dish here
n,k = map(int, input().split())

a = list(map(int, input().split()))

sum = 0

for i in range(n):
    if i %2 == 0:
        if a[i] > (2*k):
            sum += a[i]
            
if sum == 0:
    print(0)
else:
    print(sum)