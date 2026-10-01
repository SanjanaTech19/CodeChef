# cook your dish here
s = input().strip()

pair_count = {}

for i in range(len(s)-1):
    pair = s[i:i+2]
    
    pair_count[pair] = pair_count.get(pair,0) +1
    
repeating_pairs = 0

for count in pair_count.values():
    if count > 1:
        repeating_pairs += 1
print(repeating_pairs)