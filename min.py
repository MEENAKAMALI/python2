def smallest(arr,n):
    min=arr[0]
    for i in range (1,n):
        if arr[i]>min:
            min=arr[i]
    return min
arr=[10,345,56,89]
n=len(arr)
ans=smallest(arr,n)
print("answer",ans)
