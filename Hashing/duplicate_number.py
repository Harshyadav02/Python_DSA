def dupli(arr):

    for i in arr:
        if arr.count(i) > 1:
            return i
print(dupli(arr= [1,2,3,4,5,2]))
