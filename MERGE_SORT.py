arr=[100,4,3,5,6,2,3,1,6]
helper=[]

def merge(arr,helper,low,middle,high):

    helper=arr[:]

  
    helper_left=low
    current=low
    helper_right=middle+1

    while(helper_left <= middle and helper_right <= high):
        if helper[helper_left]<=helper[helper_right]:
            arr[current]= helper[helper_left]
            helper_left+=1
        else:
            arr[current] = helper[helper_right]
            helper_right+=1

        current+=1

    remianing = middle-helper_left
    for i in range(0,remianing+1):
        arr[current+i] = helper[helper_left+i]

def mergesort(arr,helper,low,high):
    if low < high:
        middle= (low+high)/2
        mergesort(arr,helper,low,middle) #left
        mergesort(arr,helper,middle+1,high) #right
        merge(arr,helper,low,middle,high)


mergesort(arr,helper,0,len(arr)-1)
print arr