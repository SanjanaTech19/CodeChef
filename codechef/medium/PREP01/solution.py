# cook your dish here
t = int(input())

for i in range(t):
    n = int(input())
    
    row = []
    current = 1
    
    for k in range(n):
        row.append(str(current))
        
        if k < n-1:
            current = current * (n-1-k) // (k+1)
            
    print(" ".join(row))