t = int(input())

for i in range(t):
    s = input()
    n = len(s)
    is_valid = True
    
    for i in range(0,n,2):
        if s[i] == s[i+1]:
            is_valid = False
            break
        
    if is_valid == True:
        print('yes')
    else:
        print('no')
            