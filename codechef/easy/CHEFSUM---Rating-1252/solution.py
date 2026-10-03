# cook your dish here

    
t = int(input())

for b in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    min_val = float('inf')
    where = -1
    
    for i in range(n):
        if a[i] < min_val:
            min_val = a[i]
            where = i+1
            
    print(where)
    
    