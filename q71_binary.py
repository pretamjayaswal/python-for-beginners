li = [3,4,6,8,16,22,44,77,89,99,103]
target = 16
index = -1


def bin_search(li,low,high,target):
    if high >= low:
        mid  = (low + high) // 2
        if li[mid] == target:
            index = mid
            return index
        elif li[mid] > target:
            high = mid - 1        
        else:
            low = mid + 1

        return bin_search(li,low,high,target)
    else:
        return -1
    

x = bin_search(li,0,11,7)
print(x)



