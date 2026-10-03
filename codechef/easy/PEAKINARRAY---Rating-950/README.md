# PEAKINARRAY - Rating 950

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

### Find the peak elements in an array

Given an array `A` of size `N`, your task is to find and print all the peak elements in the array. A peak element is one that is strictly greater than its neighboring elements. For the first and last elements, only consider their single adjacent element.

If no peak element exists in the array, print `-1`.

### Input Format
- The first line contains the integer $N$ — the size of array
- The second line contains all the elements of array $A$
### Output Format

Output all the peak elements in the array in the order they are present in the original array.

### Constraints
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
### Sample 1:
Input
Output

```
5
1 2 4 3 1
```

```
4
```

### Explanation:

1 is smaller than it's adjacent element 2.
2 is greater than 1 but smaller than 4.
4 is greater than both 2 and 3, thus it is a  **peak**  element.
Again 3 and 1 are also smaller than their adjacent elements.
Thus the output is only 4.

### Sample 2:
Input
Output

```
5
7 3 5 2 10
```

```
7 5 10
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T10:14:12.714Z  

```py
'''def findPeaks(A, n):
    hasPeak = False

    for i in range(n):
        if (i == 0 or A[i] > A[i - 1]) and (i == n - 1 or A[i] > A[i + 1]):
            print(A[i], end=" ")
            hasPeak = True

    if not hasPeak:
        print(-1)

'''
def findPeaks(A,n):
    
    peaks = []
    
    for i in range(1,n-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(str(A[i]))
    
    if len(peaks) == 0:
        print(-1)
    else:
        print(" ".join(peaks))
```

---

[View on CodeChef](https://www.codechef.com/problems/PEAKINARRAY)