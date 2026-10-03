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