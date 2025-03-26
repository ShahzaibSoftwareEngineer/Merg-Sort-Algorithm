def program31():
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L, R = arr[:mid], arr[mid:]
            merge_sort(L)
            merge_sort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    arr = [3, 1, 4, 1, 5]
    merge_sort(arr)
    print("Sorted array:", arr)  # [1, 1, 3, 4, 5]
