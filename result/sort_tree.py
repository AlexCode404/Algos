import time


def sort_tree(arr):
    if not arr:
        return []
    
    elem, *rest = arr  
    left = [x for x in rest if x < elem]  
    right = [x for x in rest if x >= elem]  
    
    return sort_tree(left) + [elem] + sort_tree(right)  

