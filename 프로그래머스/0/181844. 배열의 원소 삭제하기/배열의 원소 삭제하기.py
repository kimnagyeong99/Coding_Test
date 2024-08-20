def solution(arr, delete_list):
    for i in delete_list:
        while i in arr:
            arr.remove(i)
    
    return arr