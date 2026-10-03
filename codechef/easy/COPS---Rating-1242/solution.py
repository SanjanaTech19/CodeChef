# cook your dish her

def count_safe_houses():
    t = int(input())
    
    for i in range(t):
        m,x,y = map(int, input().split())
        cop_houses = list(map(int, input().split()))
        
        safe = [True] * 100
        
        max_dist = x * y
        
        for cop in cop_houses:
            start = max(1, cop - max_dist)
            end = min(100,cop + max_dist)
            
            for j in range(start,end+1):
                safe[j-1] = False
                
        print(sum(safe))
        
count_safe_houses()