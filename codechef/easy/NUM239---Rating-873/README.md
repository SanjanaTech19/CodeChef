# NUM239 - Rating 873

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Counting Pretty Numbers

Vasya likes the number $239$. Therefore, he considers a number  *pretty*  if its last digit is $2$, $3$ or $9$.

Vasya wants to watch the numbers between $L$ and $R$ (both inclusive), so he asked you to determine how many pretty numbers are in this range. Can you help him?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.
### Output

For each test case, print a single line containing one integer — the number of pretty numbers between $L$ and $R$.

### Constraints
- $1 \le T \le 100$
- $1 \le L \le R \le 10^5$
### Subtasks

 **Subtask #1 (100 points):**  original constraints

### Sample 1:
Input
Output

```
2
1 10
11 33
```

```
3
8
```

### Explanation:

 **Example case 1:**  The pretty numbers between $1$ and $10$ are $2$, $3$ and $9$.

 **Example case 2:**  The pretty numbers between $11$ and $33$ are $12$, $13$, $19$, $22$, $23$, $29$, $32$ and $33$.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T15:46:39.955Z  

```py
# cook your dish here
t = int(input())
for i in range(t):
    l,r = map(int, input().split())
    count = 0
    for num in range(l,r+1):
        if num % 10 == 2 or num % 10==3 or num % 10== 9:
            count +=1
    print(count)
```

---

[View on CodeChef](https://www.codechef.com/problems/NUM239)