# Uses python3

def SelectionSort(a):
    """
    Time : O(N^2)
    Space : in-place
    Method : Finds min on each scan of the array and swaps it with the first element
    Opeartions : n - 1 + n - 2 + ... + 1 = n * (n-1) * .5
    """
    if not a :
        return a

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j] <= a[i]:
                # Swaps with the ith element
                a[j],a[i] = a[i],a[j]
    return a


# SelectionSort([8,4,2,5,2,12,4,5,2,0,12,52,2])
