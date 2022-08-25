



def selectionSort(arr):

    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                print(arr)

    print(arr)

selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])