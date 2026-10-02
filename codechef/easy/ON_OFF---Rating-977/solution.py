t = int(input())

while t > 0:
    n = int(input())
    s = input()
    r = input()
    
    # Count how many buttons changed their state
    changes = 0
    for i in range(n):
        if s[i] != r[i]:
            changes += 1
            
    # The bulb starts ON (1). 
    # If the number of changes is even, it stays ON (1).
    # If the number of changes is odd, it turns OFF (0).
    if changes % 2 == 0:
        print(1)
    else:
        print(0)
        
    t -= 1