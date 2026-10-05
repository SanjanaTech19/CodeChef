# ROAMA

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Rotate and Maximize

You are given an array $A$ of $N$ integers.

You may circularly rotate the array any number of positions. In a circular rotation, elements that move past one end of the array reappear at the other end.

For example, the circular rotations of `[1, 2, 3, 4]` are:

`[1, 2, 3, 4]`, `[2, 3, 4, 1]`, `[3, 4, 1, 2]`, and `[4, 1, 2, 3]`.

After choosing a rotation, its score is calculated by multiplying each element by its  **0-based index**  and adding the results.

That is, the score is:

$\displaystyle \sum_{i=0}^{N-1} i \times A_i$

where $A_i$ represents the element present at index $i$  **after the chosen rotation**.

Find the  **maximum score**  that can be obtained among all circular rotations of the array.

### Input Format

The first line contains an integer $N$ — the size of the array.

The second line contains $N$ space-separated integers $A_0,A_1,\ldots,A_{N-1}$.

### Output Format

Print a single integer — the maximum score among all circular rotations of the array.

### Constraints
- $1 \le N \le 10^5$
- $-10^9 \le A_i \le 10^9$
### Sample 1:
Input
Output

```
4
8 3 1 2
```

```
29
```

### Explanation:

The rotation `[3, 1, 2, 8]` gives:

$0\times3+1\times1+2\times2+3\times8=29$

No other circular rotation gives a greater score.

Therefore, the maximum score is `29`.

### Sample 2:
Input
Output

```
3
1 2 3
```

```
8
```

### Explanation:

For the rotation `[1, 2, 3]`, the score is:

$0\times1+1\times2+2\times3=8$

This is the maximum score among all circular rotations.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-05T11:37:03.326Z  

```py
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
```

---

[View on CodeChef](https://www.codechef.com/problems/ROAMA)