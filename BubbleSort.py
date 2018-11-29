# Uses python3

def BubbleSort(a):
    """
    Time : O(N^2)
    Space : in-place
    Method : Bubbles the max element to the last of the array by comparing pair of adjacent elements in an array

    Opeartions : n - 1 + n - 2 + ... + 1 = n * (n-1) * .5
    """
    if not a :
        return a

    for i in range(0,len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] > a[j+1]:
                # Swap j and j+1 elements
                a[j],a[j+1] = a[j+1],a[j]
    return a

# BubbleSort([8,4,2,5,2,12,4,5,2,0,12,52,2])
