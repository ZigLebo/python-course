def selectionsort(A):
    for i in range(len(A)):
        min_val=A[i]
        min_ind=i
        for j in range(i+1,len(A)):
            if A[j]<min_val:
                min_val=A[j]
                min_ind=j
        A[i],A[min_ind]=A[min_ind],A[i]
    return A
