def merge(left, right):
    """
    Performs the array merge step

    :param: left array
            right array

    Returns - merged_array - array
    """

    left_index = right_index = 0
    # O(N) extra space
    merged_array = list()
    while(left_index < len(left) and right_index < len(right)):

        if(left[left_index] < right[right_index]):
            merged_array.append(left[left_index])
            left_index += 1
        else:
            merged_array.append(right[right_index])
            right_index += 1
    # for the remaining elements
    merged_array.extend(left[left_index:])
    merged_array.extend(right[right_index:])
    return merged_array


def mergeSort(arr):
    # Time : O ( N log N )
    # Space : O(N)
    # Recurrence relation : T(n) = 2 * T(n/2) + O(n) : O(n) is merge work , n/2 is the number of partitions , 2 is the number
    # of sub-problems
    # Base case:
    if len(arr) == 1:
        return arr
    mid = int(len(arr) / 2)
    left, right = mergeSort(arr[:mid]), mergeSort(arr[mid:])
    return merge(left, right)
