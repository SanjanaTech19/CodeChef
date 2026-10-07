# cook your dish here
# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    # Check if any element appears more than twice
    if max(a.count(x) for x in a) <= 2:
        print('Yes')
    else:
        print('No')