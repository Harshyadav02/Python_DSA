def min_height(arr,k,n):
    
    arr.sort()
    diff = arr[n-1] - arr[0]

    for i in range(1,n):
        if arr[i] < 0:
            continue
        max1 = max(arr[n-1]-k , arr[i-1]+k)
        min1 = min(arr[0]+k , arr[i]-k)

        diff = min(diff, max1 - min1)
    return diff
arr = [8, 1, 5, 4, 7, 5, 7, 9, 4, 6]  



print("The minimum height of the tower is : ",min_height(arr,5,10))