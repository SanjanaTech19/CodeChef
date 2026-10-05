# cook your dish here
n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)

cur_score = sum(i+a[i] for i in range(n))
max_score = cur_score

for k in range(1,n):
    cur_score = cur_score - total_sum + n*a[k-1]
    if cur_score > max_score:
        max_score = cur_score
print(max_score)