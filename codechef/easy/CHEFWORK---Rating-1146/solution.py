n = int(input())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

# Initialize the minimum costs with infinity
at = float('inf')   # Minimum cost for an author
tr = float('inf')   # Minimum cost for a translator
attr = float('inf') # Minimum cost for an author-translator

# Iterate through the workers and find the minimum costs for each type
for i in range(n):
    if t[i] == 1:
        tr = min(tr, c[i])
    elif t[i] == 2:
        at = min(at, c[i])
    else:
        attr = min(attr, c[i])

# The result is the minimum of (cheapest translator + cheapest author) and (cheapest author-translator)
print(min(tr + at, attr))