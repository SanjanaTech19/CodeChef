# cook your dish here

t = int(input())
for x in range(t):
    s = input()
    
    amb = 0
    brass = 0
    
    for i in s:
        if i == 'a':
            amb += 1
        else:
            brass += 1
    
    print(min(amb,brass))