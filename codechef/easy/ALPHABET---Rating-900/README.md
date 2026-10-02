# ALPHABET - Rating 900

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-02T14:49:25.047Z  

```py
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
```

---

[View on CodeChef](https://www.codechef.com/problems/ALPHABET)