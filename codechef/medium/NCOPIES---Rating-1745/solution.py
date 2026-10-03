# cook your dish here
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = input()
    
    tot = a.count('1')
    target = tot * m
    
    if target % 2 != 0:
        print(0)
    elif target == 0:
        print(n * m)
    else:
        target //= 2
        cur = 0
        
        # Skip copies of A until we are close to the target
        while m > 0:
            if cur + tot < target:
                m -= 1
                cur += tot
                continue
            else:
                break
                
        ans = 0
        # Check at most 2 copies of A after skipping
        for j in range(min(m, 2)):
            for i in range(n):
                ans += (cur == target)
                cur += (a[i] == '1')
                
        print(ans)