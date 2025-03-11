def radix_sort(arr):
    if not arr:
        return arr
    
    max_length = max(len(s) for s in arr)  
    
    for pos in range(max_length - 1, -1, -1):  
        buckets = [[] for _ in range(256)]  
        
        for s in arr:
            char = ord(s[pos]) if pos < len(s) else 0  
            buckets[char].append(s)
        
        arr = [s for bucket in buckets for s in bucket] 
    
    return arr

a = 'a'
сa = ord(a)
print(сa)