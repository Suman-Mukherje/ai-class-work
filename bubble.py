#Bubble Sort in python

def bubblesort(arr):
    swapped = False

    for i in range (len(arr)-1):

        for j in range (len(arr)-i-1):

            if arr[j]>arr[j+1]:
                swapped = True

                a=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=a

        if swapped == False:
            return

    return arr

a=[2,9,1,-2,0,23,78,6]
print("Original array: ",a)
print('Sorted array:',bubblesort(a))
