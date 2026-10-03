# CNDY - Rating 1180

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-10-03T04:17:33.772Z  

```py
def mostFrequent(N: int, A: list) -> list:
    freq = {}
    
    for i in A:
        freq[i] = freq.get(i,0) + 1
        
    max_freq = max(freq.values())
    
    best_elem = min(num for num,count in freq.items() if count == max_freq)
    
    return [best_elem , max_freq]
            
```

---

[View on CodeChef](https://www.codechef.com/problems/CNDY)