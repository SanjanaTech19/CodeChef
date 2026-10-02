def findLargestOddSubstring(num):
    # write your code here...
    
    for i in range(len(num) -1 , -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i+1]
    return -1