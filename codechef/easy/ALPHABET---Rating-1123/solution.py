# cook your dish here
s = input()
n = int(input())

for i in range(n):
    w = input()
    
    can_read = True
    
    for i in w:
        if i not in s:
            can_read = False
    
    if can_read == True:
        print('Yes')
    else:
        print('No')
        
        