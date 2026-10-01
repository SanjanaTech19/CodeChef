t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    t -= 1
    
    x = int(s[0:2])
    y = int(s[3:5])
    
    if x<= 12 and y<=12:
        print('BOTH')
    elif x >= 12:
        print("DD/MM/YYYY")
    elif y >=12 :
        print("MM/DD/YYYY")