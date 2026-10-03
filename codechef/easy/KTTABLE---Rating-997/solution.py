# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    count = 0
    prev = 0
    
    for j in range(n):
        
        available = a[j] - prev
        
        if available >= b[j]:
            count +=1
            
        prev = a[j]
            
    print(count)