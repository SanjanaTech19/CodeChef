# cook your dish here
s = input()

a = ""
for i in s:
    if i.isalpha():
        a += i.lower()

max = 0
best = "a"

for i in range(26):
    current = chr(ord('a')+i)
    
    freq = a.count(current)
    
    if freq > max:
        max = freq
        best = current
        
print(best)