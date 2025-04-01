#def bubbleSort(arr:list):
#    size=len(arr)
#    for i in range(size):
#        for j in range(i+1,size):
#            if arr[j]<arr[i]:
#                arr[j],arr[i]=arr[i],arr[j]
#    return arr

##Time complexity O(n^2)
##Space complexity O(1)

def bubbleSort(arr:list)->list:
    n=len(arr)
    flag=True
    while flag:
        flag=False
        for i in range(1,n):
            if arr[i-1]>arr[i]:
                flag=True
                arr[i-1],arr[i]=arr[i],arr[i-1]
    return arr
if __name__=="__main__":
    elements=[72,13,34,3,23,2,4,23,1,883,7]
    print(bubbleSort(elements))
