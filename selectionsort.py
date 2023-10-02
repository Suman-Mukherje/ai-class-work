#Selection Sort in Python

def selectionsort(arr):
    size=len(arr)
    for i in range(size):
        mid=i

        for j in range(i+1,size):

            if arr[j]<arr[mid]:
                mid=j


        a=arr[i]
        arr[i]=arr[mid]
        arr[mid]=a


    return arr

q=[100,23,9,200,34,-23,80,56]
print("Original array is",q)
print("After sorting array is",selectionsort(q))
