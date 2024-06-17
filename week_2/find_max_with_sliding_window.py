

def max_kernel(list, k):
    result = []
    sub_list = []
    for element in list:
        sub_list.append(element)
        if len(sub_list) == k:
            result.append(max(sub_list))
            del sub_list[0]
    return result       


num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
result = max_kernel(num_list, 3)
print(result)