RED, WHITE, BLUE = range(3)

def dutch_flag_partition(A, pivot_index):
    pivot = A[pivot_index]
    # First pass: group smaller than pivot
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements larger than pivot
    for i in range(len(A)):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element
        # less than pivot, since first pass has moved them to the
        # start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

A = [0,0,1,2,2,1,0]
dutch_flag_partition(A, 2)
print(A)

