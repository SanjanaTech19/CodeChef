# cook your dish here
t = int(input())

for i in range(t):
    s = input().split()
    
    title_case = []
    
    for i in s:
        if i.isupper():
            title_case.append(i)
            
        else:
            title_case.append(i.capitalize())
    print(" ".join(title_case))