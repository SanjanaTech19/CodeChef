# cook your dish here
t = int(input())

for i in range(t):
    n,m = map(int, input().split())
    a = input()
    
    total_ones = a.count('1') * m
    
    if total_ones % 2 != 0:
        print(0)
    elif total_ones == 0:
        print(n * m)
        
    else:
        target = total_ones // 2
        
        count = 0
        current_ones = 0
        
        for i in range(2*n):
            if a[i % n] == '1':
                current_ones += 1
            
            # If the left side has reached our target, this is a "good spot"!
            if current_ones == target:
                count += 1
                
        print(count)
    
    
    