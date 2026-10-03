def mostFrequent(N: int, A: list) -> list:
    freq = {}
    
    for i in A:
        freq[i] = freq.get(i,0) + 1
        
    max_freq = max(freq.values())
    
    best_elem = min(num for num,count in freq.items() if count == max_freq)
    
    return [best_elem,max_freq]
    
            