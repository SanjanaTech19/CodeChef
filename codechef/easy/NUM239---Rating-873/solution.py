# cook your dish here
t = int(input())
for i in range(t):
    l,r = map(int, input().split())
    count = 0
    for num in range(l,r+1):
        if num % 10 == 2 or num % 10==3 or num % 10== 9:
            count +=1
    print(count)