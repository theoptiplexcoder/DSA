def insertionSort(arr:list)->list:
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break
    return arr




if __name__=="__main__":
    elements=[72,13,34,3,23,2,4,23,1,883,7]
    print(insertionSort(elements)) 
